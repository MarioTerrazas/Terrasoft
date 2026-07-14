# Requisitos Funcionales de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2 — Arquitectura de FerreSys

---

# Objetivo

Definir las funciones que FerreSys deberá realizar.

Cada requisito tendrá un identificador único para facilitar su desarrollo, seguimiento, prueba y mantenimiento.

---

# Convención

Los requisitos funcionales utilizarán el formato:

`RF-XXX`

Ejemplo:

`RF-001 — Iniciar sesión`

---

# 1. Empresas y configuración

## RF-001 — Registrar la ferretería

El sistema deberá permitir registrar:

- Nombre comercial.
- Razón social.
- NIT.
- Dirección.
- Teléfono.
- Correo electrónico.
- Logo opcional.
- Moneda principal.
- Datos de facturación.

## RF-002 — Configurar sucursales

El sistema deberá permitir registrar una o varias sucursales.

## RF-003 — Configurar almacenes

El sistema deberá permitir asociar uno o varios almacenes a cada sucursal.

## RF-004 — Configurar métodos de pago

El propietario podrá habilitar métodos como:

- Efectivo.
- QR.
- Transferencia.
- Crédito.
- Pago mixto.

## RF-005 — Configurar unidades de medida

El sistema deberá permitir administrar unidades como:

- Unidad.
- Bolsa.
- Caja.
- Paquete.
- Metro.
- Kilogramo.
- Tonelada.
- Litro.
- Metro cúbico.
- Viaje.

---

# 2. Usuarios, roles y seguridad

## RF-006 — Iniciar sesión

El sistema deberá permitir que cada usuario ingrese mediante sus credenciales.

## RF-007 — Cerrar sesión

El usuario deberá poder cerrar su sesión de forma segura.

## RF-008 — Crear usuarios

El propietario o administrador podrá registrar nuevos usuarios.

## RF-009 — Asignar roles

El sistema deberá permitir asignar roles como:

- Propietario.
- Administrador.
- Vendedor.
- Encargado de inventario.
- Chofer.
- Ayudante de carga.
- Contador.
- Administrador técnico.

## RF-010 — Controlar permisos

El sistema deberá limitar las funciones y datos según el rol del usuario.

## RF-011 — Desactivar usuarios

El administrador podrá desactivar usuarios sin eliminar su historial.

## RF-012 — Registrar acciones

Las acciones importantes deberán guardar:

- Usuario.
- Fecha.
- Hora.
- Acción realizada.
- Registro afectado.

---

# 3. Dashboard

## RF-013 — Mostrar resumen general

El Dashboard deberá mostrar:

- Pedidos pendientes.
- Productos con stock bajo.
- Choferes en ruta.
- Ventas del día.
- Ventas del día anterior.
- Facturas pendientes.
- Estado de caja.
- Alertas importantes.

## RF-014 — Mostrar accesos rápidos

El Dashboard deberá permitir acceder directamente a:

- Pedidos.
- Inventario.
- Ventas.
- Clientes.
- Choferes.
- Facturación.
- Caja.
- Reportes.

## RF-015 — Clasificar alertas

Las alertas deberán clasificarse como:

- Críticas.
- Importantes.
- Preventivas.

## RF-016 — Mostrar actividad reciente

El propietario podrá consultar las operaciones recientes del sistema.

## RF-017 — Actualizar indicadores

Los indicadores deberán actualizarse cuando cambien pedidos, inventario, ventas, caja o entregas.

---

# 4. Productos e inventario

## RF-018 — Registrar productos

El sistema deberá permitir registrar:

- Código.
- Nombre.
- Descripción.
- Categoría.
- Marca.
- Unidad.
- Precio de compra.
- Precio de venta.
- Stock inicial.
- Stock mínimo.
- Ubicación.
- Estado.

## RF-019 — Editar productos

Los usuarios autorizados podrán actualizar la información de un producto.

## RF-020 — Desactivar productos

