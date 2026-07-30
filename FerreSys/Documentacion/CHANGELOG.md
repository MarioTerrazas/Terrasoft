# CHANGELOG

Todos los cambios importantes de FerreSys serán registrados en este documento.

---

# v0.3.0

Fecha: 2026-07-30

## Sprint 3 — Backend, seguridad, pedidos e inventario

### Agregado

- Backend desarrollado con FastAPI.
- Conexión con PostgreSQL mediante SQLAlchemy y psycopg.
- Configuración mediante variables de entorno.
- Endpoints de salud del sistema y de la base de datos.
- Documentación automática mediante Swagger.
- Autenticación mediante JWT.
- Contraseñas protegidas con Argon2.
- Control de acceso mediante roles.
- Gestión de usuarios y roles.
- CRUD de clientes.
- CRUD de productos.
- CRUD de almacenes.
- Gestión de inventarios.
- Gestión de movimientos de inventario.
- Registro del usuario responsable desde el JWT.
- Creación y consulta de pedidos.
- Detalles de pedido.
- Cálculo automático de subtotales, descuentos y totales.
- Generación automática del número de pedido.
- Relación entre pedido y almacén.
- Reserva de inventario al confirmar pedidos.
- Conservación de reserva durante preparación.
- Liberación de reserva al cancelar.
- Descuento de inventario al entregar.
- Creación automática de movimiento `SALIDA_VENTA`.
- Validación de transiciones de estado.
- Bloqueo de filas en operaciones críticas.
- Migración `004_pedido_almacen.sql`.
- Memoria operativa de FerreSys para TerrasoftAI.
- Diario técnico actualizado.
- Roadmap versión 1.1.

### Estados de pedido implementados

- PENDIENTE.
- CONFIRMADO.
- PREPARANDO.
- CANCELADO.
- ENTREGADO.

### Pruebas manuales completadas

- Login de administrador.
- Login de vendedor.
- Consulta del usuario autenticado.
- Restricciones por rol.
- Respuesta `403` para operaciones no autorizadas.
- Creación de clientes.
- Creación de productos.
- Registro de inventario.
- Registro de entradas.
- Creación de pedidos.
- Reserva de stock.
- Preparación de pedidos.
- Entrega de pedidos.
- Descuento automático de stock.
- Generación automática de `SALIDA_VENTA`.
- Conservación del historial.

### Prueba de integración confirmada

Pedido:

`PED-20260729-202109-357881`

Producto:

`CEM-001 — Cemento IP-30 50 kg`

Cantidad:

`2`

Resultado:

- reserva exitosa;
- preparación exitosa;
- entrega exitosa;
- salida automática registrada;
- usuario administrador asociado;
- historial preservado.

### Pendiente

- Pruebas automatizadas.
- Base de datos independiente para pruebas.
- Alembic.
- Auditoría.
- Entregas.
- Choferes.
- Vehículos.
- Proveedores.
- Compras.
- Pagos.
- Facturación.
- Frontend React.

---

# v0.2.0

Fecha: 2026-07

## Sprint 2 — Arquitectura y base de datos

### Agregado

- Definición del producto.
- Arquitectura funcional.
- Modelo de negocio.
- Módulos del sistema.
- Casos de uso.
- Requisitos funcionales.
- Requisitos no funcionales.
- Diseño UI/UX.
- Arquitectura API REST.
- Arquitectura de base de datos.
- Diccionario de datos.
- Modelo lógico.
- DER versión 1.
- Modelo físico PostgreSQL.
- Base de datos `ferresys`.
- Diez tablas principales.
- Claves primarias y foráneas.
- Restricciones.
- Índices.
- Roles iniciales.
- Tipos de movimiento de inventario.
- Codificación UTF-8.
- Migraciones iniciales.
- Datos semilla.

### Estado

Completado.

---

# v0.1.0

## Sprint 0 y Sprint 1 — Fundación de Terrasoft

### Agregado

- Instalación de Git.
- Instalación de Python.
- Instalación de Node.js.
- Configuración de VS Code.
- Creación del repositorio.
- Publicación en GitHub.
- Creación de la estructura Terrasoft.
- Creación de TerrasoftAI.
- Documentación oficial.
- Knowledge.
- Wiki.
- Onboarding.
- Instalación de Ollama.
- Instalación de Qwen 2.5 7B.
- Primera conversación con TerrasoftAI.
- Definición de FerreSys como primer producto.

### Estado

Completado.