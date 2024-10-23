"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os

import {{ cookiecutter.project_slug }}

SERVICE_NAMESPACE = ""

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
