import os


class TestParameters:

    def __init__(self) -> None:
        self.base_url = os.getenv('base_url', 'wss://api.staging.neontrading.com')
        self.sub_ticket_number = os.getenv('sub_ticket_number', '')
