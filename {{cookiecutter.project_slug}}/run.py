"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import uvicorn

from {{ cookiecutter.project_slug }}.core import env as environment

HOST = environment.HOST
PORT = int(environment.PORT)

if __name__ == "__main__":
    try:
        uvicorn.run(
            "{{ cookiecutter.project_slug }}.create_app:app", host=HOST, port=PORT, reload=True
        )
    except Exception as e:
        raise RuntimeError(f"Unable to run the application => {e}")
