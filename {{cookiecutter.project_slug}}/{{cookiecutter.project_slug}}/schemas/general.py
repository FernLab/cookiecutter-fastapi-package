"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

from typing import Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A general template for those responses contain a message."""

    msg: Optional[str] = Field(title="Message", description="Message from the API")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "msg": "This is a test message coming from the API.",
            },
        }
    }