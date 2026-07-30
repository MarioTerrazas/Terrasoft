# ROADMAP

Versión: 1.1

Estado: Activo

Última actualización: 2026-07-30

---

# Sprint 0 - Fundación ✅

Objetivo:

Preparar el entorno profesional de desarrollo.

Logros:

- [x] Instalar Git.
- [x] Instalar Python.
- [x] Instalar Node.js.
- [x] Configurar VS Code.
- [x] Crear repositorio Git.
- [x] Realizar el primer commit.
- [x] Publicar el proyecto en GitHub.

Estado:

Completado.

---

# Sprint 1 - Nacimiento de TerrasoftAI ✅

Objetivo:

Construir la base del ecosistema Terrasoft y crear un empleado IA local que acompañe el desarrollo.

Logros:

- [x] Diseñar la arquitectura general del proyecto.
- [x] Crear la documentación oficial.
- [x] Diseñar la estructura Knowledge.
- [x] Crear la Wiki.
- [x] Crear Onboarding.
- [x] Instalar Ollama.
- [x] Descargar Qwen 2.5 7B.
- [x] Realizar la primera conversación con TerrasoftAI.
- [x] Definir FerreSys como primer producto.
- [x] Crear memoria operativa de FerreSys.
- [x] Crear diario técnico para TerrasoftAI.
- [x] Definir reglas para que TerrasoftAI revise el DER, migraciones, reglas y diario antes de proponer código.

Estado:

Completado.

---

# Sprint 2 - Arquitectura y Base de Datos de FerreSys ✅

Objetivo:

Diseñar FerreSys antes del desarrollo y construir su base de datos inicial en PostgreSQL.

Logros:

- [x] Definir el producto.
- [x] Definir la arquitectura funcional.
- [x] Definir los módulos del sistema.
- [x] Documentar los casos de uso.
- [x] Definir el modelo de negocio.
- [x] Documentar requisitos funcionales.
- [x] Documentar requisitos no funcionales.
- [x] Diseñar la propuesta UI/UX.
- [x] Diseñar la arquitectura API REST.
- [x] Diseñar la arquitectura de base de datos.
- [x] Crear el diccionario de datos.
- [x] Crear el modelo lógico.
- [x] Completar el DER versión 1.
- [x] Diseñar el modelo físico PostgreSQL.
- [x] Crear la base de datos `ferresys`.
- [x] Crear las tablas principales.
- [x] Crear claves primarias y foráneas.
- [x] Crear restricciones e índices.
- [x] Cargar roles iniciales.
- [x] Cargar tipos de movimiento de inventario.
- [x] Configurar codificación UTF-8.
- [x] Crear migración para vincular pedidos con almacenes.

Tablas principales:

- rol;
- usuario;
- cliente;
- producto;
- almacen;
- pedido;
- detalle_pedido;
- inventario;
- tipo_movimiento;
- movimiento_inventario.

Estado:

Completado.

---

# Sprint 3 - Backend con FastAPI 🚧

Objetivo:

Construir la API principal de FerreSys con autenticación, seguridad, operaciones comerciales e inventario.

## Infraestructura Backend

- [x] Crear entorno virtual.
- [x] Instalar FastAPI.
- [x] Instalar SQLAlchemy.
- [x] Instalar psycopg.
- [x] Configurar PostgreSQL.
- [x] Configurar variables de entorno.
- [x] Proteger `.env` y `.venv` mediante `.gitignore`.
- [x] Crear endpoint raíz.
- [x] Crear endpoint de salud.
- [x] Crear verificación de conexión a la base de datos.
- [x] Configurar Swagger.

## Autenticación y Seguridad

- [x] Implementar login.
- [x] Implementar JWT.
- [x] Implementar autenticación Bearer.
- [x] Implementar hash de contraseñas con Argon2.
- [x] Crear endpoint `/auth/me`.
- [x] Implementar permisos por rol.
- [x] Proteger rutas.
- [x] Verificar respuestas `401 Unauthorized`.
- [x] Verificar respuestas `403 Forbidden`.
- [x] Evitar que el cliente envíe manualmente el usuario responsable de operaciones críticas.

## Gestión de Usuarios

- [x] Crear usuarios.
- [x] Listar usuarios.
- [x] Consultar usuarios.
- [x] Actualizar usuarios.
- [x] Cambiar contraseña.
- [x] Desactivar usuarios.
- [x] Listar roles.
- [x] Proteger la gestión de usuarios para el rol ADMINISTRADOR.
- [x] Crear y probar un usuario VENDEDOR.

## Clientes

- [x] Crear clientes.
- [x] Listar clientes.
- [x] Buscar clientes.
- [x] Consultar clientes.
- [x] Actualizar clientes.
- [x] Desactivar clientes.

## Productos

- [x] Crear productos.
- [x] Listar productos.
- [x] Buscar productos.
- [x] Consultar productos.
- [x] Actualizar productos.
- [x] Desactivar productos.
- [x] Validar código único.
- [x] Validar precios.

## Almacenes

