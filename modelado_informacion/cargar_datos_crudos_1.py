from google.cloud import bigquery
from google.api_core.exceptions import BadRequest, NotFound
from datetime import datetime, timedelta
from utils.funciones_gcp import cargar_datos_de_gcs_a_bigquery
import os


#Defino los esquemas de cada tabla
esquema_tabla_stock = [
    bigquery.SchemaField("codigo_sucursal", "INTEGER"),
    bigquery.SchemaField("fecha_cierre_comercial", "DATETIME"),
    bigquery.SchemaField("SKU_codigo", "STRING"),
    bigquery.SchemaField("SKU_descripcion", "STRING"),
    bigquery.SchemaField("stock_unidades", "INTEGER"),
    bigquery.SchemaField("unidad", "STRING"),
    bigquery.SchemaField("n_distribuidor", "INTEGER"),
]

esquema_tabla_venta = [
    bigquery.SchemaField("codigo_sucursal", "INTEGER"),
    bigquery.SchemaField("codigo_cliente", "INTEGER"),
    bigquery.SchemaField("fecha_cierre_comercial", "DATETIME"),
    bigquery.SchemaField("SKU_codigo", "STRING"),
    bigquery.SchemaField("venta_unidades", "INTEGER"),
    bigquery.SchemaField("venta_importe", "FLOAT"),
    bigquery.SchemaField("condicion_venta", "STRING"),
    bigquery.SchemaField("n_distribuidor", "INTEGER"),
]

esquema_tabla_deuda = [
    bigquery.SchemaField("codigo_sucursal", "INTEGER"),
    bigquery.SchemaField("codigo_cliente", "INTEGER"),
    bigquery.SchemaField("fecha_cierre_comercial", "DATETIME"),
    bigquery.SchemaField("deuda_vencida", "FLOAT"),
    bigquery.SchemaField("deuda_total", "FLOAT"),
    bigquery.SchemaField("n_distribuidor", "INTEGER"),
]

esquema_tabla_cliente = [
    bigquery.SchemaField("codigo_sucursal", "INTEGER"),
    bigquery.SchemaField("codigo_cliente", "INTEGER"),
    bigquery.SchemaField("ciudad", "STRING"),
    bigquery.SchemaField("provincia", "STRING"),
    bigquery.SchemaField("estado", "STRING"),
    bigquery.SchemaField("nombre_cliente", "STRING"),
    bigquery.SchemaField("cuit", "INTEGER"),
    bigquery.SchemaField("razon_social", "STRING"),
    bigquery.SchemaField("direccion", "STRING"),
    bigquery.SchemaField("dias_visita", "STRING"),
    bigquery.SchemaField("telefono", "STRING"),
    bigquery.SchemaField("fecha_alta", "DATETIME"),
    bigquery.SchemaField("fecha_baja", "DATETIME", mode="NULLABLE"),
    bigquery.SchemaField("lat", "FLOAT"),
    bigquery.SchemaField("long", "FLOAT"),
    bigquery.SchemaField("condicion_venta", "STRING"),
    bigquery.SchemaField("deuda_vencida", "FLOAT"),
    bigquery.SchemaField("tipo_negocio", "STRING"),
    bigquery.SchemaField("n_distribuidor", "INTEGER"),
]

if __name__ == '__main__':
    ID_proyecto = "usm-infra-grupo8-401213"
    ruta_credenciales= os.path.join(os.getcwd(),"credenciales.json") #Necesario tener una clave propia!
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ruta_credenciales
    client = bigquery.Client(project=ID_proyecto)
    cant_dist = 6 # Aquí la cantidad siempre debe ser una más que la real
    cant_dias = 339
    ruta_base = "gs://datos_argideal_grupo8"
    lista_tablas = ['stock', 'venta', 'deuda', 'cliente']
    fecha_actual = datetime.now()
    
    for distribuidor in range(1, cant_dist):
        print(f"\n<Distribuidor ({distribuidor})>")
        for d in range(0, cant_dias):
            try:
                fecha_cierre = fecha_actual - timedelta(days=d)
                fecha_cierre_str = f'{fecha_cierre.year}-{fecha_cierre.month:02d}-{fecha_cierre.day:02d}'
                for table in lista_tablas:
                    ID_tabla = f"{ID_proyecto}.datos_crudos.{table}"
                    GCS_URI = f"{ruta_base}/distribuidor_{distribuidor}/{table}/{fecha_cierre_str}.csv"
                    cargar_datos_de_gcs_a_bigquery(client,GCS_URI, ID_tabla, locals()[f"esquema_tabla_{table}"])
            except BadRequest as err:
                print(err)
            except NotFound as err:
                print(err)