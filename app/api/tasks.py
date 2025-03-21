import asyncio

from app.api.worker import celery
from app.src.main_driver import main  # This is your STT main function


@celery.task(name="app.api.tasks.stt_task")
def stt_task(**kwargs):
    """
    Celery task to run the STT pipeline.
    """
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main(**kwargs))
