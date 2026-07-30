# ESTADO ACTUAL DE FERRESYS

Última actualización: 2026-07-30

## Fase actual

Sprint 3 — Backend.

## Estado general

El backend de FerreSys funciona con FastAPI y PostgreSQL.

## Completado

- base de datos PostgreSQL;
- DER v1;
- migraciones iniciales;
- autenticación JWT;
- contraseñas Argon2;
- roles;
- permisos;
- CRUD de usuarios;
- CRUD de clientes;
- CRUD de productos;
- CRUD de almacenes;
- inventario;
- movimientos;
- pedidos;
- detalles de pedido;
- almacén de origen del pedido;
- reservas;
- preparación;
- cancelación;
- entrega;
- salida automática de inventario.

## Migración más reciente

004_pedido_almacen.sql

## Regla crítica

Nunca descontar inventario al crear un pedido.

El descuento se realiza solamente al entregar.

## Próxima tarea recomendada

Crear pruebas automatizadas para:

1. login correcto e incorrecto;
2. permisos por rol;
3. creación de pedidos;
4. reserva de stock;
5. cancelación y liberación;
6. entrega y movimiento automático;
7. intento de venta sin stock;
8. transiciones de estado inválidas.

## Contexto de seguridad

Nunca escribir ni registrar:

- contraseñas reales;
- JWT_SECRET_KEY;
- tokens;
- contenido del .env;
- credenciales de PostgreSQL.
