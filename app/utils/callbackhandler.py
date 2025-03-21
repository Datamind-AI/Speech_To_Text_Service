import httpx


async def callback_task(callback_url: str, task_result):
    """
    Make a GET request to the callback URL with success or failure status.
    """
    try:
        # Check if the task was successful
        if task_result.status == "SUCCESS":
            status = "success"
        else:
            status = "fail"

        async with httpx.AsyncClient() as client:
            await client.get(f"{callback_url}?status={status}")
    except Exception as e:
        print(f"Error while calling callback: {e}")
