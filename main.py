# main.py
from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Dummy token-by-token streaming simulation
            response = f"Simulating native stream for: {data}"
            for chunk in response.split():
                await websocket.send_text(chunk + " ")
                await asyncio.sleep(0.05) # Sub-100ms delay
    except Exception as e:
        print(f"Connection closed: {e}")
