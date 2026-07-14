# Productos de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2 — Arquitectura de FerreSys

---

# Objetivo

Definir cómo administrará FerreSys los productos comercializados por la ferretería.

El módulo de productos será el punto de partida para el inventario, las compras, las ventas, los pedidos y la facturación.

---

# ¿Qué es un producto?

Un producto representa cualquier artículo que la empresa compra, almacena y vende.

Ejemplos:

- Cemento
- Arena
- Ripio
- Fierro
- Clavos
- Tornillos
- Pintura
- Tubería PVC
- Pegamento
- Herramientas

---

# Información principal

Cada producto deberá almacenar como mínimo:

- Código interno.
- Código de barras (opcional).
- Nombre.
- Descripción.
- Categoría.
- Marca.
- Unidad de medida.
- Precio de compra.
- Precio de venta.
- Stock actual.
- Stock mínimo.
- Ubicación en almacén.
- Estado.
- Observaciones.

---

# Clasificación

Los productos podrán clasificarse mediante:

- Categoría.
- Marca.
- Proveedor principal.
- Unidad de medida.

Ejemplos de categorías:

- Cemento
- Hierros
- Pinturas
- Electricidad
- Plomería
- Herramientas
- Tornillería
- Agregados

---

# Estado del producto

Un producto podrá encontrarse en uno de los siguientes estados:

- Activo.
- Inactivo.
- Agotado.
- Descontinuado.

---

# Control de precios

Cada producto registrará:

- Precio de compra.
- Precio de venta.
- Historial de cambios de precio.

El cambio de precios deberá quedar registrado en la auditoría.

---

# Control de inventario

FerreSys permitirá conocer en todo momento:

- Stock disponible.
- Stock comprometido en pedidos.
- Stock mínimo.
- Última compra.
- Última venta.
- Fecha del último movimiento.

---

# Movimientos

Todo cambio deberá generar un movimiento de inventario.

Tipos de movimiento:

- Compra.
- Venta.
- Ajuste.
- Devolución.
- Pérdida.
- Daño.
- Inventario físico.

---

# Relación con otros módulos

Producto se relaciona con:

- Inventario.
- Pedido.
- Venta.
- Compra.
- Factura.
- Reportes.

---

# Alertas

El sistema notificará cuando:

- El stock llegue al mínimo.
- El producto no tenga movimientos durante mucho tiempo.
- El precio de compra aumente significativamente.
- Existan diferencias de inventario.

---

# Búsqueda

Los productos podrán buscarse por:

- Código.
- Nombre.
- Categoría.
- Marca.
- Código de barras.
- Proveedor.

---

# Futuras funcionalidades

En versiones posteriores se podrán incorporar:

- Fotografías.
- Múltiples proveedores.
- Múltiples listas de precios.
- Productos compuestos.
- Kits.
- Promociones.
- Variantes.
- Control por lote.
- Control por serie.
- Fecha de vencimiento.
- IA para predicción de compras.

---

# Principios

Todo producto deberá:

- Tener una identificación única.
- Mantener historial.
- Conservar trazabilidad.
- Poder relacionarse con pedidos y ventas.
- Permitir auditoría.
- Ser reutilizable en todos los módulos.

---

# Objetivo del módulo

Administrar correctamente los productos para garantizar un inventario confiable, facilitar las ventas y mejorar la toma de decisiones del propietario.