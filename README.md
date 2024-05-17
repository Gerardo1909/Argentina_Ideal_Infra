# Trabajo Práctico Final - Infraestructura para la Ciencia de Datos

## Enunciado 

La empresa de producción y venta de productos masivos llamada **“Argentina Ideal”**, organiza sus ventas en el territorio argentino con lo que en el mercado se denomina venta indirecta.

En esta modalidad de venta la toma del pedido, el reparto y facturación se encuentra a cargo de empresas distribuidoras. De esta forma **“Argentina Ideal”** llega a los comercios minoristas (almacenes, supermercados, free-shops, etc.) mediante los distribuidores (compañía -> distribuidor/mayorista -> comercio minorista). Los productos que se fabrican se encuentran acopiados en los distintos almacenes del único centro logístico que tiene **“Argentina Ideal”** ubicado en Capital Federal.

Las ventas se encuentran organizadas en 4 regiones a lo largo de todo el país, CABA, Norte, Centro, y Sur. Un distribuidor podría vender y distribuir en más de una región, y podría tener más de una sucursal por región. La modalidad de venta es lo que se denomina **“pre-venta”**: un vendedor sale el día n a tomar los pedidos y los repartidores al día siguiente (n+1) se encargan de llevar la mercadería a los distintos comercios.

## ¿Cuál es nuestra meta como grupo?

Nosotros nos encargaremos de crear la infraestructura necesaria para gestionar la información que **"Argentina Ideal"** recibe diariamente de los distribuidores. Esto nos permitirá responder preguntas de negocio, comprender sus necesidades y tomar acciones adecuadas.

Para lograrlo, utilizaremos **Google Cloud Platform (GCP)**, el lenguaje de programación **Python** y el lenguaje para la manipulación de bases de datos **SQL**. Seguiremos varias fases: desde la generación de la información de los distribuidores y su carga en GCP, hasta el modelado de un datawarehouse, la creación de datamarts específicos para distintas áreas del negocio y, finalmente, la visualización de la información relevante a través de dashboards.

