from typing import Optional
from typing import List
from binance.spot import Spot


class Binance:
    def __init__(self):
        self.client = Spot()

    def ping(self):
        return self.client.ping()

    def time(self):
        return self.client.time()

    def exchange_info(
        self, symbol: Optional[str] = None, symbols: Optional[List[str]] = None
    ):
        return self.client.exchange_info(symbol=symbol, symbols=symbols)

    def avg_price(self, symbol: str):
        return self.client.avg_price(symbol)

    def ticker_24hr(self, symbol: Optional[str] = None):
        return self.client.ticker_24hr(symbol)

    def ticker_price(self, symbol: Optional[str] = None):
        return self.client.ticker_price(symbol)


def main():
    binance = Binance()

    print(binance.ping())

    server_time = binance.time()
    print(f"Server time is {server_time['serverTime']}.")


if __name__ == "__main__":
    main()
