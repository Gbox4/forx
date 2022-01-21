# ForX - get forex quotes from the terminal

`forx` is a command line script for getting forex quotes/exchange rates/currency conversions from the terminal.

# Features

- Conversions between all major world currencies.
- Supports major cryptocurrencies, exchange rates
- Formatted output and raw output
- Convert different quantities of currency

# Dependencies

Python 3.6 or above.

# Installation

### AUR

For archlinux based systems, `forx` is available on the AUR. Install it with your favority AUR helper. Example using `yay`:

```
yay -S forx
```

### PyPI

`forx` is also available as a python package. Simply install using `pip`:

```
pip install forx
```

# Usage

Here are some examples of using `forx`:

```bash
forx btc usd # Price of 1 BTC in USD
forx btc usd -q 2 # Price of 2 BTC in USD
forx cny usd -f # Price of 1 CNY in USD, with no formatting
```