# API REST de FerreSys

**Versión:** 1.1

**Estado:** En desarrollo — Backend funcional

**Proyecto:** FerreSys

**Sprint:** Sprint 3 — Backend con FastAPI

**Última actualización:** 2026-07-30

---

# Objetivo

Documentar la API REST actual de FerreSys.

La API está desarrollada con FastAPI y permite la comunicación entre:

- clientes web;
- futuras aplicaciones móviles;
- PostgreSQL;
- servicios internos;
- futuras integraciones externas.

---

# Arquitectura actual

Cliente web o aplicación
        ↓
FastAPI
        ↓
Rutas y dependencias
        ↓
SQLAlchemy
        ↓
PostgreSQL

---

# Tecnologías

- Python 3.12;
- FastAPI;
- SQLAlchemy 2;
- Pydantic 2;
- PostgreSQL 17;
- psycopg 3;
- JWT;
- Argon2;
- Swagger/OpenAPI.

---

# Formato de datos

La API utiliza JSON para solicitudes y respuestas.

Ejemplo:

{
  "id_producto": 1,
  "codigo": "CEM-001",
  "nombre": "Cemento IP-30 50 kg",
  "precio_venta": "62.00"
}

Los valores monetarios y cantidades decimales pueden devolverse como texto para conservar precisión.

Ejemplo:

{
  "cantidad": "2.000",
  "total": "124.00"
}

---

# Documentación automática

Swagger:

http://127.0.0.1:8000/docs

OpenAPI:

http://127.0.0.1:8000/openapi.json

---

# Autenticación

FerreSys utiliza JWT mediante autenticación Bearer.

## Iniciar sesión

POST /auth/login

## Consultar usuario autenticado

GET /auth/me

El token debe enviarse en el encabezado:

Authorization: Bearer TOKEN

Las contraseñas se almacenan mediante hash Argon2.

---

# Roles

Roles disponibles:

- ADMINISTRADOR;
- VENDEDOR;
- ALMACENERO;
- CHOFER.

La API devuelve:

- 401 Unauthorized cuando no existe autenticación válida;
- 403 Forbidden cuando el usuario no tiene permisos;
- 404 Not Found cuando el recurso no existe;
- 409 Conflict cuando una operación contradice el estado del sistema;
- 422 Unprocessable Entity cuando los datos enviados no son válidos.

---

# Endpoints generales

## Inicio

GET /

## Salud del backend

GET /health

## Salud de la base de datos

GET /health/database

---

# Autenticación

POST /auth/login
GET /auth/me

---

# Usuarios

Acceso exclusivo para ADMINISTRADOR.

GET    /usuarios/roles
POST   /usuarios
GET    /usuarios
GET    /usuarios/{id_usuario}
PUT    /usuarios/{id_usuario}
PUT    /usuarios/{id_usuario}/password
DELETE /usuarios/{id_usuario}

La eliminación es lógica mediante desactivación.

---

# Clientes

POST   /clientes
GET    /clientes
GET    /clientes/{id_cliente}
PUT    /clientes/{id_cliente}
DELETE /clientes/{id_cliente}

Características:

- búsqueda;
- paginación;
- validación de estado;
- desactivación lógica.

---

# Productos

POST   /productos
GET    /productos
GET    /productos/{id_producto}
PUT    /productos/{id_producto}
DELETE /productos/{id_producto}

Validaciones principales:

- código único;
- precios no negativos;
- precio de venta válido;
- desactivación lógica.

---

# Almacenes

POST   /almacenes
GET    /almacenes
GET    /almacenes/{id_almacen}
PUT    /almacenes/{id_almacen}
DELETE /almacenes/{id_almacen}

---

# Inventarios

POST /inventarios
GET  /inventarios
GET  /inventarios/{id_inventario}
PUT  /inventarios/{id_inventario}

La API calcula:

stock_disponible = stock_actual - stock_reservado

También informa:

- stock actual;
- stock reservado;
- stock mínimo;
- bajo stock.

---

# Movimientos de inventario

POST /movimientos-inventario
GET  /movimientos-inventario
GET  /movimientos-inventario/{id_movimiento}

