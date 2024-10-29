"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os

import {{ cookiecutter.project_slug }}

SERVICE_NAMESPACE = ""

# --------------------------------------------------- #
# --------------------- Settings -------------------- #

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", "8881")
ROOT_PATH = os.environ["ROOT_PATH"] if "ROOT_PATH" in os.environ else ""
ALLOWED_ORIGINS = (
    os.environ["ALLOWED_ORIGINS"].split(",")
    if "ALLOWED_ORIGINS" in os.environ and os.environ["ALLOWED_ORIGINS"]
    else "*"
)

# --------------------------------------------------- #
# ------------------- Directories ------------------- #
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname({{ cookiecutter.project_slug }}.__file__), "..")
)

# --------------------------------------------------- #
# ---------------- Set Path for test ---------------- #
if (
    "service_namespace" in os.environ
    and os.environ["service_namespace"] == "test-service"
):
    SERVICE_NAMESPACE = os.environ["service_namespace"]

    # Creates a directory for results in test mode
    # if not os.path.isdir(RESULTS_DIR):
    #     Path(RESULTS_DIR).mkdir(parents=True, exist_ok=True)
