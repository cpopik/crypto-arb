# api wrapper

# exchange apis
from coinbase.wallet.client         import Client
from bitstamp.client                import Public

# userinfo
from secrets import *


class Coinbase:
    def __init__(self):
        self.client = Client(COINBASE_API_KEY, COINBASE_API_SECRET)

    @property
    def bid(self):
        return float(self.client.get_sell_price(currency_pair = 'BTC-USD')['amount'])
    @property
    def spot(self):
        return float(self.client.get_spot_price(currency_pair = 'BTC-USD')['amount'])
    @property
    def ask(self):
        return float(self.client.get_buy_price(currency_pair = 'BTC-USD')['amount'])

class Bitstamp:
    def __init__(self):
        self.client = Public()

    @property
    def bid(self):
        return float(self.client.ticker()['bid'])
    @property
    def spot(self):
        return float(self.client.ticker()['last'])
    @property
    def ask(self):
        return float(self.client.ticker()['ask'])




def main():
    bs = Bitstamp()
    cb = Coinbase()
    print(bs.bid, bs.spot, bs.ask)
    print(cb.bid, cb.spot, cb.ask)




if __name__ == "__main__":
    main()
