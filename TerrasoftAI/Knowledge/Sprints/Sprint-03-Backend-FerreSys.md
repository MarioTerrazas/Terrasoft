# Sprint 3 — Backend de FerreSys

**Estado:** Muy avanzado

**Fecha de actualización:** 2026-07-30

---

## Objetivo

Construir el backend funcional de FerreSys mediante FastAPI y PostgreSQL.

---

## Tecnologías utilizadas

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

## Funcionalidades completadas

### Infraestructura

- backend FastAPI;
- conexión con PostgreSQL;
- variables de entorno;
- endpoints de salud;
- documentación Swagger;
- protección de `.env` y `.venv`.

### Autenticación

- login con JWT;
- Bearer Token;
- endpoint `/auth/me`;
- contraseñas con Argon2;
- control de acceso por roles.

### Roles

- ADMINISTRADOR;
- VENDEDOR;
- ALMACENERO;
- CHOFER.

### Usuarios

- crear;
- listar;
- consultar;
- actualizar;
- cambiar contraseña;
- desactivar;
- listar roles.

### Clientes

- crear;
- listar;
- buscar;
- consultar;
- actualizar;
- desactivar.

### Productos

- crear;
- listar;
- buscar;
- consultar;
- actualizar;
- desactivar;
- validar códigos y precios.

### Almacenes

- crear;
- listar;
- consultar;
- actualizar;
- desactivar.

### Inventarios

- relacionar producto y almacén;
- stock actual;
- stock reservado;
- stock disponible;
- stock mínimo;
- indicador de bajo stock.

### Movimientos

- entradas;
- salidas;
- historial;
- usuario responsable desde JWT;
- bloqueo de filas;
- validación de existencias.

### Pedidos

- crear pedidos;
- consultar pedidos;
- listar pedidos;
- detalles de pedido;
- precios obtenidos desde la base de datos;
- cálculo de subtotal;
- descuentos;
- cálculo de total;
- número de pedido automático;
- almacén de origen.

---

## Flujo de estados

### PENDIENTE

No modifica inventario.

### CONFIRMADO

Valida y reserva existencias.

### PREPARANDO

Mantiene la reserva.

### CANCELADO

Libera la reserva cuando corresponde y cierra el pedido.

### ENTREGADO

Descuenta el stock actual, libera la reserva, genera `SALIDA_VENTA` y cierra el pedido.

---

## Prueba de integración

Pedido:

`PED-20260729-202109-357881`

Producto:

`CEM-001 — Cemento IP-30 50 kg`

Cantidad:

`2`

Resultado:

- pedido creado;
- reserva confirmada;
- preparación confirmada;
- entrega confirmada;
- stock descontado;
- reserva liberada;
- movimiento `SALIDA_VENTA` creado;
- usuario administrador registrado;
- historial preservado.

---

## Migración agregada

`004_pedido_almacen.sql`

La migración agregó:

- columna `id_almacen` en pedido;
- clave foránea hacia almacén;
- índice para búsquedas por almacén.

---

## Reglas aprendidas

1. No descontar stock al crear el pedido.
2. Reservar stock cuando el pedido se confirma.
3. Liberar la reserva al cancelar.
4. Descontar stock al entregar.
5. Registrar todo cambio real como movimiento.
6. Obtener el usuario desde el JWT.
7. Obtener precios desde PostgreSQL.
8. Usar transacciones.
9. Bloquear inventario en operaciones críticas.
10. No reabrir pedidos entregados o cancelados.

---

## Pendientes

- pruebas automatizadas;
- base de datos de pruebas;
- Alembic;
- auditoría;
- manejo global de errores;
- documentación detallada de respuestas;
- logística y entregas;
- choferes;
- vehículos.

---

## Próxima tarea

Crear pruebas automatizadas para seguridad, permisos, inventario y pedidos.