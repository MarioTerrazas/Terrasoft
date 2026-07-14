# Pedidos

Versión: 1.0

Estado: En diseño

Proyecto: FerreSys

---

# Objetivo

El pedido representa la solicitud realizada por un cliente para adquirir uno o más productos de la ferretería.

Es la entidad principal del sistema y será el punto de partida para los procesos de ventas, inventario, logística y facturación.

---

# Información del Pedido

Cada pedido deberá contener:

## Información general

- Número de pedido.
- Fecha.
- Hora.
- Estado.
- Usuario que registró el pedido.

---

## Cliente

- Nombre.
- Teléfono.
- Dirección.
- Ubicación (opcional).
- Tipo de cliente.

---

## Productos

Cada pedido podrá contener uno o varios productos.

Para cada producto se registrará:

- Producto.
- Cantidad.
- Unidad.
- Precio.
- Descuento.
- Subtotal.

---

## Totales

- Subtotal.
- Descuento.
- Impuestos.
- Total.

---

## Forma de pago

- Efectivo.
- Transferencia.
- QR.
- Crédito.
- Mixto.

---

## Entrega

- Retira en tienda.
- Entrega a domicilio.

Si es entrega:

- Dirección.
- Referencia.
- Chofer asignado.
- Vehículo.
- Hora estimada.

---

## Observaciones

Campo libre para notas importantes.

---

# Estados del Pedido

Un pedido podrá pasar por los siguientes estados:

Pendiente

↓

Confirmado

↓

Preparando

↓

Listo para despacho

↓

En ruta

↓

Entregado

↓

Facturado

```
También podrá pasar a:

Cancelado

o

Devuelto
```

---

# Objetivo

Todo el flujo operativo de FerreSys girará alrededor del Pedido.