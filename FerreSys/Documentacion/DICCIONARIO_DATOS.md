# Diccionario de Datos de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2

---

# Objetivo

Definir el significado de cada entidad del sistema antes de construir la base de datos física en PostgreSQL.

Cada entidad representa un concepto del negocio.

---

# Empresa

## Descripción

Representa la empresa propietaria del sistema.

## Responsabilidad

Guardar la información fiscal y comercial de la empresa.

## Se relaciona con

- Sucursal
- Usuario

---

# Sucursal

## Descripción

Representa una sede física de la empresa.

## Responsabilidad

Organizar operaciones por ubicación.

## Se relaciona con

- Empresa
- Almacén
- Caja

---

# Almacén

## Descripción

Lugar donde se almacenan los productos.

## Responsabilidad

Controlar el inventario físico.

## Se relaciona con

- Producto
- Inventario

---

# Usuario

## Descripción

Persona autorizada para utilizar FerreSys.

## Responsabilidad

Operar el sistema según sus permisos.

## Se relaciona con

- Rol
- Pedido
- Venta
- Compra
- Caja
- Auditoría

---

# Rol

## Descripción

Conjunto de permisos asignados a un usuario.

## Responsabilidad

Controlar el acceso al sistema.

## Se relaciona con

- Usuario
- Permiso

---

# Permiso

## Descripción

Acción específica permitida dentro del sistema.

## Responsabilidad

Restringir funciones.

---

# Cliente

## Descripción

Persona o empresa que compra productos.

## Responsabilidad

Registrar información comercial del cliente.

## Se relaciona con

- Pedido
- Venta
- Factura

---

# Proveedor

## Descripción

Empresa que suministra mercadería.

## Responsabilidad

Registrar compras y abastecimiento.

## Se relaciona con

- Compra

---

# Categoría

## Descripción

Agrupa productos similares.

## Responsabilidad

Organizar el catálogo.

## Se relaciona con

- Producto

---

# Marca

## Descripción

Fabricante o marca comercial del producto.

## Responsabilidad

Clasificar productos.

## Se relaciona con

- Producto

---

# Unidad de Medida

## Descripción

Unidad utilizada para vender un producto.

Ejemplos:

- Bolsa
- Caja
- Metro
- Unidad
- Litro

## Se relaciona con

- Producto

---

# Producto

## Descripción

Artículo comercializado por la ferretería.

## Responsabilidad

Representar un producto disponible para compra y venta.

## Se relaciona con

- Inventario
- Compra
- Pedido
- Venta

---

# Inventario

## Descripción

Cantidad disponible de cada producto.

## Responsabilidad

Controlar existencias.

## Se relaciona con

- Producto
- MovimientoInventario

---

# MovimientoInventario

## Descripción

Registro histórico de entradas y salidas.

## Responsabilidad

Mantener trazabilidad del inventario.

## Se relaciona con

- Inventario
- Compra
- Venta
- Ajustes

---

# Compra

## Descripción

Registro de adquisición de productos.

## Responsabilidad

Ingresar mercadería.

## Se relaciona con

- Proveedor
- DetalleCompra

---

# DetalleCompra

## Descripción

Productos incluidos en una compra.

## Responsabilidad

Registrar cantidades y precios.

---

# Pedido

## Descripción

Solicitud realizada por un cliente.

## Responsabilidad

Controlar el proceso completo de venta.

## Se relaciona con

- Cliente
- DetallePedido
- Venta
- Entrega

---

# DetallePedido

## Descripción

Productos incluidos en un pedido.

## Responsabilidad

Registrar cantidades, precios y subtotales.

---

# Venta

## Descripción

Operación comercial confirmada.

## Responsabilidad

Registrar la venta realizada.

## Se relaciona con

- Cliente
- Pedido
- Factura
- Caja

---

# DetalleVenta

## Descripción

Productos vendidos.

## Responsabilidad

Guardar cantidades y precios.

---

# Factura

## Descripción

Documento tributario generado a partir de una venta.

## Responsabilidad

Cumplir la normativa fiscal.

## Se relaciona con

- Venta

---

# Caja

## Descripción

Registro del dinero administrado durante la jornada.

## Responsabilidad

Controlar ingresos y egresos.

## Se relaciona con

- MovimientoCaja
- Venta

---

# MovimientoCaja

## Descripción

Registro histórico de todos los movimientos económicos.

## Responsabilidad

Mantener trazabilidad financiera.

---

# Chofer

## Descripción

Empleado encargado de realizar entregas.

## Responsabilidad

Transportar pedidos.

## Se relaciona con

- Vehículo
- Entrega

---

# Vehículo

## Descripción

Medio de transporte utilizado para entregas.

## Responsabilidad

Mover la mercadería.

## Se relaciona con

- Chofer
- Entrega

---

# Entrega

## Descripción

Proceso de despacho de un pedido.

## Responsabilidad

Controlar el transporte y la recepción.

## Se relaciona con

- Pedido
- Chofer
- Vehículo

---

# Auditoría

## Descripción

Registro de eventos importantes del sistema.

## Responsabilidad

Permitir trazabilidad.

## Se relaciona con

- Usuario

---

# Notificación

## Descripción

Aviso generado por el sistema.

## Responsabilidad

Informar situaciones relevantes.

## Se relaciona con

- Usuario

---

# Principio del Diccionario de Datos

Toda nueva entidad deberá incorporarse primero a este documento antes de ser implementada en la base de datos.

Este documento será la referencia oficial para el diseño del modelo lógico y físico de FerreSys.