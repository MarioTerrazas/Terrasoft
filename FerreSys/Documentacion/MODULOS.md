# Módulos de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2 — Arquitectura de FerreSys

---

# Objetivo

Definir los módulos funcionales que compondrán FerreSys y establecer cómo se relacionan para administrar la operación completa de una ferretería.

FerreSys será modular. Cada módulo deberá resolver un problema real y podrá evolucionar sin afectar innecesariamente a los demás.

---

# Módulo central: Pedidos y Operaciones

Este será el corazón operativo de FerreSys.

Permitirá:

- Registrar pedidos.
- Asociar clientes.
- Agregar productos y cantidades.
- Verificar disponibilidad.
- Calcular importes.
- Definir forma de pago.
- Elegir retiro en tienda o entrega a domicilio.
- Asignar chofer y vehículo.
- Cambiar el estado del pedido.
- Consultar la línea de tiempo.
- Confirmar la entrega.
- Relacionar el pedido con una venta y una factura.

## Estados principales

- Pendiente.
- Confirmado.
- En preparación.
- Listo para despacho.
- En ruta.
- Entregado.
- Facturado.
- Cancelado.
- Devuelto.

---

# Módulo de Dashboard

Permitirá al propietario comprender el estado del negocio en menos de treinta segundos.

Mostrará:

- Pedidos pendientes.
- Productos con stock bajo.
- Choferes en ruta.
- Ventas del día.
- Ventas del día anterior.
- Facturas pendientes.
- Dinero registrado en caja.
- Alertas críticas, importantes y preventivas.
- Actividad reciente.

Cada indicador permitirá acceder al módulo correspondiente.

---

# Módulo de Inventario

Permitirá controlar las existencias de mercadería.

Incluirá:

- Registro de productos.
- Categorías.
- Marcas.
- Unidades de medida.
- Stock actual.
- Stock mínimo.
- Entradas.
- Salidas.
- Ajustes.
- Devoluciones.
- Kardex.
- Historial de movimientos.
- Alertas por stock bajo.
- Inventario físico.

## Unidades previstas

- Unidad.
- Bolsa.
- Caja.
- Paquete.
- Metro.
- Kilo.
- Tonelada.
- Litro.
- Volumen.
- Viaje.

Un producto podrá manejar diferentes presentaciones o unidades cuando el negocio lo requiera.

---

# Módulo de Ventas

Permitirá registrar y controlar las operaciones comerciales.

Incluirá:

- Venta rápida.
- Venta vinculada a pedido.
- Cotización.
- Descuentos autorizados.
- Formas de pago.
- Comprobantes internos.
- Historial de ventas.
- Anulación controlada.
- Devoluciones.
- Relación con inventario, caja y facturación.

Una venta confirmada deberá generar automáticamente la salida correspondiente del inventario.

---

# Módulo de Clientes

Permitirá mantener información organizada de cada cliente.

Incluirá:

- Nombre o razón social.
- Documento de identidad o NIT.
- Teléfono.
- Dirección.
- Ubicación geográfica.
- Referencias de entrega.
- Historial de compras.
- Pedidos realizados.
- Facturas.
- Saldos pendientes.
- Límite de crédito, cuando corresponda.
- Estado del cliente.

---

# Módulo de Compras y Proveedores

Permitirá registrar el abastecimiento de la ferretería.

Incluirá:

- Proveedores.
- Órdenes de compra.
- Productos comprados.
- Precios de compra.
- Recepción de mercadería.
- Facturas del proveedor.
- Cuentas por pagar.
- Historial de compras.
- Actualización automática del inventario.

---

# Módulo de Caja e Ingresos/Egresos

Permitirá controlar los movimientos económicos diarios.

Incluirá:

- Apertura de caja.
- Cierre de caja.
- Ingresos por ventas.
- Ingresos adicionales.
- Egresos.
- Gastos operativos.
- Pagos a proveedores.
- Formas de pago.
- Arqueo.
- Diferencias de caja.
- Historial de movimientos.
- Reportes diarios y mensuales.

No se considerará dinero real disponible únicamente por estar registrado; todos los movimientos deberán contar con trazabilidad.

---

# Módulo de Facturación

Permitirá preparar y gestionar la emisión de facturas conforme a la modalidad autorizada para la empresa.

Incluirá:

- Datos fiscales del emisor.
- Datos fiscales del cliente.
- Factura vinculada a una venta.
- Estado de emisión.
- Envío y validación.
- Representación gráfica.
- Anulación.
- Reintentos.
- Registro de errores.
- Historial de eventos.