Los productos que ya no se vendan podrán desactivarse sin perder su historial.

## RF-021 — Consultar inventario

El sistema deberá mostrar la existencia actual de cada producto.

## RF-022 — Registrar entradas

El sistema deberá registrar aumentos de inventario provenientes de:

- Compras.
- Devoluciones.
- Ajustes.
- Inventario inicial.

## RF-023 — Registrar salidas

El sistema deberá registrar disminuciones provenientes de:

- Ventas.
- Pérdidas.
- Daños.
- Ajustes.
- Devoluciones a proveedores.

## RF-024 — Generar kardex

El sistema deberá mostrar el historial cronológico de movimientos de cada producto.

## RF-025 — Alertar stock bajo

El sistema deberá generar una alerta cuando un producto alcance o baje de su stock mínimo.

## RF-026 — Realizar inventario físico

Los usuarios autorizados podrán comparar las cantidades físicas con las registradas.

## RF-027 — Registrar ajustes

Toda diferencia de inventario deberá registrar:

- Cantidad anterior.
- Cantidad nueva.
- Motivo.
- Usuario responsable.
- Fecha y hora.

## RF-028 — Manejar diferentes unidades

Un producto podrá comercializarse en diferentes unidades o presentaciones cuando corresponda.

---

# 5. Clientes

## RF-029 — Registrar clientes

El sistema deberá permitir registrar:

- Nombre o razón social.
- Documento o NIT.
- Teléfono.
- Dirección.
- Ubicación.
- Referencias.
- Correo electrónico.
- Tipo de cliente.

## RF-030 — Editar clientes

Los usuarios autorizados podrán actualizar sus datos.

## RF-031 — Consultar historial

El sistema deberá mostrar:

- Compras.
- Pedidos.
- Facturas.
- Pagos.
- Deudas.
- Entregas.

## RF-032 — Registrar varias direcciones

Un cliente podrá tener una o más direcciones de entrega.

## RF-033 — Gestionar crédito

Cuando se habilite la venta a crédito, se podrá registrar:

- Límite de crédito.
- Saldo pendiente.
- Fecha de vencimiento.
- Estado de la deuda.

---

# 6. Pedidos

## RF-034 — Crear pedidos

El sistema deberá permitir crear pedidos con:

- Cliente.
- Productos.
- Cantidades.
- Unidades.
- Precios.
- Descuentos.
- Forma de pago.
- Método de entrega.
- Observaciones.

## RF-035 — Generar número de pedido

Cada pedido tendrá un número único.

## RF-036 — Verificar disponibilidad

Antes de confirmar el pedido, el sistema deberá verificar la disponibilidad de los productos.

## RF-037 — Calcular totales

El sistema calculará:

- Subtotal.
- Descuentos.
- Impuestos.
- Costo de entrega.
- Total final.

## RF-038 — Cambiar estado del pedido

Los estados iniciales serán:

- Pendiente.
- Confirmado.
- En preparación.
- Listo para despacho.
- En ruta.
- Entregado.
- Facturado.
- Cancelado.
- Devuelto.

## RF-039 — Modificar pedidos pendientes

Los pedidos podrán modificarse mientras no estén confirmados o despachados.

## RF-040 — Cancelar pedidos

La cancelación deberá registrar:

- Motivo.
- Usuario.
- Fecha.
- Hora.

## RF-041 — Mostrar línea de tiempo

El sistema deberá mostrar todos los eventos relevantes del pedido.

## RF-042 — Relacionar pedido con venta

Un pedido confirmado podrá generar o asociarse a una venta.

## RF-043 — Relacionar pedido con entrega

Los pedidos a domicilio deberán generar una operación de entrega.

---

# 7. Ventas

## RF-044 — Registrar venta rápida

El vendedor podrá registrar una venta sin entrega cuando el cliente retire en tienda.

## RF-045 — Registrar venta desde pedido

Un pedido confirmado podrá convertirse en venta.

