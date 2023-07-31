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

# Authenticating with a configuration file

By default, the [Refinitiv Data Library for Python](https://pypi.org/project/refinitiv-data/) expects you to provide credentials in a configuration file named `refinitiv-data.config.json`.

At minimum, it must include your application key, as well as the username and password you use to access the Refinitiv web portal.

Start by copying and pasting the following snippet into a file named `refinitiv-data.config.json`. Replace the placeholder values with your credentials.

```javascript
{
  "sessions": {
    "default": "platform.rdp",
    "platform": {
      "rdp": {
        "app-key": "YOUR APP KEY GOES HERE!",
        "username": "YOUR RDP LOGIN OR MACHINE GOES HERE!",
        "password": "YOUR RDP PASSWORD GOES HERE!"
      }
    }
  }
}
```

```{note}
A fuller example of all the configuration options available can be found in Refinitiv's [official documentation](https://github.com/Refinitiv-API-Samples/Example.DataLibrary.Python/blob/main/Configuration/refinitiv-data.config.json).
```

Unless you provide further instruction your Python script will expect the configuration file to be located in the same directory as the script you are running. Once the file is in place, you can import the library and open a session by running the following code:

```{code-cell}
import refinitiv.data as rd

rd.open_session()
```

Verify the session is open by executing a query for the current price of Thomson Reuters stock. You should back a table of data.

```{code-cell}
rd.get_history('TRI.N')
```

The library expects you to close your session when you're finished. You can do so by running the following code:

```{code-cell}
rd.close_session()
```

## Specifying a configuration file

If you want to store your configuration file in a different location, you can specify its path when you open a session.

For example, if you gave your configuration file with a shorter name and stored it in a subdirectory named `config`, you could open a session by running something like the following:

```python
rd.open_session(
  config_name='./config/refinitiv.json'
)
```