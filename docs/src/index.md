# Refinitiv Data Python Cookbook

Practical examples for users of the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/)

## What this is

This collection of Python snippets will show you how to use the [`refinitiv-data`](https://pypi.org/project/refinitiv-data/) library to retrieve data on markets, companies and macroeconomics.

## Who can use it

Like the Refinitiv Python client, this cookbook is free. All it requires is a [Refinitiv Eikon](https://eikon.refinitiv.com/) account with access to the company's [private data services](https://developers.refinitiv.com/en/api-catalog/eikon/eikon-data-api).

## Table of contents

```{toctree}
:maxdepth: 1
:caption: Getting Started
:name: getting-started

./appkey.md
./install.md
./import.md
```

```{toctree}
:maxdepth: 1
:caption: Logging in
:name: logging-in

./login-config-file.md
./login-inline.md
./login-contextmanager.md
```

```{toctree}
:maxdepth: 1
:caption: Markets
:name: markets

./markets-stock-prices.md
./markets-index-prices.md
./markets-commodity-prices.md
./markets-time-range.md
```

```{toctree}
:maxdepth: 1
:caption: Companies
:name: companies

./companies-instrument-list.md
./companies-peer-list.md
./companies-naics.md
./companies-trbc.md
./companies-quarterly-results.md
```

```{toctree}
:maxdepth: 1
:caption: Macroeconomics
:name: macroeconomics

./economics-monthly-values.md
./economics-weekly-values.md
./economics-time-range.md
```
