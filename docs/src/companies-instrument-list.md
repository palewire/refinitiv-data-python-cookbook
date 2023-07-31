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
```{include} _templates/nav.html
```

# Fetching all companies in an index

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve metadata about all of the companies in a stock index.

To do so, pass the index's [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) with a `0#` prefix to the `fundamental_and_reference` component of package's `content` submodule.

The method requires that you specify at least one field to retrieve for each company, in addition to its code. Here's how to retrieve the name and ticket symbol of each of the 30 entries in the Dow Jones Industrial Average:


```{code-cell}
rd.content.fundamental_and_reference.Definition(
    universe=["0#.DJI"],
    fields=[
        "TR.CommonName",
        "TR.TickerSymbol"
    ],
).get_data().data.df
```

```{note}
In Refinitiv terminology, the `0#` prefix is known as a “chain.” It is used to identify a group of instruments that share a common characteristic, such as being part of an index.
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
