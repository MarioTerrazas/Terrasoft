# Requisitos No Funcionales de FerreSys

**Versión:** 1.0  
**Estado:** En diseño  
**Proyecto:** FerreSys  
**Sprint:** Sprint 2 — Arquitectura de FerreSys

---

# Objetivo

Definir las características de calidad que deberá cumplir FerreSys para garantizar un sistema seguro, rápido, estable, mantenible y fácil de usar.

Los requisitos no funcionales describen cómo debe comportarse el sistema, independientemente de las funcionalidades que implemente.

---

# RNF-001 — Rendimiento

El sistema deberá responder en menos de **2 segundos** para las operaciones habituales.

Las búsquedas de productos y clientes deberán ejecutarse de forma rápida incluso con miles de registros.

---

# RNF-002 — Disponibilidad

FerreSys deberá estar disponible durante el horario de trabajo de la empresa.

Las tareas de mantenimiento deberán minimizar el tiempo de interrupción.

---

# RNF-003 — Seguridad

El acceso requerirá autenticación.

Cada usuario visualizará únicamente la información autorizada según su rol.

Las contraseñas deberán almacenarse cifradas.

---

# RNF-004 — Auditoría

Toda operación importante deberá registrar:

- Usuario.
- Fecha.
- Hora.
- Acción realizada.
- Información afectada.

---

# RNF-005 — Facilidad de uso

La interfaz deberá ser sencilla e intuitiva.

Una persona con conocimientos básicos de computación deberá poder utilizar el sistema con una capacitación mínima.

---

# RNF-006 — Compatibilidad

FerreSys deberá funcionar correctamente en:

- Computadoras de escritorio.
- Laptops.
- Tablets.
- Teléfonos móviles.

Los navegadores soportados serán inicialmente:

- Google Chrome.
- Microsoft Edge.

---

# RNF-007 — Escalabilidad

La arquitectura deberá permitir incorporar nuevos módulos sin afectar el funcionamiento existente.

---

# RNF-008 — Mantenibilidad

El código deberá estar organizado por módulos y seguir estándares definidos por Terrasoft.

La documentación deberá mantenerse actualizada junto con el desarrollo.

---

# RNF-009 — Integridad de los datos

El sistema deberá evitar información duplicada o inconsistente.

Las operaciones críticas deberán ejecutarse mediante transacciones.

---

# RNF-010 — Copias de seguridad

El sistema deberá permitir realizar respaldos de la base de datos.

En futuras versiones se evaluará la automatización de los respaldos.

---

# RNF-011 — Portabilidad

FerreSys deberá poder desplegarse en:

- Servidores locales.
- Servidores en la nube.

La arquitectura deberá facilitar futuras migraciones.

---

# RNF-012 — Trazabilidad

Cada proceso importante deberá conservar su historial para permitir auditorías y análisis posteriores.

---

# RNF-013 — Experiencia de usuario

El Dashboard deberá permitir al propietario comprender el estado general del negocio en menos de treinta segundos.

---

# RNF-014 — Calidad del software

El desarrollo seguirá principios de:

- Código limpio.
- Modularidad.
- Reutilización.
- Documentación continua.
- Control de versiones mediante Git.

---

# RNF-015 — Integración futura

La arquitectura deberá permitir integrar posteriormente:

- TerrasoftAI.
- WhatsApp.
- Facturación electrónica.
- Mapas.
- Aplicación móvil.
- Servicios externos.

Estas integraciones no deberán requerir una reestructuración completa del sistema.

---

# Principios de calidad

FerreSys deberá ser:

- Seguro.
- Confiable.
- Escalable.
- Mantenible.
- Fácil de usar.
- Fácil de aprender.
- Documentado.
- Modular.
- Preparado para crecer.