from google.cloud import bigquery
from utils.funciones_gcp import crear_tabla
import os

if __name__ == '__main__':
    ID_proyecto = "usm-infra-grupo8-401213"
    datawarehouse_nombre = "datawarehouse_argideal"
    ruta_credenciales= os.path.join(os.getcwd(),"credenciales.json") #Necesario tener una clave propia!
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ruta_credenciales
    client = bigquery.Client(project=ID_proyecto)

    #Queries para crear tablas temporales
    generar_dim_producto_temp = f"""
        SELECT DISTINCT
            stock.SKU_codigo AS sku_codigo,
            stock.SKU_descripcion AS descripcion
        FROM `{ID_proyecto}.datos_crudos.stock` as stock;
    """

    generar_dim_ubicacion_temp = f"""
        SELECT DISTINCT
            cliente.provincia AS Provincia,
            cliente.ciudad AS Ciudad
        FROM `{ID_proyecto}.datos_crudos.cliente` as cliente;
    """

    #Queries para crear tablas finales con IDs subrogados
    generar_dim_producto = f"""
        SELECT
            ROW_NUMBER() OVER() AS id_producto,
            sku_codigo AS Codigo_SKU,
            descripcion AS nombre_producto
        FROM `{ID_proyecto}.{datawarehouse_nombre}.temp_producto`
        ORDER BY id_producto;
    """

    generar_dim_ubicacion = f"""
        SELECT
            ROW_NUMBER() OVER() AS id_ubicacion,
            Provincia,
            Ciudad
        FROM `{ID_proyecto}.{datawarehouse_nombre}.temp_ubicacion`
        ORDER BY id_ubicacion;
    """

    #Queries para crear tablas finales con sus IDs originales
    generar_dim_cliente= f"""
        SELECT DISTINCT
            cliente.codigo_cliente,
            cliente.codigo_sucursal,
            cliente.n_distribuidor,
            cliente.nombre_cliente,
            cliente.tipo_negocio
        FROM `{ID_proyecto}.datos_crudos.cliente` as cliente
        ORDER BY cliente.codigo_cliente;
    """

    #Genero listas para asociar las tablas con las queriesque las generan
    lista_tablas_temp = ['temp_producto', 'temp_ubicacion']
    lista_querys_temp = [generar_dim_producto_temp, generar_dim_ubicacion_temp]

    lista_tablas_final = ['dim_producto', 'dim_ubicacion', 'dim_cliente']
    lista_querys_final = [generar_dim_producto, generar_dim_ubicacion, generar_dim_cliente]

    #Primero genero las tablas temporales
    for tabla, query in zip(lista_tablas_temp, lista_querys_temp):
        TABLE_ID = f"{ID_proyecto}.{datawarehouse_nombre}.{tabla}"
        crear_tabla(
            client=client,
            ID_tabla_a_crear=TABLE_ID,
            query=query,
            metodo_escritura="WRITE_TRUNCATE"
        )

    #Y luego genero las tablas finales, cuyos querys se apoyan en las tablas temporales
    for tabla, query in zip(lista_tablas_final, lista_querys_final):
        TABLE_ID = f"{ID_proyecto}.{datawarehouse_nombre}.{tabla}"
        
        crear_tabla(
            client=client,
            ID_tabla_a_crear=TABLE_ID,
            query=query,
            metodo_escritura="WRITE_TRUNCATE"
        )

        #Cliente no tiene tabla temporal!
        if tabla != "dim_cliente":
        
            #Luego de crear la tabla, elimino la tabla temporal correspondiente
            TEMP_TABLE_ID = f"{ID_proyecto}.{datawarehouse_nombre}.temp_{tabla.split('_')[1]}"
            client.delete_table(TEMP_TABLE_ID, not_found_ok=True)
            print(f"Tabla temporal {TEMP_TABLE_ID} eliminada.")  
