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

# Fetching weekly economic indicators

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve weekly economic indicators by passing the relevent [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_history` function with the `interval` parameter set to `"weekly"`.

Here's how to retrieve the number of new jobless claims in the US, a weekly indicator released by the US Department of Labor:

```{code-cell}
rd.get_history(
    "USJOB=ECI",
    interval="weekly",
)
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
