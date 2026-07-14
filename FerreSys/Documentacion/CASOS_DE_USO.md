# Casos de Uso de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2

---

# Objetivo

Definir las acciones que podrá realizar cada tipo de usuario dentro de FerreSys.

Los casos de uso representan la interacción entre las personas y el sistema.

---

# Actores del sistema

- Propietario
- Administrador
- Vendedor
- Encargado de Inventario
- Chofer
- Ayudante de carga
- Contador
- Cliente (futuras versiones)

---

# Propietario

Puede:

- Acceder a todos los módulos.
- Consultar el Dashboard.
- Crear y modificar productos.
- Registrar compras.
- Registrar ventas.
- Aprobar descuentos especiales.
- Administrar caja.
- Consultar reportes.
- Administrar usuarios.
- Configurar el sistema.

---

# Administrador

Puede:

- Administrar usuarios.
- Asignar permisos.
- Configurar parámetros.
- Consultar auditoría.
- Realizar respaldos.
- Supervisar el funcionamiento general.

---

# Vendedor

Puede:

- Buscar clientes.
- Registrar nuevos clientes.
- Crear pedidos.
- Modificar pedidos antes de su confirmación.
- Registrar ventas.
- Consultar inventario disponible.
- Emitir cotizaciones.
- Cobrar ventas.

No puede:

- Eliminar ventas confirmadas.
- Modificar inventario manualmente.
- Acceder a la configuración del sistema.

---

# Encargado de Inventario

Puede:

- Registrar productos.
- Actualizar existencias.
- Registrar entradas.
- Registrar salidas.
- Realizar ajustes.
- Consultar kardex.
- Gestionar almacenes.

No puede:

- Registrar ventas.
- Acceder a caja.
- Emitir facturas.

---

# Chofer

Puede:

- Consultar pedidos asignados.
- Ver direcciones de entrega.
- Confirmar salida.
- Confirmar entrega.
- Registrar observaciones.
- Adjuntar evidencia de entrega (futuro).

No puede:

- Cambiar precios.
- Modificar pedidos.
- Acceder a inventario.

---

# Ayudante de carga

Puede:

- Consultar pedidos preparados.
- Confirmar carga del vehículo.
- Registrar observaciones relacionadas con la carga.

No puede:

- Modificar pedidos.
- Registrar ventas.

---

# Contador

Puede:

- Consultar ventas.
- Consultar compras.
- Revisar caja.
- Acceder a información para declaraciones tributarias.
- Exportar reportes.

No puede:

- Modificar inventario.
- Cambiar pedidos.

---

# Cliente (Futuro)

Podrá:

- Consultar sus pedidos.
- Consultar facturas.
- Consultar historial de compras.
- Descargar comprobantes.
- Consultar estado de entrega.

---

# Principio de seguridad

Cada usuario visualizará únicamente la información necesaria para realizar su trabajo.

El acceso estará controlado mediante roles y permisos.