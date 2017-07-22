# api wrapper

# exchange apis
from coinbase.wallet.client         import Client
from bitstamp.client                import Public
from gdax                           import PublicClient

# userinfo
from secrets import *


class Coinbase:
    def __init__(self, crypto = 'btc', base = 'usd'):
        self.crypto = crypto
        self.base = base
        self.client = Client(COINBASE_API_KEY, COINBASE_API_SECRET)

    @property
    def bid(self):
        return float(self.client.get_sell_price(currency_pair = self.crypto+'-'+self.base)['amount'])
    @property
    def spot(self):
        return float(self.client.get_spot_price(currency_pair = self.crypto+'-'+self.base)['amount'])
    @property
    def ask(self):
        return float(self.client.get_buy_price(currency_pair = self.crypto+'-'+self.base)['amount'])

class Bitstamp:
    def __init__(self, crypto = 'btc', base = 'usd'):
        self.crypto = crypto
        self.base = base
        self.client = Public()

    @property
    def bid(self):
        return float(self.client.ticker(base=self.crypto, quote=self.base)['bid'])
    @property
    def spot(self):
        return float(self.client.ticker(base=self.crypto, quote=self.base)['last'])
    @property
    def ask(self):
        return float(self.client.ticker(base=self.crypto, quote=self.base)['ask'])

class GDAX:
    def __init__(self, crypto = 'btc', base = 'usd'):
        self.crypto = crypto
        self.base = base
        self.client = PublicClient()

    @property
    def bid(self):
        return float(self.client.get_product_ticker(product_id=self.crypto+'-'+self.base)['bid'])
    @property
    def spot(self):
        return float(self.client.get_product_ticker(product_id=self.crypto+'-'+self.base)['price'])
    @property
    def ask(self):
        return float(self.client.get_product_ticker(product_id=self.crypto+'-'+self.base)['ask'])


def main():
    bs = Bitstamp()
    cb = Coinbase()
    gd = GDAX()
    print(bs.bid, bs.spot, bs.ask)
    print(cb.bid, cb.spot, cb.ask)
    print(gd.bid, gd.spot, gd.ask)




if __name__ == "__main__":
    main()
