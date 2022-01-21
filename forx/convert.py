# Gabe Banks 1/20/22 <https://gabebanks.net>

import requests
import argparse
import sys


extra_help = """Examples:
    forx btc usd # Price of 1 BTC in USD
    forx btc usd -q 2 # Price of 2 BTC in USD
    forx cny usd -f # Price of 1 CNY in USD, with no formatting
"""
__version__ = "1.0.0"
valid_currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SEK', 'SHP', 'SKK', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'SVC', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMW', 'JEP', 'GGP', 'IMP', 'GBX', 'CNH', 'TMM', 'ZWL', 'SGD', 'USD', 'BTC', 'BCH', 'BSV', 'ETH', 'ETH2', 'ETC', 'LTC', 'ZRX', 'USDC', 'BAT', 'MANA', 'KNC', 'LINK', 'DNT', 'MKR', 'CVC', 'OMG', 'DAI', 'ZEC', 'XRP', 'REP', 'XLM', 'EOS', 'XTZ', 'ALGO', 'DASH', 'ATOM', 'OXT', 'COMP', 'ENJ', 'REPV2', 'BAND', 'NMR', 'CGLD', 'UMA', 'LRC', 'YFI', 'UNI', 'BAL', 'REN', 'WBTC', 'NU', 'YFII', 'FIL', 'AAVE', 'BNT', 'GRT', 'SNX', 'STORJ', 'SUSHI', 'MATIC', 'SKL', 'ADA', 'ANKR', 'CRV', 'ICP', 'NKN', 'OGN', '1INCH', 'USDT', 'FORTH', 'CTSI', 'TRB', 'POLY', 'MIR', 'RLC', 'DOT', 'SOL', 'DOGE', 'MLN', 'GTC', 'AMP', 'SHIB', 'CHZ', 'KEEP', 'LPT', 'QNT', 'BOND', 'RLY', 'CLV', 'FARM', 'MASK', 'FET', 'PAX', 'ACH', 'ASM', 'PLA', 'RAI', 'TRIBE', 'ORN', 'IOTX', 'UST', 'QUICK', 'AXS', 'REQ', 'WLUNA', 'TRU', 'RAD', 'COTI', 'DDX', 'SUKU', 'RGT', 'XYO', 'ZEN', 'AUCTION', 'JASMY', 'WCFG', 'BTRST', 'AGLD', 'AVAX', 'FX', 'TRAC', 'LCX', 'ARPA', 'BADGER', 'KRL', 'PERP', 'RARI', 'DESO', 'API3', 'NCT', 'SHPING', 'CRO', 'MDT', 'VGX', 'ALCX', 'COVAL', 'FOX', 'MUSD', 'GALA', 'POWR', 'GYEN', 'INV', 'LQTY', 'PRO', 'SPELL', 'ENS', 'BLZ', 'IDEX', 'MCO2', 'POLS', 'SUPER', 'STX', 'GODS', 'IMX', 'RBN', 'BICO', 'GFI']
# Currency symbols from https://github.com/arshadkazmi42/currency-symbols/blob/master/currency_symbols/constants.py
currency_symbols = CURRENCY_SYMBOLS_MAP = {"AED": "د.إ", "AFN": "؋", "ALL": "L", "AMD": "֏", "ANG": "ƒ", "AOA": "Kz", "ARS": "$", "AUD": "$", "AWG": "ƒ", "AZN": "₼", "BAM": "KM", "BBD": "$", "BDT": "৳", "BGN": "лв", "BHD": ".د.ب", "BIF": "FBu", "BMD": "$", "BND": "$", "BOB": "$b", "BRL": "R$", "BSD": "$", "BTC": "฿", "BTN": "Nu.", "BWP": "P", "BYR": "Br", "BYN": "Br", "BZD": "BZ$", "CAD": "$", "CDF": "FC", "CHF": "CHF", "CLP": "$", "CNY": "¥", "COP": "$", "CRC": "₡", "CUC": "$", "CUP": "₱", "CVE": "$", "CZK": "Kč", "DJF": "Fdj", "DKK": "kr", "DOP": "RD$", "DZD": "دج", "EEK": "kr", "EGP": "£", "ERN": "Nfk", "ETB": "Br", "ETH": "Ξ", "EUR": "€", "FJD": "$", "FKP": "£", "GBP": "£", "GEL": "₾", "GGP": "£", "GHC": "₵", "GHS": "GH₵", "GIP": "£", "GMD": "D", "GNF": "FG", "GTQ": "Q", "GYD": "$", "HKD": "$", "HNL": "L", "HRK": "kn", "HTG": "G", "HUF": "Ft", "IDR": "Rp", "ILS": "₪", "IMP": "£", "INR": "₹", "IQD": "ع.د", "IRR": "﷼", "ISK": "kr", "JEP": "£", "JMD": "J$", "JOD": "JD", "JPY": "¥", "KES": "KSh", "KGS": "лв", "KHR": "៛", "KMF": "CF", "KPW": "₩", "KRW": "₩", "KWD": "KD", "KYD": "$", "KZT": "лв", "LAK": "₭", "LBP": "£", "LKR": "₨", "LRD": "$", "LSL": "M", "LTC": "Ł", "LTL": "Lt", "LVL": "Ls", "LYD": "LD", "MAD": "MAD", "MDL": "lei", "MGA": "Ar", "MKD": "ден", "MMK": "K", "MNT": "₮", "MOP": "MOP$", "MRO": "UM", "MRU": "UM", "MUR": "₨", "MVR": "Rf", "MWK": "MK", "MXN": "$", "MYR": "RM", "MZN": "MT", "NAD": "$", "NGN": "₦", "NIO": "C$", "NOK": "kr", "NPR": "₨", "NZD": "$", "OMR": "﷼", "PAB": "B/.", "PEN": "S/.", "PGK": "K", "PHP": "₱", "PKR": "₨", "PLN": "zł", "PYG": "Gs", "QAR": "﷼", "RMB": "￥", "RON": "lei", "RSD": "Дин.", "RUB": "₽", "RWF": "R₣", "SAR": "﷼", "SBD": "$", "SCR": "₨", "SDG": "ج.س.", "SEK": "kr", "SGD": "$", "SHP": "£", "SLL": "Le", "SOS": "S", "SRD": "$", "SSP": "£", "STD": "Db", "STN": "Db", "SVC": "$", "SYP": "£", "SZL": "E", "THB": "฿", "TJS": "SM", "TMT": "T", "TND": "د.ت", "TOP": "T$", "TRL": "₤", "TRY": "₺", "TTD": "TT$", "TVD": "$", "TWD": "NT$", "TZS": "TSh", "UAH": "₴", "UGX": "USh", "USD": "$", "UYU": "$U", "UZS": "лв", "VEF": "Bs", "VND": "₫", "VUV": "VT", "WST": "WS$", "XAF": "FCFA", "XBT": "Ƀ", "XCD": "$", "XOF": "CFA", "XPF": "₣", "YER": "﷼", "ZAR": "R", "ZWD": "Z$"}


