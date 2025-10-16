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

# Authenticating in Python

You can authenticate with the [LSEG Data Library for Python](https://pypi.org/project/lseg-data/) directly inline using a function in the package’s `session` module.

It requires that provide your application key, as well as the username and password you use to access the LSEG web portal. In this example, they will be stored in environment variables to avoid exposing private information in the source code.

```{code-cell}
import os
import lseg.data as ld

session = ld.session.platform.Definition(
    app_key=os.getenv('LSEG_APP_KEY'),
    grant=ld.session.platform.GrantPassword(
        username=os.getenv('LSEG_USERNAME'),
        password=os.getenv('LSEG_PASSWORD')
    ),
    signon_control=True
).get_session()
```

Once that's successful, you can open a session:

```{code-cell}
session.open()
```

Then it as the default for the library.

```{code-cell}
ld.session.set_default(session)
```

Verify the session is open by executing a query for the current price of Thomson Reuters stock. You should back a table of data.

```{code-cell}
ld.get_history('TRI.N')
```


The library expects you to close your session when you're finished. You can do so by running the following code:

```{code-cell}
ld.close_session()
```
