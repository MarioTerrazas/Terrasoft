# Arquitectura de Base de Datos de FerreSys

**Versión:** 1.0

**Estado:** En diseño

**Proyecto:** FerreSys

**Sprint:** Sprint 2 — Arquitectura de FerreSys

---

# Objetivo

Definir la arquitectura de la base de datos de FerreSys antes de comenzar su implementación física.

Este documento describe las entidades del negocio, sus relaciones y los principios que regirán el diseño de la base de datos.

No contiene instrucciones SQL.

---

# Filosofía

La base de datos de FerreSys deberá representar el negocio real de una ferretería.

Cada tabla deberá existir porque representa una entidad del negocio y no simplemente porque sea necesaria para programar.

Toda información deberá almacenarse una sola vez.

La prioridad será:

- Integridad.
- Escalabilidad.
- Claridad.
- Rendimiento.
- Facilidad de mantenimiento.

---

# Principios de diseño

La base de datos seguirá los siguientes principios:

- Normalización.
- Integridad referencial.
- Uso de claves primarias.
- Uso de claves foráneas.
- Auditoría.
- Modularidad.
- Escalabilidad.
- Nombres consistentes.

---

# Entidades principales

La primera versión de FerreSys estará compuesta por las siguientes entidades principales.

## Configuración

- Empresa
- Sucursal
- Almacén

---

## Seguridad

- Usuario
- Rol
- Permiso

---

## Clientes

- Cliente

---

## Proveedores

- Proveedor

---

## Productos

- Producto
- Categoría
- Marca
- Unidad de Medida

---

## Inventario

- Inventario
- Movimiento de Inventario

---

## Compras

- Compra
- DetalleCompra

---

## Pedidos

- Pedido
- DetallePedido

---

## Ventas

- Venta
- DetalleVenta

---

## Facturación

- Factura

---

## Caja

- Caja
- MovimientoCaja

---

## Logística

- Chofer
- Vehículo
- Entrega

---

## Auditoría

- Auditoría
- Notificación

---

# Relaciones generales

Empresa

↓

Sucursal

↓

Almacén

↓

Producto

↓

Inventario

↓

Pedido

↓

Venta

↓

Factura

↓

Caja

↓

Reportes

---

# Principios de relaciones

Un cliente puede tener muchos pedidos.

Un pedido pertenece a un solo cliente.

Un pedido puede contener muchos productos.

Un producto puede aparecer en muchos pedidos.

Un pedido puede generar una venta.

Una venta puede generar una factura.

Una compra genera movimientos de inventario.

Una venta genera movimientos de inventario.

Una venta genera movimientos de caja.

Una entrega pertenece a un pedido.

Un chofer puede realizar muchas entregas.

Un vehículo puede realizar muchas entregas.

---

# Auditoría

Las operaciones importantes deberán generar un registro histórico.

Ejemplos:

- Cambio de precio.
- Eliminación lógica.
- Cambio de stock.
- Cambio de estado del pedido.
- Apertura de caja.
- Cierre de caja.

---

# Eliminación de información

No se eliminarán registros importantes físicamente.

Se utilizará eliminación lógica cuando sea necesario para conservar el historial.

---

# Identificadores

Todas las tablas utilizarán una clave primaria.

Las relaciones utilizarán claves foráneas.

No se utilizarán datos descriptivos como claves.

---

# Convención de nombres

Las tablas utilizarán nombres en singular.

Ejemplo:

Producto

Cliente

Pedido

Venta

Factura

Las columnas utilizarán nombres claros y consistentes.

---

# Fechas

Todas las entidades importantes deberán registrar:

- Fecha de creación.
- Fecha de actualización.

Cuando corresponda:

- Usuario creador.
- Usuario modificador.

---

# Escalabilidad

La base de datos deberá permitir incorporar nuevos módulos sin modificar la estructura existente.

---

# Compatibilidad

La implementación oficial será realizada en PostgreSQL.

El diseño deberá evitar características específicas que dificulten futuras migraciones.

---

# Objetivo final

Construir una base de datos robusta, organizada y preparada para acompañar el crecimiento de FerreSys durante muchos años.