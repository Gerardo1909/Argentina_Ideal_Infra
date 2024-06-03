# Planteo del problema - departamento de Marketing

## El código de este directorio

En este directorio, podrán encontrar los scripts de Python y SQL que utilizamos para subir los datos crudos, generar el datawarehouse y construir el datamart para el manejo de la información de **"Argentina Ideal"**. Para ejecutarlos y no obtener ningún error inesperado les hemos colocado un número al final de su nombre que indica el orden en que deben ser ejecutados los scripts. A continuación dejamos una explicación del propósito de cada archivo:

```sh
C:.
├───modelado_informacion
│       cargar_datos_crudos_1.py #Como su nombre indica, es el primero a ser ejecutado ya que carga los datos crudos desde el Storage
│       crear_dimensiones_2.py #Una vez cargados los datos crudos, este archivo se encarga de generar los archivos de dimensiones del datawarehouse
│       crear_fact_table_3.py #Este archivo se encarga de crear la tabla de hechos, su creación se apoya de los archivos de dimensiones
│       crear_datamart_4.py #Este archivo se encarga de generar el datamart del departamento de marketing, se ejecuta desde GCP
│       ..
```

## Nuestro caso de negocios

Desde la gerencia de **Argentina ideal** se ha identificado que en el último año ha habido productos con un bajo volumen de ventas, lo cual ha representado pérdidas significativas para la empresa.

Después de una exhaustiva reunión con todos los departamentos, se ha encomendado al departamento de Marketing la tarea de idear nuevas estrategias de ventas con el objetivo de maximizar la venta de estos productos y mantener la competitividad de Argentina Ideal en el mercado.

## Hipótesis desde el departamento de Marketing

El departamento de Marketing ha propuesto la hipótesis de que existe una correlación entre la estacionalidad y la baja venta de ciertos productos. Se sugiere que cada trimestre hay productos que consistentemente tienen una menor demanda. Además, se plantea que la cantidad de ventas de estos productos menos vendidos puede variar según la región y las características demográficas.

## Preguntas a responder

* ¿Cuáles son los productos que tienen menor volumen de ventas en general?

* Para los productos con menor volumen de ventas en general, ¿en que trimestre tienen peor desempeño?, ¿en otro trimestre hay un comportamiento parecido?

* Para los trimestres encontrados, ¿en que provincia hubo un peor desempeño de los productos hallados?

* Entre las provincias halladas, ¿que distribuidor tuvo el volumen de ventas más bajo?

## Plan de acción 

1. Utilizar la información almacenada en el datawarehouse de **"Argentina ideal"** y generar un datamart con la información relevante para el departamento de Marketing.

2. Realizar un análisis exhaustivo para responder las preguntas planteadas, utilizando tableros y extrayendo información valiosa de los mismos.

3. Identificar patrones de ventas bajas y proponer estrategias para incrementar las ventas de estos productos. Esto puede incluir promociones especiales, cambios en el packaging, campañas de marketing dirigidas o la inclusión de estos productos en combos o paquetes atractivos.

4. Desarrollar y probar campañas de marketing específicas para los productos identificados con menores ventas, ajustando la estrategia según la región y las características demográficas.

## Modelo de datawarehouse para encarar nuestro caso de negocio

Desde nuestro grupo de trabajo, hemos decidido construir un datawarehouse que nos ayude a responder de la mejor forma las preguntas que hemos planteado. Para ello, utilizaremos un **modelo estrella** con las siguientes características:

* **Dimensión "ubicación"**: Nos permitirá analizar el volumen de ventas discriminando por provincia y ciudades. Esto nos ayudará a tener una idea más clara sobre en qué zonas es más necesario o recomendable **tomar acción**.

* **Dimensión "productos"**: Contiene información sobre los productos que distribuye **"Argentina Ideal"**. Esta dimensión, junto con la tabla de hechos y otras dimensiones, nos permitirá analizar aquellos productos con menor volumen de ventas.

* **Dimensión "cliente"**: Contiene información relacionada con los clientes de los distribuidores. De esta dimensión podemos obtener **insights valiosos** como identificar los tipos de negocios que presentan un menor volumen de ventas, los productos que venden dichos negocios y entender su comportamiento temporalmente.

* **Hechos "ventas"**: Contiene información sobre las ventas realizadas por día, a cada cliente individual, de un producto específico. Además, contiene información sobre la fecha en la que se realizó una venta. Esto nos permitirá segmentar la información según su temporalidad, lo cual es el **foco principal** de este análisis.

A continuación, dejamos una imagen del modelo de datawarehouse que hemos estado describiendo:

![Modelo Datawarehouse](./Modelo_dws_grupo8_infra.png)