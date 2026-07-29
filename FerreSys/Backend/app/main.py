from fastapi import FastAPI
from sqlalchemy import text

from app.api.routes.almacenes import router as almacenes_router
from app.api.routes.clientes import router as clientes_router
from app.api.routes.inventarios import router as inventarios_router
from app.api.routes.productos import router as productos_router
from app.core.config import settings
from app.db.database import engine


app = FastAPI(
    title=settings.app_name,
    description="Backend oficial del sistema FerreSys",
    version=settings.app_version,
)

app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(almacenes_router)
app.include_router(inventarios_router)


@app.get("/")
def inicio() -> dict[str, str]:
    return {
        "sistema": "FerreSys",
        "estado": "Backend funcionando",
        "version": settings.app_version,
        "entorno": settings.app_env,
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/database")
def database_health_check() -> dict[str, str]:
    with engine.connect() as connection:
        database_name = connection.execute(
            text("SELECT current_database()")
        ).scalar_one()

    return {
        "status": "ok",
        "database": database_name,
    }
