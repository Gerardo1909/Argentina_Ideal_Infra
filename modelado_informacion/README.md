# Planteo del problema - departamento de Marketing

## Nuestra hipótesis

Desde la gerencia de **"Argentina ideal"** están buscando estrategias de mercado para maximizar la venta de sus productos menos vendidos en un ciclo trimestral. Desde el departamento de Marketing proponen la hipótesis de que existe cierta correlación entre la estacionalidad y la baja venta de ciertos productos.

* Se sugiere que cada trimestre hay productos que consistentemente tienen menor demanda.

* Además, se sugiere que según la región y las características demográficas, la cantidad de ventas de ciertos productos menos vendidos puede variar.

## Preguntas a responder

* ¿Cuáles son los productos que tienen menor volumen de ventas cada trimestre?

* ¿Durante qué trimestre tienen los productos el menor volumen de ventas por región?

* Para los productos con menor volumen de ventas, ¿en qué tipo de establecimiento se suelen vender menos?

* ¿Qué factores podrían estar influyendo en las bajas ventas de estos productos en cada trimestre?

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

En este directorio, podrán encontrar los scripts de Python que utilizamos para manipular la información, generar el datawarehouse y construir datamarts. A continuación, dejamos una imagen del modelo de datawarehouse que implementaremos:

![Modelo Datawarehouse](./Modelo_dws_grupo8_infra.png)