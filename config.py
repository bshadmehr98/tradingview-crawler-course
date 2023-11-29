import json


class Config:
    def __init__(self, exchange, screener, symbol):
        self.exchange = exchange
        self.screener = screener
        self.symbol = symbol

    @staticmethod
    def load():
        with open("./config.json", "r") as f:
            config_json = json.load(f)
            return Config(**config_json)
