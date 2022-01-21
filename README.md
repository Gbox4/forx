# ForX - get forex quotes from the terminal

`forx` is a command line tool for checking exchange rates between currencies, both crypto and fiat.

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

# Donate

I develop `forx` for free in my spare time. If you like it, and want to by me a coffee, I'd really appreciate it.

Bitcoin: (<a href='https://i.ibb.co/b2rS0kV/btcgithubtstock.png'>QR</a>) `bc1qusuztegpfuh7jk25l2dx5xyjvasgryrqg42d5n`

Monero: (<a href='https://i.ibb.co/PNhgC3q/xmrgithubtstock.png'>QR</a>) `87wuCKbbchKV8Dz3JRoSN3jaqWBSiEShFXkFrYUaKT8Bew4P7dFvUJWVVR6RLr84J44QCdtNVyR6QC7aCSKYUWfnGK9y4K2`
