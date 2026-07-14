# Modelo Lógico de FerreSys

**Versión:** 1.0

**Estado:** En diseño

**Proyecto:** FerreSys

**Sprint:** Sprint 2

---

# Objetivo

Definir las relaciones entre las entidades del sistema antes de construir la base de datos física.

Este documento representa el puente entre el análisis del negocio y PostgreSQL.

---

# Relaciones principales

## Empresa

Tiene muchas

↓

Sucursales

---

## Sucursal

Tiene muchos

↓

Almacenes

↓

Usuarios

↓

Cajas

---

## Rol

Tiene muchos

↓

Usuarios

---

## Usuario

Puede registrar

↓

Clientes

Productos

Compras

Pedidos

Ventas

Caja

---

## Cliente

Puede tener muchos

↓

Pedidos

↓

Ventas

↓

Facturas

---

## Proveedor

Puede tener muchas

↓

Compras

---

## Categoría

Puede contener muchos

↓

Productos

---

## Marca

Puede contener muchos

↓

Productos

---

## Unidad de Medida

Puede utilizarse en muchos

↓

Productos

---

## Producto

Puede aparecer en muchos

↓

DetallesPedido

↓

DetallesVenta

↓

DetallesCompra

↓

MovimientosInventario

---

## Compra

Tiene muchos

↓

DetalleCompra

---

## Pedido

Tiene muchos

↓

DetallePedido

↓

Una Venta

↓

Una Entrega

---

## Venta

Tiene muchos

↓

DetalleVenta

↓

Una Factura

↓

Muchos MovimientosCaja

---

## Inventario

Tiene muchos

↓

MovimientosInventario

---

## Chofer

Puede realizar muchas

↓

Entregas

---

## Vehículo

Puede realizar muchas

↓

Entregas

---

# Cardinalidades

Empresa

1 ---- N Sucursal

Sucursal

1 ---- N Almacén

Rol

1 ---- N Usuario

Cliente

1 ---- N Pedido

Pedido

1 ---- N DetallePedido

Producto

1 ---- N DetallePedido

Compra

1 ---- N DetalleCompra

Producto

1 ---- N DetalleCompra

Venta

1 ---- N DetalleVenta

Producto

1 ---- N DetalleVenta

Producto

1 ---- N MovimientoInventario

Inventario

1 ---- N MovimientoInventario

Pedido

1 ---- 1 Entrega

Chofer

1 ---- N Entrega

Vehículo

1 ---- N Entrega

Venta

1 ---- 1 Factura

Caja

1 ---- N MovimientoCaja

---

# Relaciones N:M

Pedido ←→ Producto

Se resuelve mediante:

DetallePedido

Venta ←→ Producto

Se resuelve mediante:

DetalleVenta

Compra ←→ Producto

Se resuelve mediante:

DetalleCompra

---

# Reglas de Integridad

No podrá existir un pedido sin cliente.

No podrá existir una venta sin detalles.

No podrá existir una factura sin venta.

No podrá eliminarse un producto con movimientos registrados.

No podrá eliminarse un cliente con historial.

No podrá existir una entrega sin pedido.

Todo movimiento de inventario deberá estar asociado a una causa.

---

# Objetivo final

El modelo lógico será utilizado para construir el modelo físico de PostgreSQL.