La integración oficial con el sistema tributario boliviano se implementará únicamente después de estudiar y documentar los requisitos técnicos vigentes del SIN.

Generar un PDF no será considerado equivalente a emitir una factura válida.

---

# Módulo de Choferes y Vehículos

Permitirá administrar los recursos destinados a las entregas.

## Choferes

- Datos personales.
- Teléfono.
- Estado.
- Horario.
- Vehículo asignado.
- Pedidos activos.
- Historial de entregas.

## Vehículos

- Tipo.
- Placa.
- Capacidad.
- Estado.
- Chofer asignado.
- Mantenimiento.
- Disponibilidad.

---

# Módulo de Entregas y Seguimiento

Permitirá controlar un pedido desde el despacho hasta su recepción.

Incluirá:

- Asignación de chofer.
- Asignación de vehículo.
- Dirección de entrega.
- Ubicación del cliente.
- Hora de salida.
- Tiempo estimado.
- Estados de la entrega.
- Ubicación del chofer, cuando sea técnicamente posible.
- Confirmación de llegada.
- Fotografía o evidencia.
- Nombre de quien recibe.
- Observaciones.
- Confirmación final.

La primera versión podrá apoyarse en enlaces de Google Maps o aplicaciones de navegación. El seguimiento en tiempo real se evaluará posteriormente.

---

# Módulo de Usuarios, Roles y Permisos

Permitirá determinar qué puede ver y hacer cada persona.

Roles iniciales:

- Propietario.
- Administrador.
- Vendedor.
- Encargado de inventario.
- Chofer.
- Ayudante de carga.
- Contador o asesor externo.
- Administrador técnico de Terrasoft.

Cada acción importante deberá registrar:

- Usuario.
- Fecha.
- Hora.
- Acción.
- Información afectada.

---

# Módulo de Reportes

Permitirá transformar los datos del sistema en información útil.

Reportes iniciales:

- Ventas por día, semana y mes.
- Productos más vendidos.
- Productos con stock bajo.
- Movimientos de inventario.
- Ingresos y egresos.
- Estado de caja.
- Pedidos pendientes y entregados.
- Tiempo promedio de entrega.
- Rendimiento de entregas.
- Compras por proveedor.
- Facturas emitidas, pendientes o anuladas.

---

# Módulo de Auditoría y Línea de Tiempo

Permitirá responder:

- ¿Qué ocurrió?
- ¿Quién realizó la acción?
- ¿Cuándo ocurrió?
- ¿Qué cambió?
- ¿Desde qué estado?
- ¿Hacia qué estado?

Los pedidos tendrán una línea de tiempo visible.

Otros procesos importantes también deberán generar eventos de auditoría:

- Inventario.
- Ventas.
- Caja.
- Compras.
- Facturas.
- Usuarios.
- Entregas.

---

# Módulo de Configuración

Permitirá personalizar el sistema para cada ferretería.

Incluirá:

- Nombre comercial.
- Logo.
- Datos fiscales.
- Sucursales.
- Almacenes.
- Moneda.
- Impuestos.
- Unidades de medida.
- Estados configurables.
- Stock mínimo.
- Métodos de pago.
- Parámetros de facturación.
- Preferencias de notificaciones.

---

# Integraciones futuras

FerreSys podrá incorporar progresivamente:

- WhatsApp.
- Mapas y geolocalización.
- Facturación en línea del SIN.
- Pagos mediante QR.
- Tienda o catálogo web.
- Aplicación móvil.
- TerrasoftAI.
- Recomendaciones de reposición.
- Optimización de rutas.
- Notificaciones automáticas.

Estas integraciones no formarán parte automáticamente del MVP. Serán evaluadas según valor, complejidad, costo y validación con el primer cliente.

---

# Prioridad para el MVP

La primera versión deberá concentrarse en:

1. Usuarios y permisos básicos.
2. Productos e inventario.
3. Clientes.
4. Pedidos.
5. Ventas.
6. Caja básica.
7. Choferes y vehículos.
8. Entregas y estados.
9. Dashboard.
10. Auditoría básica.

La integración tributaria oficial se planificará como un bloque especializado después de confirmar la modalidad de facturación y los requisitos del SIN aplicables a Marito.

---

# Relación principal entre módulos

```text
Cliente
   ↓
Pedido
   ↓
Verificación de inventario
   ↓
Confirmación de venta
   ├──→ Movimiento de inventario
   ├──→ Movimiento de caja
   ├──→ Facturación
   └──→ Entrega
             ↓
        Chofer y vehículo
             ↓
       Confirmación final
             ↓
          Reportes