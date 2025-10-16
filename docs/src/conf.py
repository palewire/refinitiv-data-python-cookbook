from datetime import datetime

extensions = [
    "myst_nb",
]

source_suffix = ".md"
master_doc = "index"

project = "LSEG Data Python Cookbook"
year = datetime.now().year
copyright = f"{year} palewi.re"

exclude_patterns = ["_build"]

html_theme = "palewire"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
    ]
}
html_theme_options = {
    "canonical_url": "https://palewi.re/docs/refinitiv-data-python-cookbook/",
}

html_static_path = ["_static"]
pygments_style = "sphinx"
