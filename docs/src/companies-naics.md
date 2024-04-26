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

# Fetching a company's NAICS codes

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve the [North American Industry Classification System](https://www.census.gov/naics/) (NAICS) codes associated with a company. It is a standard used by US statistical agencies to classify business establishments for economic analysis.

To do acquire the data, pass a company’s [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_data` method with a request for NAICS related fields.

Here's a query for Thomson Reuters:

```{code-cell}
rd.get_data(
    'TRI.N',
    fields=[
        # Basic stuff
        "TR.CommonName",
        "TR.TickerSymbol",
        # NAICS codes
        "TR.NAICSSectorCode",
        "TR.NAICSSector",
        "TR.NAICSSubsectorCode",
        "TR.NAICSSubsector",
        "TR.NAICSIndustryGroupCode",
        "TR.NAICSIndustryGroup",
        "TR.NAICSIndustryCode",
        "TR.NAICSIndustry",
        "TR.NAICSActivityCode",
        "TR.NAICSActivity",
    ]
)
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
