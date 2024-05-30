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

## Nuestra hipótesis

Desde la gerencia de **"Argentina ideal"** están buscando estrategias de mercado para maximizar la venta de sus productos menos vendidos en un ciclo trimestral. Desde el departamento de Marketing proponen la hipótesis de que existe cierta correlación entre la estacionalidad y la baja venta de ciertos productos.

* Se sugiere que cada trimestre hay productos que consistentemente tienen menor demanda.

* Además, se sugiere que según la región y las características demográficas, la cantidad de ventas de ciertos productos menos vendidos puede variar.

## Preguntas a responder

* ¿Cuáles son los productos que tienen menor volumen de ventas en general?

* Para los productos con menor volumen de ventas en general, ¿en que trimestre tienen peor desempeño?, ¿en otro trimestre hay un comportamiento parecido?

* Para los trimestres encontrados, ¿que distribuidor vendió más los productos con menor volumen de ventas?

* Para los trimestres encontrados, ¿en que provincia hubo un peor desempeño de los productos con menor volumen de ventas?

* ¿Que factores podrían estar influyendo en el bajo volumen de venta de estos productos?

## Plan de acción 

* Utilizar la información almacenada en el datawarehouse de **"Argentina ideal"** y generar un datamart con la información que resulte relevante para el departamento de Marketing.

* Realizar el análisis pertinente para lograr responder las preguntas planteadas, para este caso usando tableros y extrayendo información valiosa de los mismos.

* Identificar patrones de ventas bajas y proponer estrategias para incrementar las ventas de estos productos, tales como promociones especiales, cambios en el packaging, campañas de marketing dirigidas, o la inclusión de estos productos en combos o paquetes atractivos.

* Desarrollar y testar campañas de marketing específicas cada trimestre para los productos identificados con menores ventas, ajustando la estrategia según la región y características demográficas.

## Modelo de warehouse para encarar nuestro problema/hipótesis

Desde nuestro grupo de trabajo, hemos decidido construir un datawarehouse que nos ayude a responder de la mejor forma las preguntas que hemos planteado. Para ello, utilizaremos un **modelo estrella** con las siguientes características:

* **Dimensión "fechas"**: Nos ayudará a realizar el análisis temporal que requiere nuestra hipótesis. En su nivel más detallado, incluye información sobre el día de la venta, representado como **fecha_cierre_comercial**. En su nivel más alto, proporciona información sobre el cuatrimestre en el que se realizó la venta del producto.

* **Dimensión "ubicación"**: Nos permitirá analizar el volumen de ventas discriminando por provincia y ciudades. Esto nos ayudará a tener una idea más clara sobre en qué zonas es más necesario o recomendable **tomar acción**.

* **Dimensión "productos"**: Contiene información sobre los productos que distribuye **"Argentina Ideal"**. Esta dimensión, junto con la tabla de hechos y otras dimensiones, nos permitirá analizar aquellos productos con menor volumen de ventas.

* **Dimensión "cliente"**: Contiene información relacionada con los clientes de los distribuidores. De esta dimensión podemos obtener **insights valiosos** como identificar los tipos de negocios que presentan un menor volumen de ventas, los productos que venden dichos negocios y entender su comportamiento temporalmente.

* **Hechos "ventas"**: Contiene información sobre las ventas realizadas por día, a cada cliente individual, de un producto específico.

A continuación, dejamos una imagen del modelo de datawarehouse que hemos estado describiendo:

![Modelo Datawarehouse](./Modelo_dws_grupo8_infra.png)