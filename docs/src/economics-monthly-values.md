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

# Fetching monthly economic indicators

```{code-cell}
:tags: [hide-cell]
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import lseg.data as ld

ld.open_session()
```

You can use the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) to retrieve monthly economic indicators like inflation and unemployment by passing the relevent [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_history` function with the `interval` parameter set to `"monthly"`.

Here's how to retrieve the Consumer Price Index, a monthly inflation indicator released by the US Bureau of Labor Statistics:

```{code-cell}
ld.get_history(
    "USCPI=ECI",
    interval="monthly",
)
```

```{code-cell}
:tags: [hide-cell]
ld.close_session()
```
