BEGIN;

-- =========================================================
-- FERRESYS
-- Seed 001: catálogos iniciales
-- Basado en DER v1
-- Fecha: 2026-07-29
-- =========================================================

-- =========================
-- ROLES
-- =========================

INSERT INTO rol (
    nombre,
    descripcion,
    estado
)
VALUES
    (
        'ADMINISTRADOR',
        'Acceso completo a todos los módulos y configuraciones de FerreSys',
        TRUE
    ),
    (
        'VENDEDOR',
        'Gestiona clientes, productos y pedidos',
        TRUE
    ),
    (
        'ALMACENERO',
        'Gestiona inventario, entradas, salidas y ajustes de existencias',
        TRUE
    ),
    (
        'CHOFER',
        'Consulta pedidos y entregas asignadas',
        TRUE
    )
ON CONFLICT (nombre) DO NOTHING;

-- =========================
-- TIPOS DE MOVIMIENTO
-- =========================

INSERT INTO tipo_movimiento (
    nombre,
    descripcion,
    estado
)
VALUES
    (
        'ENTRADA_COMPRA',
        'Ingreso de productos al inventario mediante una compra',
        TRUE
    ),
    (
        'SALIDA_VENTA',
        'Salida de productos del inventario mediante una venta o pedido',
        TRUE
    ),
    (
        'ENTRADA_DEVOLUCION',
        'Ingreso de productos devueltos por un cliente',
        TRUE
    ),
    (
        'SALIDA_DEVOLUCION_PROVEEDOR',
        'Salida de productos devueltos a un proveedor',
        TRUE
    ),
    (
        'AJUSTE_ENTRADA',
        'Aumento manual de existencias por regularización',
        TRUE
    ),
    (
        'AJUSTE_SALIDA',
        'Disminución manual de existencias por regularización',
        TRUE
    ),
    (
        'TRASLADO_ENTRADA',
        'Ingreso de productos trasladados desde otro almacén',
        TRUE
    ),
    (
        'TRASLADO_SALIDA',
        'Salida de productos trasladados hacia otro almacén',
        TRUE
    ),
    (
        'MERMA',
        'Salida por pérdida, daño, vencimiento o deterioro',
        TRUE
    ),
    (
        'INVENTARIO_INICIAL',
        'Registro inicial de existencias de un producto',
        TRUE
    )
ON CONFLICT (nombre) DO NOTHING;

COMMIT;
