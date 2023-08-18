from pydantic import BaseModel, Field


class HTTPError(BaseModel):
    """
    A simple model only for presentation based on what `HTTPException` returns.
    """
    detail: str = Field(
        example="A message containing what went wrong.",
        description="The error message that is occurred."
    )
