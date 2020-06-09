import pytest
from websocket import WebSocket
from config import parameters
from steps.connect import connect_by_protocol_with_client_info
from steps.subscribe import init_instrument_subscription
from test_data import client_info


@pytest.mark.smoke
class TestSubscription:

    @pytest.mark.asyncio
    async def test_connection(self, ws: WebSocket):
        ws.connect(parameters.base_url)
        connect_by_protocol_with_client_info(21, client_info.IOS_CLIENT_INFO, ws)

    @pytest.mark.asyncio
    async def test_instrument_subscription(self, ws: WebSocket):
        ws.connect(parameters.base_url)
        connect_by_protocol_with_client_info(21, client_info.IOS_CLIENT_INFO, ws)
        init_instrument_subscription('DE000BASF111', ws)
