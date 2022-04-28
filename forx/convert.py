# Gabe Banks 1/20/22 <https://gabebanks.net>

import sys
import argparse
import requests

from .currency_data import *

__version__ = "1.0.4"

# Prints on --help
extra_help = """Examples:
    forx btc usd # Price of 1 BTC in USD
    forx btc usd -q 2 # Price of 2 BTC in USD
    forx cny usd -f # Price of 1 CNY in USD, with no formatting
"""


def parse_args_exit(parser):
    """Process args that exit."""
    args = parser.parse_args()

    if args.version:
        print(f"forx {__version__}\nWritten by Gabe Banks 2022 <https://gabebanks.net>")
        sys.exit(0)

    if args.list:
        print("-----Fiat Currencies-----")
        for code, data in FIAT_CURRENCIES.items():
            print(f"{code}:", data["name"], data["flag"])

        print("-----Crypto Currencies------")
        for code, data in CRYPTO_CURRENCIES.items():
            print(f"{code}:", data["name"])

        sys.exit(0)

    # Script should always take exactly two positional arguments: from_currency and to_currency
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
    for currency in args.currencies:
        currency = currency.upper()
        if not (
            currency in FIAT_CURRENCIES.keys() or currency in CRYPTO_CURRENCIES.keys()
        ):
            print(f"Invalid currency {currency}.")
            sys.exit(1)

    # Print options if verbose
    if args.v:
        for k, v in opts.items():
            print(f"{k}: {v}")

    return opts


def get_args():
    """Get the script arguments."""
    description = "forx - a command line tool for checking exchange rates between currencies, both crypto and fiat."

    arg = argparse.ArgumentParser(
        description=description,
        epilog=extra_help,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    arg.add_argument(
        "currencies",
        metavar="FROM\tTO",
        nargs="*",
        help="get price of FROM in terms of TO",
    )

    arg.add_argument(
        "-q",
        metavar="AMOUNT",
        type=float,
        default=1,
        help="Quantity of FROM currency. Defaults to 1.",
    )

    arg.add_argument("-f", action="store_true", help="Disable formatting of price.")

    arg.add_argument(
        "--list", action="store_true", help="Print list of valid currencies."
    )

    arg.add_argument("-v", action="store_true", help="Toggle verbosity.")

    arg.add_argument("--version", action="store_true", help="Print forx version.")

    return arg


def get_price(base: str, to: str, verbose: bool) -> float:
    """
    Convert one unit of one currency into another using Coinbase API.

            Parameters:
                    base (str): The base currency code (Ex: USD)
                    to (str): The currency code to convert to
                    verbose (bool): Verbosity

            Returns:
                    rate (float): The price of 'base' in terms of 'to'
    """
    request_url = f"https://api.coinbase.com/v2/exchange-rates?currency={base}"

    if verbose:
        print(f"Request URL: {request_url}")

    try:
        r = requests.get(request_url).json()
    except Exception:
        print(
            "An error occured while making an HTTP request. Are you connected to the internet?"
        )
        sys.exit(1)

    return float(r["data"]["rates"][to])


def main():
    """forx main script body."""
    parser = get_args()
    parse_args_exit(parser)
    opts = parse_args(parser)

    base = opts["base"].upper()
    to = opts["to"].upper()

    try:
        base_data = FIAT_CURRENCIES[base]
    except KeyError:
        base_data = CRYPTO_CURRENCIES[base]
    try:
        to_data = FIAT_CURRENCIES[to]
    except KeyError:
        to_data = CRYPTO_CURRENCIES[to]

    if opts["verbose"]:
        print(f"Base data: {base_data}")
        print(f"To data: {to_data}")

    # Get price and multiply it by specified quantity (default 1)
    price = get_price(base, to, opts["verbose"]) * opts["quantity"]

    # Output the price
    if opts["no_format"]:
        print(price)
    else:
        formatted_price = "{:,.2f}".format(price)
        if price < 1:
            formatted_price = f"{price:.10f}"
            while formatted_price.endswith("0"):
                formatted_price = formatted_price[:-1]
        print(to_data["sympol"] + formatted_price)


if __name__ == "__main__":
    main()
