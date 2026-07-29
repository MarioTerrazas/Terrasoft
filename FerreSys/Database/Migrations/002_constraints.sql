BEGIN;

-- =========================================================
-- FERRESYS
-- Migración 002: restricciones y relaciones
-- Basado en DER v1
-- Fecha: 2026-07-29
-- =========================================================

-- =========================
-- CLAVES FORÁNEAS
-- =========================

ALTER TABLE usuario
    ADD CONSTRAINT fk_usuario_rol
    FOREIGN KEY (id_rol)
    REFERENCES rol (id_rol);

ALTER TABLE pedido
    ADD CONSTRAINT fk_pedido_cliente
    FOREIGN KEY (id_cliente)
    REFERENCES cliente (id_cliente);

ALTER TABLE detalle_pedido
    ADD CONSTRAINT fk_detalle_pedido_pedido
    FOREIGN KEY (id_pedido)
    REFERENCES pedido (id_pedido)
    ON DELETE CASCADE;

ALTER TABLE detalle_pedido
    ADD CONSTRAINT fk_detalle_pedido_producto
    FOREIGN KEY (id_producto)
    REFERENCES producto (id_producto);

ALTER TABLE inventario
    ADD CONSTRAINT fk_inventario_producto
    FOREIGN KEY (id_producto)
    REFERENCES producto (id_producto);

ALTER TABLE inventario
    ADD CONSTRAINT fk_inventario_almacen
    FOREIGN KEY (id_almacen)
    REFERENCES almacen (id_almacen);

ALTER TABLE movimiento_inventario
    ADD CONSTRAINT fk_movimiento_inventario_inventario
    FOREIGN KEY (id_inventario)
    REFERENCES inventario (id_inventario);

ALTER TABLE movimiento_inventario
    ADD CONSTRAINT fk_movimiento_inventario_tipo
    FOREIGN KEY (id_tipo_movimiento)
    REFERENCES tipo_movimiento (id_tipo_movimiento);

ALTER TABLE movimiento_inventario
    ADD CONSTRAINT fk_movimiento_inventario_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuario (id_usuario);

-- =========================
-- RESTRICCIONES UNIQUE
-- =========================

ALTER TABLE rol
    ADD CONSTRAINT uq_rol_nombre
    UNIQUE (nombre);

ALTER TABLE usuario
    ADD CONSTRAINT uq_usuario_usuario
    UNIQUE (usuario);

ALTER TABLE usuario
    ADD CONSTRAINT uq_usuario_correo
    UNIQUE (correo);

ALTER TABLE producto
    ADD CONSTRAINT uq_producto_codigo
    UNIQUE (codigo);

ALTER TABLE pedido
    ADD CONSTRAINT uq_pedido_numero
    UNIQUE (numero_pedido);

ALTER TABLE inventario
    ADD CONSTRAINT uq_inventario_producto_almacen
    UNIQUE (id_producto, id_almacen);

ALTER TABLE tipo_movimiento
    ADD CONSTRAINT uq_tipo_movimiento_nombre
    UNIQUE (nombre);

-- =========================
-- VALIDACIONES CHECK
-- =========================

ALTER TABLE producto
    ADD CONSTRAINT chk_producto_precio_compra
    CHECK (precio_compra >= 0);

ALTER TABLE producto
    ADD CONSTRAINT chk_producto_precio_venta
    CHECK (precio_venta >= 0);

ALTER TABLE producto
    ADD CONSTRAINT chk_producto_stock_minimo
    CHECK (stock_minimo >= 0);

ALTER TABLE pedido
    ADD CONSTRAINT chk_pedido_subtotal
    CHECK (subtotal >= 0);

ALTER TABLE pedido
    ADD CONSTRAINT chk_pedido_descuento
    CHECK (descuento >= 0);

ALTER TABLE pedido
    ADD CONSTRAINT chk_pedido_total
    CHECK (total >= 0);

ALTER TABLE detalle_pedido
    ADD CONSTRAINT chk_detalle_pedido_cantidad
    CHECK (cantidad > 0);

ALTER TABLE detalle_pedido
    ADD CONSTRAINT chk_detalle_pedido_precio_unitario
    CHECK (precio_unitario >= 0);

ALTER TABLE detalle_pedido
    ADD CONSTRAINT chk_detalle_pedido_descuento
    CHECK (descuento >= 0);

ALTER TABLE detalle_pedido
    ADD CONSTRAINT chk_detalle_pedido_subtotal
    CHECK (subtotal >= 0);

ALTER TABLE inventario
    ADD CONSTRAINT chk_inventario_stock_actual
    CHECK (stock_actual >= 0);

ALTER TABLE inventario
    ADD CONSTRAINT chk_inventario_stock_reservado
    CHECK (stock_reservado >= 0);

ALTER TABLE inventario
    ADD CONSTRAINT chk_inventario_stock_minimo
    CHECK (stock_minimo >= 0);

ALTER TABLE inventario
    ADD CONSTRAINT chk_inventario_reservado_actual
    CHECK (stock_reservado <= stock_actual);

ALTER TABLE movimiento_inventario
    ADD CONSTRAINT chk_movimiento_inventario_cantidad
    CHECK (cantidad > 0);

ALTER TABLE cliente
    ADD CONSTRAINT chk_cliente_correo
    CHECK (
        correo IS NULL
        OR correo LIKE '%_@_%._%'
    );

ALTER TABLE usuario
    ADD CONSTRAINT chk_usuario_correo
    CHECK (
        correo IS NULL
        OR correo LIKE '%_@_%._%'
    );

COMMIT;
