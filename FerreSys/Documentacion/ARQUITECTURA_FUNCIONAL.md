# Arquitectura Funcional de FerreSys

Versión: 1.0

Estado: En diseño

Proyecto: FerreSys

---

# Objetivo

Definir el comportamiento funcional de FerreSys antes del desarrollo del software.

Este documento describe cómo funcionará el sistema desde el punto de vista del negocio.

No contiene detalles técnicos de programación.

---

# Dashboard del Administrador

## Objetivo

Permitir que el propietario conozca el estado general de la ferretería desde una sola pantalla.

## Componentes principales

### Encabezado

- Logo de la empresa (opcional).
- Nombre de la empresa.
- Usuario conectado.
- Fecha y hora.
- Notificaciones.
- Perfil.

---

### Indicadores principales

El Dashboard mostrará:

- Pedidos pendientes.
- Productos con stock bajo.
- Choferes en ruta.
- Ventas del día anterior.
- Facturas pendientes.
- Dinero disponible en caja.
- Alertas importantes.

Cada indicador permitirá acceder directamente al módulo correspondiente.

---

### Menú principal

El sistema dispondrá de accesos rápidos hacia:

- Pedidos
- Inventario
- Choferes
- Ventas
- Facturación
- Caja
- Clientes
- Reportes

---

### Alertas

Las alertas tendrán tres niveles:

🔴 Crítica

🟠 Importante

🟡 Preventiva

Las alertas críticas deberán mostrarse siempre en la pantalla principal.

---

## Objetivo del Dashboard

El propietario deberá comprender el estado general de su negocio en menos de 30 segundos.

Este principio guiará el diseño de toda la interfaz principal de FerreSys.