## RF-046 — Descontar inventario

Una venta confirmada deberá generar la salida correspondiente del inventario.

## RF-047 — Registrar forma de pago

Cada venta deberá indicar cómo fue pagada.

## RF-048 — Permitir pago mixto

Una venta podrá dividirse entre varios métodos de pago.

## RF-049 — Aplicar descuentos

Los descuentos deberán respetar los permisos definidos.

## RF-050 — Anular venta

Solo usuarios autorizados podrán anular una venta.

## RF-051 — Registrar devolución

El sistema permitirá registrar devoluciones parciales o totales.

## RF-052 — Generar comprobante interno

El sistema podrá generar un comprobante antes de integrar la facturación oficial.

---

# 8. Caja e ingresos/egresos

## RF-053 — Abrir caja

El responsable deberá registrar el monto inicial de la jornada.

## RF-054 — Registrar ingresos

Las ventas y otros ingresos deberán quedar asociados a la caja correspondiente.

## RF-055 — Registrar egresos

El sistema deberá permitir registrar:

- Gastos.
- Pagos.
- Retiros.
- Compras menores.
- Otros egresos.

## RF-056 — Consultar movimientos

El usuario autorizado podrá consultar todos los movimientos de caja.

## RF-057 — Cerrar caja

El cierre deberá comparar:

- Saldo esperado.
- Saldo contado.
- Diferencia.
- Observaciones.

## RF-058 — Registrar diferencias

Las diferencias deberán conservar responsable, motivo, fecha y hora.

---

# 9. Proveedores y compras

## RF-059 — Registrar proveedores

El sistema deberá guardar sus datos comerciales y de contacto.

## RF-060 — Crear orden de compra

El usuario autorizado podrá registrar productos, cantidades y precios solicitados.

## RF-061 — Recibir mercadería

La recepción deberá permitir comparar lo pedido con lo recibido.

## RF-062 — Actualizar inventario por compra

La recepción confirmada deberá aumentar las existencias.

## RF-063 — Registrar cuentas por pagar

El sistema permitirá registrar compras pendientes de pago.

## RF-064 — Consultar historial del proveedor

Se podrán revisar compras, pagos, productos y saldos.

---

# 10. Choferes y vehículos

## RF-065 — Registrar choferes

El sistema deberá almacenar sus datos personales, teléfono y estado.

## RF-066 — Registrar vehículos

Cada vehículo podrá registrar:

- Tipo.
- Placa.
- Capacidad.
- Estado.
- Observaciones.

## RF-067 — Asignar vehículo

Se podrá asociar un vehículo a un chofer o entrega.

## RF-068 — Consultar disponibilidad

El sistema deberá indicar si un chofer o vehículo está:

- Disponible.
- En ruta.
- Fuera de servicio.
- En mantenimiento.

## RF-069 — Consultar historial

Se podrá revisar el historial de entregas por chofer y vehículo.

---

# 11. Entregas

## RF-070 — Crear entrega

Los pedidos a domicilio deberán generar una entrega.

## RF-071 — Asignar chofer y vehículo

Un usuario autorizado podrá realizar la asignación.

## RF-072 — Mostrar dirección

El chofer deberá poder consultar la dirección y referencia del cliente.

## RF-073 — Abrir ubicación en mapa

El sistema deberá permitir abrir la ubicación en una aplicación de navegación.

## RF-074 — Confirmar salida

El chofer registrará el momento en que inicia la entrega.

## RF-075 — Cambiar estado de entrega

Los estados serán:

- Pendiente.
- Asignada.
- Cargando.
- En ruta.
- En destino.
- Entregada.
- No entregada.
- Cancelada.

## RF-076 — Confirmar recepción

El chofer podrá registrar:

- Nombre de quien recibe.
- Fecha.
- Hora.
- Observaciones.

## RF-077 — Adjuntar evidencia

En una fase posterior podrá adjuntarse fotografía, firma o código de confirmación.

