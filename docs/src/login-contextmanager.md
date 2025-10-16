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

```{code-cell}
:tags: [hide-cell]
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
```

# Handing sessions with a context manager

By default, the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) expects you to open and close a session manually, typically done with the `open_session` and `close_session` functions.

This can lead to problems if you forget to close your session, and it can require you to write more code than you might like.

That can be avoided by using a [context manager](https://book.pythontips.com/en/latest/context_managers.html). Context managers allow you to create a block of code that is executed when you enter and exit a [`with`](https://peps.python.org/pep-0343/) statement. A common example from Python's standard library is opening and closing a file like so:

```python
with open("my_file.txt", "w") as f:
    f.write("Hello, world!")
```

Here's how to create a custom context manager that will open and close a LSEG Data Library for Python session:

```{code-cell}
from contextlib import contextmanager

import lseg.data as ld


@contextmanager
def ld_session():
    """Context manager for handling a LSEG Data Library for Python session."""
    try:
        # Create a session and return it
        ld.open_session()
        yield
    finally:
        # Close the session
        ld.close_session()
```

Once that's been introduced to your code, you can open a session by running the following code:

```{code-cell}
with ld_session():
    # Do whatever you want to do your `ld` session in the indent ...
    pass
```

Once the indent is removed, the session will be closed automatically. Here's how you could use it to get the current price of Thomson Reuters stock:

```{code-cell}
with ld_session():
    df = ld.get_history('TRI.N')

df.head(5)
```
