from fastapi import APIRouter
import time

router = APIRouter(prefix="/status", tags=["Status"])

start_time = time.time()

@router.get("/")
def get_status():
    uptime = time.time() - start_time
    return {
        "status": "OK",
        "uptime_seconds": round(uptime, 2)
    }
