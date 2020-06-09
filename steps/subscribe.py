import json
import allure
from jsonschema import Draft6Validator
from websocket import WebSocket
from jsonschemas import *


@allure.step
def init_instrument_subscription(instrument_id: str, ws: WebSocket):
    instrument_data = {"type": "instrument", "id": instrument_id}
    ws.send(f'sub 1 {json.dumps(instrument_data)}')
    response = ws.recv()
    print(response)
    index = response.split(" ", 1)[0].strip()
    assert 1 == int(index)
    code = response.split(" ", 2)[1].strip()
    assert 'A' == code
    body = json.loads(response.split(" ", 2)[2])
    validator = Draft6Validator(instrument.INSTRUMENT_TOPIC_SCHEMA)
    validator.validate(body)

