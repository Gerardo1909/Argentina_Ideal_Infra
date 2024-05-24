from google.cloud import bigquery
from utils.funciones_gcp import crear_tabla
import os
        
if __name__ == '__main__':
    ID_proyecto = "usm-infra-grupo8-401213"
    datawarehouse_nombre = "datawarehouse_argideal"
    ruta_credenciales= os.path.join(os.getcwd(),"credenciales.json") #Necesario tener una clave propia!
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ruta_credenciales
    client = bigquery.Client(project=ID_proyecto)
    
    #Primero hago la query para juntar la tabla de ventas con la ubicación
    generar_fact_ventas_temp = f"""
    SELECT
        tabla_cliente.ciudad,
        tabla_cliente.provincia,
        tabla_venta.codigo_sucursal,
        tabla_venta.codigo_cliente,
        tabla_venta.fecha_cierre_comercial,
        tabla_venta.SKU_codigo,
        tabla_venta.venta_unidades,
        tabla_venta.venta_importe
    FROM `{ID_proyecto}.datos_crudos.venta` AS tabla_venta
    JOIN `{ID_proyecto}.datos_crudos.cliente` AS tabla_cliente
        ON tabla_venta.codigo_sucursal = tabla_cliente.codigo_sucursal AND tabla_venta.codigo_cliente = tabla_cliente.codigo_cliente
    """

    generar_fact_ventas= f"""
    SELECT
        dim_cliente.codigo_cliente,
        dim_fechas.id_fecha,
        dim_producto.id_producto,
        dim_ubicacion.id_ubicacion,
        fact_ventas_temp.venta_unidades,
        fact_ventas_temp.venta_importe
    FROM `{ID_proyecto}.{datawarehouse_nombre}.fact_ventas_temp` AS fact_ventas_temp
    JOIN `{ID_proyecto}.{datawarehouse_nombre}.dim_ubicacion` AS dim_ubicacion
        ON fact_ventas_temp.ciudad = dim_ubicacion.Ciudad AND fact_ventas_temp.provincia = dim_ubicacion.Provincia
    JOIN `{ID_proyecto}.{datawarehouse_nombre}.dim_producto` AS dim_producto
        ON fact_ventas_temp.SKU_codigo = dim_producto.Codigo_SKU 
    JOIN `{ID_proyecto}.{datawarehouse_nombre}.dim_fechas` AS dim_fechas
        ON fact_ventas_temp.fecha_cierre_comercial = dim_fechas.fecha_cierre_comercial
    JOIN `{ID_proyecto}.{datawarehouse_nombre}.dim_cliente` AS dim_cliente
        ON fact_ventas_temp.codigo_cliente = dim_cliente.codigo_cliente
    """

    #Creo la tabla temporal de la cual se apoyará la tabla de hechos de ventas
    ID_tabla_temporal = f"{ID_proyecto}.{datawarehouse_nombre}.fact_ventas_temp"
    crear_tabla(
            client=client,
            ID_tabla_a_crear=ID_tabla_temporal,
            query=generar_fact_ventas_temp,
            metodo_escritura="WRITE_TRUNCATE"
        )
    
    #Ahora si creo la tabla de hechos de ventas usando la tabla temporal
    ID_tabla_hechos = f"{ID_proyecto}.{datawarehouse_nombre}.fact_ventas"
    crear_tabla(
            client=client,
            ID_tabla_a_crear=ID_tabla_hechos,
            query=generar_fact_ventas,
            metodo_escritura="WRITE_TRUNCATE"
        )

    #Elimino la tabla temporal
    client.delete_table(ID_tabla_temporal, not_found_ok=True)
    print(f"Tabla temporal {ID_tabla_temporal} eliminada.")