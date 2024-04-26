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

# Fetching a company's TRBC codes

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve the [The Refinitiv Business Classification](https://en.wikipedia.org/wiki/The_Refinitiv_Business_Classification) (TRBC) codes associated with a company. The standard is used by Refinitiv to classify business establishments for economic analysis.

To do acquire the data, pass a company’s [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_data` method with a request for TRBC related fields.

Here's a query for Thomson Reuters:

```{code-cell}
rd.get_data(
    'TRI.N',
    fields=[
        # Basic stuff
        "TR.CommonName",
        "TR.TickerSymbol",
        # TRBC codes
        "TR.TRBCEconSectorCode",
        "TR.TRBCEconomicSector",
        "TR.TRBCBusinessSectorCode",
        "TR.TRBCBusinessSector",
        "TR.TRBCIndustryGroupCode",
        "TR.TRBCIndustryCode",
        "TR.TRBCIndustry",
        "TR.TRBCActivityCode",
        "TR.TRBCActivity",
    ]
)
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
