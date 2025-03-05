from fastapi import APIRouter
from pydantic import BaseModel

from app.src.main_driver import main

router = APIRouter()


class RetrieverRequest(BaseModel):
    class Config:
        extra = "allow"


@router.post("/stt")
async def retriever(request_data: dict):
    """
    Endpoint to retriever data using the main pipeline.

    Args:
        request_data: The request body containing JSON data.

    Returns:
        The result of the main function execution.
    """
    result = await main(**request_data)
    return result