- [x] Crear almacenes.
- [x] Listar almacenes.
- [x] Consultar almacenes.
- [x] Actualizar almacenes.
- [x] Desactivar almacenes.

## Inventario

- [x] Crear inventario por producto y almacén.
- [x] Consultar inventario.
- [x] Listar inventarios.
- [x] Calcular stock disponible.
- [x] Calcular indicador de bajo stock.
- [x] Manejar stock actual.
- [x] Manejar stock reservado.
- [x] Evitar salidas superiores al stock disponible.

## Movimientos de Inventario

- [x] Registrar entradas.
- [x] Registrar salidas.
- [x] Mantener historial de movimientos.
- [x] Obtener el usuario responsable desde el JWT.
- [x] Validar la naturaleza del movimiento.
- [x] Usar transacciones.
- [x] Usar bloqueo de fila para operaciones críticas.

## Pedidos

- [x] Crear pedidos.
- [x] Listar pedidos.
- [x] Consultar pedidos.
- [x] Relacionar pedido con cliente.
- [x] Relacionar pedido con almacén.
- [x] Crear detalles de pedido.
- [x] Obtener precios desde la base de datos.
- [x] Calcular subtotales.
- [x] Calcular descuentos.
- [x] Calcular total.
- [x] Impedir productos repetidos.
- [x] Validar descuentos.
- [x] Generar número único de pedido.

## Estados e Inventario de Pedidos

- [x] Implementar estado PENDIENTE.
- [x] Implementar estado CONFIRMADO.
- [x] Implementar estado PREPARANDO.
- [x] Implementar estado CANCELADO.
- [x] Implementar estado ENTREGADO.
- [x] Reservar stock al confirmar.
- [x] Mantener la reserva durante preparación.
- [x] Liberar reserva al cancelar.
- [x] Descontar stock al entregar.
- [x] Crear movimiento automático `SALIDA_VENTA`.
- [x] Cerrar pedidos entregados o cancelados.
- [x] Validar transiciones de estado.
- [x] Probar el flujo completo de integración.

## Pendientes del Sprint 3

- [ ] Crear pruebas automatizadas.
- [ ] Configurar base de datos independiente para pruebas.
- [ ] Probar login correcto e incorrecto.
- [ ] Probar permisos por rol.
- [ ] Probar reserva de stock.
- [ ] Probar cancelación y liberación de reserva.
- [ ] Probar entrega y salida automática.
- [ ] Probar intento de venta sin stock.
- [ ] Probar transiciones inválidas.
- [ ] Integrar Alembic para futuras migraciones.
- [ ] Mejorar manejo global de errores.
- [ ] Agregar paginación uniforme.
- [ ] Agregar filtros avanzados.
- [ ] Crear documentación técnica de endpoints.

Estado:

Muy avanzado.

---

# Sprint 4 - Logística, Entregas y Auditoría

Objetivo:

Construir el proceso operativo que ocurre después de la venta.

## Auditoría

- [ ] Diseñar tabla de auditoría.
- [ ] Registrar usuario responsable.
- [ ] Registrar acción realizada.
- [ ] Registrar fecha y hora.
- [ ] Registrar entidad afectada.
- [ ] Registrar valores anteriores y nuevos.
- [ ] Crear consultas de auditoría.

## Entregas

- [ ] Diseñar módulo de entregas.
- [ ] Relacionar entrega con pedido.
- [ ] Definir dirección de entrega.
- [ ] Guardar ubicación GPS.
- [ ] Definir fecha programada.
- [ ] Definir costo de entrega.
- [ ] Definir estado de entrega.
- [ ] Registrar evidencia de entrega.
- [ ] Registrar recepción del cliente.

## Choferes

- [ ] Diseñar perfil de chofer.
- [ ] Relacionar chofer con usuario.
- [ ] Asignar pedidos.
- [ ] Consultar pedidos asignados.
- [ ] Aceptar entrega.
- [ ] Iniciar recorrido.
- [ ] Confirmar llegada.
- [ ] Confirmar entrega.
- [ ] Reportar incidentes.

## Vehículos

- [ ] Diseñar módulo de vehículos.
- [ ] Registrar placa.
- [ ] Registrar tipo de vehículo.
- [ ] Registrar capacidad.
- [ ] Registrar estado.
- [ ] Asignar vehículo a una entrega.
- [ ] Controlar disponibilidad.
- [ ] Registrar mantenimiento básico.

## Seguimiento

- [ ] Crear estados logísticos.
- [ ] Guardar ubicación del chofer.
- [ ] Calcular tiempo estimado.
- [ ] Compartir seguimiento con cliente.
- [ ] Preparar integración con WhatsApp.

Estado:

Pendiente.

---

# Sprint 5 - Proveedores, Compras, Pagos y Facturación

Objetivo:

Completar el ciclo administrativo y comercial de FerreSys.

## Proveedores

- [ ] Crear proveedores.
- [ ] Listar proveedores.
- [ ] Actualizar proveedores.
- [ ] Desactivar proveedores.
- [ ] Registrar contactos.
- [ ] Registrar condiciones de compra.

## Compras

