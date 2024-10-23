"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import {{cookiecutter.project_slug}}.schemas.general as general_schema
import {{cookiecutter.project_slug}}.schemas.item as item_schema

router = APIRouter()

TAG = ["Item"]

data = [
    {"id": "1", "price": 12.99},
    {"id": "2", "price": 15.89},
    {"id": "3", "price": 11.19},
    {"id": "4", "price": 13.49},
]


@router.get(
    "/item",
    tags=TAG,
    summary="Get a list of items",
    response_model=item_schema.GETItemsResponse,
    responses={
        404: {"model": general_schema.Message},
        500: {"model": general_schema.Message},
    },
)
def get_items():
    """Return a list of items."""
    return {"data": data}


@router.get(
    "/item/{item_id}",
    tags=TAG,
    summary="Get item by id",
    response_model=item_schema.GETItemResponse,
    responses={
        404: {"model": general_schema.Message},
        500: {"model": general_schema.Message},
    },
)
def get_item_by_id(item_id: str):
    """Return an item from list by its id."""
    item = [item for item in data if item["id"] == item_id]
    if not item:
        return JSONResponse(
            status_code=404, content={"msg": f"Item with id ({item_id}) not found!"}
        )

    return {"data": item[0]}