## RF-078 — Consultar estado

El propietario podrá ver el estado sin llamar al chofer.

## RF-079 — Registrar ubicación

El seguimiento en tiempo real será evaluado en una fase posterior.

---

# 12. Facturación

## RF-080 — Generar factura desde venta

Una factura deberá originarse desde una venta confirmada.

## RF-081 — Registrar datos fiscales

El sistema deberá utilizar los datos fiscales del emisor y del cliente.

## RF-082 — Registrar estado de factura

Los estados podrán incluir:

- Pendiente.
- Generada.
- Enviada.
- Validada.
- Observada.
- Rechazada.
- Anulada.

## RF-083 — Guardar respuesta tributaria

El sistema deberá conservar códigos, mensajes y resultados recibidos.

## RF-084 — Reintentar envíos

Cuando exista una falla permitida, el sistema podrá reintentar el envío.

## RF-085 — Anular factura

La anulación se realizará únicamente bajo las condiciones autorizadas.

## RF-086 — Generar representación gráfica

El sistema podrá generar la representación visual de la factura válida.

## RF-087 — Cumplir normativa vigente

La integración deberá adaptarse a la modalidad habilitada para la empresa y a los requisitos vigentes del SIN.

---

# 13. Reportes

## RF-088 — Reportar ventas

El sistema deberá generar reportes por:

- Día.
- Semana.
- Mes.
- Usuario.
- Cliente.
- Producto.
- Método de pago.

## RF-089 — Reportar inventario

Deberá mostrar:

- Stock actual.
- Stock bajo.
- Productos sin movimiento.
- Entradas.
- Salidas.
- Ajustes.

## RF-090 — Reportar caja

Deberá mostrar ingresos, egresos, diferencias y cierres.

## RF-091 — Reportar pedidos

Deberá mostrar pedidos por estado, fecha, cliente y vendedor.

## RF-092 — Reportar entregas

Deberá mostrar tiempos, estados, choferes y pedidos no entregados.

## RF-093 — Exportar reportes

Los reportes podrán exportarse en formatos definidos posteriormente.

---

# 14. Auditoría y notificaciones

## RF-094 — Registrar auditoría

Las operaciones críticas deberán generar un registro de auditoría.

## RF-095 — Consultar auditoría

Solo usuarios autorizados podrán consultar el historial.

## RF-096 — Generar alertas

El sistema deberá alertar sobre:

- Stock bajo.
- Pedidos atrasados.
- Entregas demoradas.
- Diferencias de caja.
- Facturas con error.
- Deudas vencidas.

## RF-097 — Mostrar notificaciones

Las notificaciones aparecerán en el Dashboard y en el módulo correspondiente.

## RF-098 — Marcar notificaciones como atendidas

Los usuarios autorizados podrán cerrar o marcar una alerta como resuelta.

---

# 15. TerrasoftAI — Funciones futuras

## RF-099 — Consultar información mediante lenguaje natural

El propietario podrá realizar preguntas sobre el negocio.

## RF-100 — Detectar situaciones relevantes

TerrasoftAI podrá identificar:

- Stock crítico.
- Caída de ventas.
- Productos sin movimiento.
- Entregas demoradas.
- Diferencias inusuales.

## RF-101 — Generar recomendaciones

TerrasoftAI podrá sugerir acciones, pero no ejecutará operaciones críticas sin autorización humana.

---

# Criterios generales

Todo requisito funcional deberá:

- Resolver una necesidad real.
- Tener permisos definidos.
- Generar trazabilidad cuando corresponda.
- Ser verificable mediante pruebas.
- Funcionar en computadora y teléfono cuando corresponda.
- Mantener consistencia con los demás módulos.

---

# Priorización inicial

Los requisitos se clasificarán posteriormente como:

- MVP.
- Segunda fase.
- Futuro.

Esta clasificación se realizará después de validar las prioridades reales con Marito.