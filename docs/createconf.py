import json
import os
from pathlib import Path

THIS_DIR = Path(__file__).parent.resolve()


def main():
    """Create the lseg-data.config.json file used by the documentation site."""
    # Open the template file
    with open(THIS_DIR / "src/lseg-data.config.tmpl") as fp:
        tmpl = json.load(fp)

    # Drop in the private variables from the environment
    tmpl["sessions"]["platform"]["rdp"].update(
        {
            "app-key": os.environ["LSEG_APP_KEY"],
            "username": os.environ["LSEG_USERNAME"],
            "password": os.environ["LSEG_PASSWORD"],
        }
    )

    # Write out the config file
    with open(THIS_DIR / "src/lseg-data.config.json", "w") as fp:
        json.dump(tmpl, fp, indent=2)


if __name__ == "__main__":
    main()
