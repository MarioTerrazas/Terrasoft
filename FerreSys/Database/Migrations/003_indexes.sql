BEGIN;

-- =========================================================
-- FERRESYS
-- Migración 003: índices
-- Basado en DER v1
-- Fecha: 2026-07-29
-- =========================================================

-- =========================
-- USUARIO
-- =========================

CREATE INDEX idx_usuario_id_rol
    ON usuario (id_rol);

CREATE INDEX idx_usuario_estado
    ON usuario (estado);

CREATE INDEX idx_usuario_nombre
    ON usuario (nombre);

-- =========================
-- CLIENTE
-- =========================

CREATE INDEX idx_cliente_nombre
    ON cliente (nombre);

CREATE INDEX idx_cliente_documento
    ON cliente (documento);

CREATE INDEX idx_cliente_nit
    ON cliente (nit);

CREATE INDEX idx_cliente_telefono
    ON cliente (telefono);

-- =========================
-- PRODUCTO
-- =========================

CREATE INDEX idx_producto_nombre
    ON producto (nombre);

CREATE INDEX idx_producto_estado
    ON producto (estado);

CREATE INDEX idx_producto_stock_minimo
    ON producto (stock_minimo);

-- =========================
-- PEDIDO
-- =========================

CREATE INDEX idx_pedido_id_cliente
    ON pedido (id_cliente);

CREATE INDEX idx_pedido_fecha
    ON pedido (fecha);

CREATE INDEX idx_pedido_estado
    ON pedido (estado);

CREATE INDEX idx_pedido_cliente_fecha
    ON pedido (id_cliente, fecha DESC);

-- =========================
-- DETALLE DE PEDIDO
-- =========================

CREATE INDEX idx_detalle_pedido_id_pedido
    ON detalle_pedido (id_pedido);

CREATE INDEX idx_detalle_pedido_id_producto
    ON detalle_pedido (id_producto);

-- =========================
-- INVENTARIO
-- =========================

CREATE INDEX idx_inventario_id_producto
    ON inventario (id_producto);

CREATE INDEX idx_inventario_id_almacen
    ON inventario (id_almacen);

CREATE INDEX idx_inventario_stock_actual
    ON inventario (stock_actual);

-- =========================
-- MOVIMIENTOS DE INVENTARIO
-- =========================

CREATE INDEX idx_movimiento_id_inventario
    ON movimiento_inventario (id_inventario);

CREATE INDEX idx_movimiento_id_tipo
    ON movimiento_inventario (id_tipo_movimiento);

CREATE INDEX idx_movimiento_id_usuario
    ON movimiento_inventario (id_usuario);

CREATE INDEX idx_movimiento_fecha
    ON movimiento_inventario (fecha_movimiento DESC);

CREATE INDEX idx_movimiento_inventario_fecha
    ON movimiento_inventario (
        id_inventario,
        fecha_movimiento DESC
    );

-- =========================
-- ALMACÉN
-- =========================

CREATE INDEX idx_almacen_estado
    ON almacen (estado);

-- =========================
-- TIPO DE MOVIMIENTO
-- =========================

CREATE INDEX idx_tipo_movimiento_estado
    ON tipo_movimiento (estado);

COMMIT;
