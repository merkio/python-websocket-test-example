import json
import allure
from websocket import WebSocket


@allure.step
def connect_by_protocol_with_client_info(protocol: int, client_info: dict, ws: WebSocket):
    ws.send(f'connect {protocol} {json.dumps(client_info)}')
    response = ws.recv()
    assert response == "connected"


