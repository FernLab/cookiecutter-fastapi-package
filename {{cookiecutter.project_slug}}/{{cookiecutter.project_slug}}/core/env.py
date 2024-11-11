"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os

import {{ cookiecutter.project_slug }}

# --------------------------------------------------- #
# --------------------- Settings -------------------- #
ROOT_PATH = os.environ.get("ROOT_PATH", "")
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")
if "ALLOWED_ORIGINS" != "*":
    ALLOWED_ORIGINS = ALLOWED_ORIGINS.split(",")

# --------------------------------------------------- #
# ------------------- Directories ------------------- #
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname({{ cookiecutter.project_slug }}.__file__), ".."))

# --------------------------------------------------- #
# ---------------- Set Path for test ---------------- #
SERVICE_NAMESPACE = ""
if "SERVICE_NAMESPACE" in os.environ and os.environ["SERVICE_NAMESPACE"] == "test-service":
    SERVICE_NAMESPACE = os.environ["SERVICE_NAMESPACE"]

    # Creates a directory for results in test mode
    # if not os.path.isdir(RESULTS_DIR):
    #     Path(RESULTS_DIR).mkdir(parents=True, exist_ok=True)
