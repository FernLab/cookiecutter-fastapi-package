"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

from fastapi import APIRouter

from {{ cookiecutter.project_slug }}.routes.endpoints import home, item

api_router = APIRouter()
api_router.include_router(home.router)
api_router.include_router(item.router)
