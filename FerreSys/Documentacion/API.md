# API REST de FerreSys

**Versión:** 1.0

**Estado:** En diseño

**Proyecto:** FerreSys

**Sprint:** Sprint 2

---

# Objetivo

Definir la arquitectura de la API REST que utilizará FerreSys.

La API será desarrollada con FastAPI y permitirá la comunicación entre el Frontend, la Base de Datos y futuras integraciones.

---

# Arquitectura

Cliente (React)

↓

FastAPI

↓

Servicios

↓

PostgreSQL

---

# Formato

La API utilizará JSON.

Ejemplo:

{
    "success": true,
    "message": "Producto creado correctamente",
    "data": {}
}

---

# Autenticación

Se utilizará JWT.

Los usuarios iniciarán sesión mediante:

POST /api/auth/login

El servidor devolverá un Token.

---

# Módulos de la API

## Autenticación

POST /api/auth/login

POST /api/auth/logout

GET /api/auth/profile

---

## Productos

GET /api/productos

GET /api/productos/{id}

POST /api/productos

PUT /api/productos/{id}

DELETE /api/productos/{id}

---

## Clientes

GET /api/clientes

GET /api/clientes/{id}

POST /api/clientes

PUT /api/clientes/{id}

DELETE /api/clientes/{id}

---

## Pedidos

GET /api/pedidos

GET /api/pedidos/{id}

POST /api/pedidos

PUT /api/pedidos/{id}

PATCH /api/pedidos/{id}/estado

DELETE /api/pedidos/{id}

---

## Ventas

GET /api/ventas

POST /api/ventas

GET /api/ventas/{id}

---

## Compras

GET /api/compras

POST /api/compras

PUT /api/compras/{id}

---

## Inventario

GET /api/inventario

GET /api/inventario/movimientos

POST /api/inventario/ajuste

---

## Caja

GET /api/caja

POST /api/caja/apertura

POST /api/caja/cierre

POST /api/caja/movimiento

---

## Facturación

GET /api/facturas

POST /api/facturas

GET /api/facturas/{id}

POST /api/facturas/{id}/anular

---

## Choferes

GET /api/choferes

POST /api/choferes

PUT /api/choferes/{id}

---

## Vehículos

GET /api/vehiculos

POST /api/vehiculos

PUT /api/vehiculos/{id}

---

## Entregas

GET /api/entregas

POST /api/entregas

PATCH /api/entregas/{id}/estado

---

## Reportes

GET /api/reportes/ventas

GET /api/reportes/inventario

GET /api/reportes/caja

GET /api/reportes/pedidos

---

# Convenciones

- GET → Consultar
- POST → Crear
- PUT → Actualizar completamente
- PATCH → Actualización parcial
- DELETE → Eliminación lógica

---

# Versionado

Todas las rutas iniciarán con:

/api/v1/

Ejemplo:

/api/v1/productos

---

# Objetivo

Construir una API limpia, segura, escalable y preparada para futuras integraciones.