BEGIN;

-- =========================================================
-- FERRESYS
-- Migración 004: vincular pedidos con almacenes
-- Fecha: 2026-07-30
-- =========================================================

ALTER TABLE pedido
    ADD COLUMN id_almacen BIGINT;

-- Para los pedidos ya existentes se asigna el primer almacén.
UPDATE pedido
SET id_almacen = (
    SELECT MIN(id_almacen)
    FROM almacen
)
WHERE id_almacen IS NULL;

ALTER TABLE pedido
    ALTER COLUMN id_almacen SET NOT NULL;

ALTER TABLE pedido
    ADD CONSTRAINT fk_pedido_almacen
    FOREIGN KEY (id_almacen)
    REFERENCES almacen (id_almacen);

CREATE INDEX idx_pedido_id_almacen
    ON pedido (id_almacen);

COMMIT;
