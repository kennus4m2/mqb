from datetime import datetime, timezone

from fastapi import APIRouter

from app.db import get_connection
from app.errors import AppError

router = APIRouter()


@router.get("/health")
def health():
    try:
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        finally:
            conn.close()
    except Exception:
        raise AppError(503, "DATABASE_DOWN", "The database is not available right now.")

    return {
        "status": "ok",
        "database": "ok",
        "time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
