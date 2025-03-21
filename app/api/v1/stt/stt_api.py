import logging

from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

from app.api.tasks import stt_task
from app.src.main_driver import main
from app.utils.callbackhandler import callback_task

router = APIRouter()

logger = logging.getLogger(__name__)


class STTRequest(BaseModel):
    audio_data: str  # The base64-encoded audio input
    callback: str = None  # Optional callback URL

    class Config:
        extra = "allow"


@router.post("/stt")
async def stt(request_data: STTRequest, background_tasks: BackgroundTasks):
    """
    Endpoint to transcribe audio using the STT pipeline,
    with optional background processing via Celery and callback support.

    Args:
        request_data (STTRequest): The request body containing audio and
                                   metadata.

    Returns:
        A message indicating task status or transcription result.
    """
    if request_data.callback:
        # Run STT in background via Celery
        task_result = stt_task.apply_async(kwargs=request_data.dict())

        # Add background callback trigger
        background_tasks.add_task(
            callback_task, request_data.callback, task_result
        )

        logger.info(
            (
                "STT task is processing in the background, callback will "
                "be used upon completion."
            )
        )

        return {
            "status": "STT task is processing in the background, callback will be used upon completion."  # noqa
        }

    else:
        try:
            result = await main(**request_data.dict())
            logger.info("STT processing successful.")
            return {
                "status": "Transcription successful",
                "text": result,
            }
        except Exception as e:
            logger.error("Failed to transcribe audio: %s", str(e))
            return {"status": "Failed to transcribe", "error": str(e)}
