"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os
from configparser import ConfigParser

config = ConfigParser()

try:
    CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")

    if not config.read(CONFIG_FILE):  # pragma: no cover
        raise ValueError("Empty configuration file!")

    config.read(CONFIG_FILE)

except Exception as e:  # pragma: no cover
    raise RuntimeError(f"Unable to read config.ini file => {e}!") from e
