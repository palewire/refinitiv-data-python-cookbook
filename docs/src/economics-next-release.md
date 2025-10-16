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

# Fetching an economic indicator's next release date

```{code-cell}
:tags: [hide-cell]
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import lseg.data as ld

ld.open_session()
```

You can use the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) to retrieve an economic indicator's next release date by passing the relevant [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_data` function and requesting the necessary fields.

The `ECI_ACT_DT` field contains the confirmed date when new data will be released. This is the preferred field as it represents the official release schedule. However, this field may not be updated immediately after a release, causing it to show a past date until the next schedule is entered into the system.

The `NDOR_1` field is a forward-looking value that always contains the next scheduled release date. This serves as our fallback when `ECI_ACT_DT` is stale or in the past.

Here's how to retrieve the next release date for the US Consumer Price Index, a monthly inflation indicator released by the US Bureau of Labor Statistics:

```{code-cell}
ld.get_data(
    "USCPI=ECI",
    fields=["ECI_ACT_DT", "NDOR_1"],
)
```
