import ssl
import pytest
import websocket


@pytest.fixture(name='ws', scope='function')
def websocket_client():
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.timeout = 5
    yield ws
    ws.close()
