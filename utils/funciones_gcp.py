from google.cloud import bigquery

def crear_tabla(client, ID_tabla_a_crear, query, metodo_escritura):
    """
    Esta función crea una nueva tabla en Google BigQuery utilizando una consulta SQL y la disposición de escritura dada.

    Parameters:
    client (bigquery.Client): El cliente de BigQuery.
    ID_tabla_a_crear (str): El ID de la tabla que se va a crear en el formato 'proyecto.dataset.tabla'.
    query (str): La consulta SQL que se va a ejecutar para llenar la tabla.
    metodo_escritura (str): La disposición de escritura para la tabla. Puede ser uno de los siguientes:
        - 'WRITE_TRUNCATE': Si la tabla existe sobre escribe los datos.
        - 'WRITE_APPEND': Si la tabla existe agrega datos en la tabla.
        - 'WRITE_EMPTY': Solo escribe datos cuando la tabla existe y no tiene datos.

    Returns:
    None. Si la ejecución de la consulta es exitosa, imprime el resultado. Si se produce un error, imprime el mensaje de error.
    """

    # Crea un objeto QueryJobConfig con la disposición de escritura especificada
    job_config = bigquery.QueryJobConfig(
        destination = ID_tabla_a_crear,
        write_disposition = metodo_escritura
    )

    # Ejecuta la consulta de manera asíncrona
    query_job = client.query(query, job_config=job_config)

    # Espera a que finalice el trabajo de consulta y maneja cualquier excepción
    try:
        query_job.result()
        print(f"Tabla {ID_tabla_a_crear} creada y datos insertados con éxito.")
    except Exception as err:
        print(f"Error al crear la tabla {ID_tabla_a_crear}: {err}")
        
def cargar_datos_de_gcs_a_bigquery(GCS_URI, ID_tabla, esquema_tabla):
    """
    Esta función carga datos de un bucket de Google Cloud Storage (GCS) a una tabla específica de BigQuery.

    Parameters:
    GCS_URI (str): El Identificador Uniforme de Recursos (URI) del bucket de GCS y el archivo a cargar.
    ID_tabla (str): El ID de la tabla de BigQuery donde se cargarán los datos.
    esquema_tabla (list): El esquema de la tabla de BigQuery.

    Returns:
    None

    Raises:
    BadRequest: Si la solicitud no es válida.
    NotFound: Si el bucket de GCS especificado o la tabla de BigQuery no se encuentran.
    """

    #Creo un objeto LoadJobConfig con el esquema especificado, formato de origen, disposición de escritura y filas de encabezado que omitir.
    job_config = bigquery.LoadJobConfig(
        schema=esquema_tabla,
        source_format=bigquery.SourceFormat.CSV,
        write_disposition = 'WRITE_APPEND',
        skip_leading_rows=1
    )

    #Cargo los datos del URI de GCS especificado a la tabla de BigQuery especificada utilizando el objeto LoadJobConfig.
    load_job = client.load_table_from_uri(GCS_URI, ID_tabla, job_config=job_config)

    #Espero a que se complete el trabajo de carga.
    load_job.result()

    #Obtengo los metadatos de la tabla actualizados.
    tabla = client.get_table(ID_tabla)

    #Voy imprimiendo el número de filas cargados a la tabla
    print(f"Se cargaron {tabla.num_rows} filas a la tabla {ID_tabla}")