Características:

- entradas;
- salidas;
- historial permanente;
- usuario responsable obtenido desde JWT;
- validación de stock;
- transacciones;
- bloqueo de filas.

Tipos disponibles:

- ENTRADA_COMPRA;
- SALIDA_VENTA;
- ENTRADA_DEVOLUCION;
- SALIDA_DEVOLUCION_PROVEEDOR;
- AJUSTE_ENTRADA;
- AJUSTE_SALIDA;
- TRASLADO_ENTRADA;
- TRASLADO_SALIDA;
- MERMA;
- INVENTARIO_INICIAL.

---

# Pedidos

POST /pedidos
GET  /pedidos
GET  /pedidos/{id_pedido}
PUT  /pedidos/{id_pedido}/estado

Al crear un pedido, la API:

- valida cliente;
- valida almacén;
- valida productos;
- obtiene precios desde PostgreSQL;
- calcula subtotales;
- calcula descuentos;
- calcula total;
- genera número único;
- impide productos repetidos.

Ejemplo de creación:

{
  "id_cliente": 1,
  "id_almacen": 1,
  "descuento": 0,
  "detalles": [
    {
      "id_producto": 1,
      "cantidad": 2,
      "descuento": 0
    }
  ]
}

---

# Estados de pedido

## PENDIENTE

- no modifica inventario.

## CONFIRMADO

- valida existencias;
- aumenta stock_reservado.

## PREPARANDO

- conserva la reserva.

## CANCELADO

- libera la reserva cuando corresponde;
- queda cerrado.

## ENTREGADO

- reduce stock_actual;
- reduce stock_reservado;
- crea movimiento automático SALIDA_VENTA;
- queda cerrado.

---

# Transiciones permitidas

PENDIENTE
   ├── CONFIRMADO
   │      ├── PREPARANDO
   │      │      ├── ENTREGADO
   │      │      └── CANCELADO
   │      ├── ENTREGADO
   │      └── CANCELADO
   └── CANCELADO

Los pedidos ENTREGADO y CANCELADO no pueden volver a modificarse.

---

# Permisos principales

## ADMINISTRADOR

Acceso completo.

## VENDEDOR

- clientes;
- productos;
- pedidos;
- consulta de almacenes;
- consulta de inventario.

## ALMACENERO

- inventario;
- movimientos;
- consulta de pedidos;
- cambios operativos de estado.

## CHOFER

- consultas necesarias para futuras entregas.

---

# Convenciones

- GET para consultar;
- POST para crear;
- PUT para actualizar;
- DELETE para desactivación lógica cuando corresponda.

Actualmente las rutas no utilizan el prefijo /api/v1.

Una futura versión podrá incorporar versionado explícito sin romper los clientes existentes.

---

# Seguridad

La API debe cumplir estas reglas:

1. no exponer contraseñas;
2. no devolver hashes;
3. no registrar tokens en documentación;
4. obtener el usuario responsable desde JWT;
5. validar permisos por rol;
6. no aceptar precios manipulados desde el cliente;
7. no modificar inventario sin movimiento;
8. usar transacciones en operaciones críticas;
9. usar bloqueo de filas en reservas y entregas;
10. proteger .env mediante .gitignore.

---

# Módulos futuros

Todavía no implementados:

- auditoría;
- entregas;
- choferes;
- vehículos;
- proveedores;
- compras;
- pagos;
- caja;
- facturación;
- reportes avanzados;
- frontend React.

---

# Estado actual

La API base está funcional y fue probada manualmente.

Se completaron pruebas de:

- autenticación;
- permisos por rol;
- usuarios;
- clientes;
- productos;
- almacenes;
- inventarios;
- movimientos;
- pedidos;
- reserva de stock;
- entrega;
- salida automática de inventario.

---

# Próximos pasos

1. crear pruebas automatizadas;
2. configurar base de datos de pruebas;
3. integrar Alembic;
4. implementar auditoría;
5. desarrollar logística y entregas;
6. documentar cada endpoint con ejemplos de respuesta;
7. preparar versionado /api/v1.