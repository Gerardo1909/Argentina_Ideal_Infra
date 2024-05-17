# Generación de datos

## Descipción de los archivos

El sistema de los distribuidores cuenta con un componente de software que es capaz de generar, a partir de la información de su sistema de ventas, 
los archivos en formato csv. Los notebooks que encontrarán en este directorio son los que generan dicha información y la suben a un bucket de 
**Google Cloud Storage**, a continuación dejamos una descripción de cada archivo:

* **Venta:** Contiene la venta que los distribuidores ha realizado a los negocios minoristas en un día. En este archivo se debe considerar para un mismo cliente, misma fecha, mismo SKU (código de producto), la sumatoria de lo facturado considerando en el archivo una sola línea para cada combinación de Cliente/fecha/SKU.

* **Deuda:** Contiene la deuda que los negocios minoristas tienen con los distribuidores. Este archivo debe contener los montos de deuda vencida y total por cliente por día.

* **Stock:** Debe contener el saldo del stock al cierre de cada día, de todos los productos que tenga el distribuidor asignado a la sucursal. Estos, deben sumarizar tanto los stocks en almacén o depósito. Este archivo deberá contener información del día de cierre comercial.

* **Maestro/Cliente:** Deben incluirse en este archivo a todos los clientes del distribuidor. Los clientes que sean dados de baja deberán reflejarse con el campo 
Estado = I.

## Flujo de la información

Para un mejor entendimiento de como se maneja la información en **"Argentina Ideal"** les dejamos una imagen:

![Flujo información](./TP_final_grupo8.drawio.png)
