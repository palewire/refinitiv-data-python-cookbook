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

# Fetching a company's peers

```{code-cell}
:tags: [hide-cell]
import refinitiv.data as rd

rd.open_session()
```

You can use the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) to retrieve a list of the companies judged to be peers of a given company.

To do so, pass a company’s [Refinitiv Instrument Code](https://en.wikipedia.org/wiki/Refinitiv_Identification_Code) to the `Peer` component of the package's `discovery` submodule. By default, the method only returns the code of each peer. You'll need to pass the resulting list to another query to retrieve additional information about each company.

Here's how to retrieve each of the Thomson Reuters' peers:

```{code-cell}
rd.discovery.Peers("TRI.N")
```

You'll need to convert it to a `list` object to see the results.

```{code-cell}
list(rd.discovery.Peers("TRI.N"))
```

```{code-cell}
:tags: [hide-cell]
rd.close_session()
```
