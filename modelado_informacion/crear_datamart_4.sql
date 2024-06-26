CREATE TABLE datamart_marketing.volumen_ventas AS
SELECT
  EXTRACT(MONTH FROM ventas.fecha_cierre_comercial) AS mes,
  EXTRACT(QUARTER FROM ventas.fecha_cierre_comercial) AS trimestre,
  dim_cliente.n_distribuidor,
  dim_cliente.tipo_negocio,
  dim_ubicacion.Provincia,
  dim_ubicacion.Ciudad,
  dim_producto.nombre_producto,
  ventas.venta_unidades,
  ventas.venta_importe
FROM
  datawarehouse_argideal.fact_ventas ventas
JOIN
  `datawarehouse_argideal.dim_producto` dim_producto
    ON
      ventas.id_producto = dim_producto.id_producto
JOIN
  `datawarehouse_argideal.dim_cliente` dim_cliente
    ON
      ventas.codigo_cliente = dim_cliente.codigo_cliente
JOIN
  `datawarehouse_argideal.dim_ubicacion` dim_ubicacion
    ON
      ventas.id_ubicacion = dim_ubicacion.id_ubicacion;