# app/api/v1/tracking_ws.py
from fastapi import APIRouter, WebSocket
from app.services.tracking_service import TrackingService

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            await TrackingService.handle_ws_message(ws, data)
    except Exception:
        await ws.close()