def parse_args_exit(parser):
    """Process args that exit."""
    args = parser.parse_args()

    if args.version:
        print(f"forx {__version__}\nWritten by Gabe Banks 2022 <https://gabebanks.net>")
        sys.exit(0)

    if args.list:
        out = ""
        for i in valid_currencies:
            out += i + ", "
        print(out[:-2])
        sys.exit(0)

    if len(args.currencies) != 2:
        parser.print_help()
        sys.exit(0)

def parse_args(parser):
    """Parse args."""
    args = parser.parse_args()
    opts = {
        "base": args.currencies[0],
        "to": args.currencies[1],
        "quantity": args.q,
        "no_format": args.f,
        "verbose": args.v,
    }

    # Validate arguments
    for c in args.currencies:
        if c.upper() not in valid_currencies:
            print(f"Invalid currency {c}.")
            sys.exit(1)

    # Print options if verbose
    if args.v:
        for k, v in opts.items():
            print(f"{k}: {v}")

    return opts



def get_args():
    """Get the script arguments."""
    description = "forx - command line tool for getting exchange rates"
    arg = argparse.ArgumentParser(description=description, epilog=extra_help, formatter_class=argparse.RawTextHelpFormatter)

    arg.add_argument("currencies", metavar="FROM\tTO", nargs='*',
        help="get price of FROM in terms of TO")

    arg.add_argument("-q", metavar="AMOUNT", type=int, default=1,
        help="Quantity of FROM currency. Defaults to 1.")

    arg.add_argument("-f", action="store_true",
        help="Disable formatting of price.")

    arg.add_argument("--list", action="store_true",
        help="Print list of valid currencies.")

    arg.add_argument("-v", action="store_true",
        help="Toggle verbosity.")

    arg.add_argument("--version", action="store_true",
        help="Print forx version.")

    return arg



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

if __name__ == "__main__":
    main()