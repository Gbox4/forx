# Gabe Banks 1/20/22 <https://gabebanks.net>

import requests
from .parse import *

def get_price(base, to, verbose):
    request_url = f"https://api.coinbase.com/v2/exchange-rates?currency={base}"
    if verbose:
        print(f"Request URL: {request_url}")
    r = requests.get(request_url).json()
    out = float(r['data']['rates'][to.upper()])
    
    return out


def main():
    parser = get_args()
    parse_args_exit(parser)
    opts = parse_args(parser)

    base = opts['base']
    to = opts['to']
    quantity = opts['quantity']

    price = get_price(base, to, opts['verbose'])
    price *= quantity

    if opts['no_format']:
        print(price)
    else:
        symbol = ""
        if currency_symbols[to.upper()]:
            symbol = currency_symbols[to.upper()]
        
        formatted_price = "{:,.2f}".format(price)
        if price < 1:
            formatted_price = f"{price:.10f}"
            while formatted_price.endswith("0"):
                formatted_price = formatted_price[:-1]
        print(symbol + formatted_price)