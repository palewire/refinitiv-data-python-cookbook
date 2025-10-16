---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Fetching commodity prices

```{code-cell}
:tags: [hide-cell]
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import lseg.data as ld

ld.open_session()
```

You can use the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) to retrieve the latest price of a commodity by passing its [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_data` function.

Adding an equals sign as a suffix will return the value in US dollars. Here's the spot price of gold:

```python
ld.get_data("XAU=")
```

The `get_data` query requires that you account have access to real-time trading data, which is not available to all users. If you don't, you can request the latest `"1min"` intervals from the `get_history` method.

```{code-cell}
ld.get_history(
    "XAU=",
    interval="1min",
).tail(1)
```

## Historical data

You can retrieve historical stock prices by passing a Refinitiv Instrument Code to the `get_history` function. By default it returns the closing price for the last 30 days.

```{code-cell}
ld.get_history('XAU=')
```

## Multiple instruments

You can retrieve data for multiple instruments by passing a list of Refinitiv Instrument Codes to the `get_data` and `get_history` functions.

```{code-cell}
ld.get_history(['XAU=', 'XAG='])
```

```{code-cell}
:tags: [hide-cell]
ld.close_session()
```
