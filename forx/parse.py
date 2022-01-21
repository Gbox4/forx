# Gabe Banks 1/20/22 <https://gabebanks.net>

import argparse
import sys
from .settings import *
from .currency_data import *

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
        help="get price of 1 unit of FROM in terms of TO")

    arg.add_argument("-f", action="store_true",
        help="Disable formatting of price.")

    arg.add_argument("--list", action="store_true",
        help="Print list of valid currencies.")

    arg.add_argument("-v", action="store_true",
        help="Toggle verbosity.")

    arg.add_argument("--version", action="store_true",
        help="Print forx version.")

    return arg