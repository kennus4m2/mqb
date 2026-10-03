from fastapi import FastAPI

from app.errors import register_error_handlers
from app.routes import game_info, health

app = FastAPI(title="Monster Quiz Battle API")
register_error_handlers(app)

app.include_router(game_info.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")