- [ ] Crear órdenes de compra.
- [ ] Crear detalle de compra.
- [ ] Recibir mercadería.
- [ ] Actualizar inventario.
- [ ] Generar movimiento `ENTRADA_COMPRA`.
- [ ] Registrar costo de adquisición.
- [ ] Gestionar compras pendientes y recibidas.

## Pagos

- [ ] Registrar pagos de clientes.
- [ ] Registrar pagos parciales.
- [ ] Registrar efectivo.
- [ ] Registrar transferencia.
- [ ] Registrar QR.
- [ ] Calcular saldo pendiente.
- [ ] Generar comprobantes.
- [ ] Preparar conciliación.

## Facturación

- [ ] Diseñar módulo de facturación.
- [ ] Registrar NIT o CI.
- [ ] Registrar razón social.
- [ ] Generar número de factura.
- [ ] Relacionar factura con pedido.
- [ ] Preparar integración con facturación en Bolivia.
- [ ] Generar comprobante PDF.
- [ ] Preparar reportes tributarios.

Estado:

Pendiente.

---

# Sprint 6 - Frontend con React

Objetivo:

Crear las interfaces de usuario para administrar FerreSys.

## Base del Frontend

- [ ] Crear proyecto React.
- [ ] Configurar Vite.
- [ ] Configurar rutas.
- [ ] Configurar cliente HTTP.
- [ ] Configurar variables de entorno.
- [ ] Crear diseño responsivo.
- [ ] Crear sistema de componentes.

## Seguridad

- [ ] Crear pantalla de login.
- [ ] Guardar sesión de forma segura.
- [ ] Proteger rutas.
- [ ] Mostrar opciones según el rol.
- [ ] Implementar cierre de sesión.

## Panel Administrativo

- [ ] Crear dashboard.
- [ ] Mostrar ventas.
- [ ] Mostrar pedidos.
- [ ] Mostrar inventario.
- [ ] Mostrar alertas de bajo stock.
- [ ] Mostrar entregas pendientes.

## Módulos

- [ ] Interfaz de clientes.
- [ ] Interfaz de productos.
- [ ] Interfaz de almacenes.
- [ ] Interfaz de inventarios.
- [ ] Interfaz de movimientos.
- [ ] Interfaz de pedidos.
- [ ] Interfaz de usuarios.
- [ ] Interfaz de entregas.
- [ ] Interfaz de compras.
- [ ] Interfaz de pagos.

## Aplicación del Chofer

- [ ] Ver pedidos asignados.
- [ ] Ver ubicación del cliente.
- [ ] Cambiar estado de entrega.
- [ ] Abrir navegación.
- [ ] Subir evidencia.
- [ ] Confirmar entrega.

Estado:

Pendiente.

---

# Sprint 7 - Integración y Pruebas

Objetivo:

Validar la calidad, seguridad y estabilidad de todos los módulos.

Logros planificados:

- [ ] Crear pruebas unitarias.
- [ ] Crear pruebas de integración.
- [ ] Crear pruebas end-to-end.
- [ ] Probar concurrencia de inventario.
- [ ] Probar seguridad y permisos.
- [ ] Probar recuperación ante errores.
- [ ] Probar rendimiento.
- [ ] Corregir errores.
- [ ] Preparar copias de seguridad.
- [ ] Preparar restauración de base de datos.
- [ ] Crear manual técnico.
- [ ] Crear manual de usuario.
- [ ] Preparar despliegue.

Estado:

Pendiente.

---

# Sprint 8 - Implementación Piloto

Objetivo:

Implementar FerreSys en la ferretería de Marito y validar el sistema en un entorno real.

Actividades:

- [ ] Cargar productos reales.
- [ ] Cargar clientes reales.
- [ ] Cargar inventario inicial.
- [ ] Configurar almacenes.
- [ ] Crear usuarios reales.
- [ ] Capacitar a los usuarios.
- [ ] Registrar pedidos reales.
- [ ] Asignar entregas reales.
- [ ] Medir tiempos de atención.
- [ ] Medir diferencias de inventario.
- [ ] Recopilar observaciones.
- [ ] Corregir problemas encontrados.
- [ ] Validar el modelo de negocio.
- [ ] Preparar una versión comercial.

Estado:

Pendiente.

---

# Visión posterior al piloto

Después de validar FerreSys en una ferretería real, se evaluará:

- marketplace de materiales por zona;
- aplicación para clientes;
- aplicación independiente para conductores;
- pedidos con seguimiento en tiempo real;
- pagos digitales;
- facturación electrónica;
- integración con WhatsApp;
- modelo de suscripción;
- comisión por pedido;
- expansión a otras ferreterías;
- integración con TerrasoftAI;
- análisis inteligente de ventas e inventario.

---

# Regla del Roadmap

Cada sprint debe:

1. tener un objetivo claro;
2. producir una entrega verificable;
3. actualizar el diario;
4. actualizar la memoria de TerrasoftAI;
5. guardarse en Git;
6. publicarse en GitHub;
7. documentar decisiones importantes;
8. no exponer credenciales ni datos privados.
