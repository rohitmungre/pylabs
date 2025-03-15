from fastapi import APIRouter, Request

router = APIRouter(prefix="/my-ip", tags=["My IP"])

@router.get("/")
def get_client_ip(request: Request):
    client_ip = request.client.host
    return {"ip": client_ip}
