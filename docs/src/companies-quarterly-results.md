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

# Fetching quarterly results

```{code-cell}
:tags: [hide-cell]
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import lseg.data as ld

ld.open_session()
```

You can use the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) to retrieve quarterly results that company's post each earnings season.

To do so, pass the company's [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `get_data` submodule. In addition to the code, you must provide custom parameters that specify the metric, time interval and number of periods to retrieve.

## Earnings per share

Here’s how to retrieve earnings per share for the last eight fiscal quarters for Thomson Reuters.

First define the metric you want to retrieve, followed by the time interval and number of periods in parenthesis.

```{code-cell}
expression = "TR.EPSFRActValue(SDate=0,EDate=-8,Period=FQ0,Frq=FQ)"
```

Then query the data for the company, asking for the metric as well as the date it was released and the last fiscal quarter's end date.

```{code-cell}
ld.get_data(
    "TRI.TO",
    fields=[
        f"{expression}.Date",
        f"{expression}.periodenddate",
        expression,
    ],
)
```

## Revenue

The same logic can be used to query revenue, which is provided by the "TR.RevenueActValue" field.

```{code-cell}
expression = "TR.RevenueActValue(SDate=0,EDate=-8,Period=FQ0,Frq=FQ)"

ld.get_data(
    "TRI.TO",
    fields=[
        f"{expression}.Date",
        f"{expression}.periodenddate",
        expression,
    ],
)
```


```{code-cell}
:tags: [hide-cell]
ld.close_session()
```
