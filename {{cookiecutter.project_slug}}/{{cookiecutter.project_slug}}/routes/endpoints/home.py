"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import {{ cookiecutter.project_slug }}.schemas.general as general_schema
from {{ cookiecutter.project_slug }}.core.config_parser import config

router = APIRouter()

APP_NAME = config["meta"]["app_name"]


@router.get(
    "/",
    tags=["Home"],
    summary="Home Page",
    response_model=general_schema.Message,
    responses={
        404: {"model": general_schema.Message},
        500: {"model": general_schema.Message},
    },
)
def home():
    """Return HomePage."""
    return JSONResponse(
        status_code=200,
        content={
            "msg": f"{APP_NAME} APIs is working. "
            "Use /docs or /redoc to see the documentation."
        },
    )
