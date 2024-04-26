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

# Fetching custom time ranges

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve economic indicators for custom time ranges by passing a `start` and `end` date to the `get_history` function.

The inputs should be `datetime.timedelta` objects. The `start` argument is how many days before today to start the range, and the `end` argument is how many days before today to end the range.

This example retrieves the US unemployment rate for the last 20 years:

```{code-cell}
from datetime import timedelta

rd.get_history(
    "USUNR=ECI",
    # Note that this number is negative because it's in the past
    start=timedelta(days=-365 * 20),
    # `end` is set to zero to draw the latest numbers
    end=timedelta(days=0),
)
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
