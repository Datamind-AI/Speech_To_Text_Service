import uvicorn
from fastapi import FastAPI

from app.api.router import router

app = FastAPI()
app.include_router(router)


@app.get("/status")
def status():
    """
    Endpoint to check the status of the application.

    Returns:
        dict: A dictionary containing the status message.
    """
    return {"status": "App is running healthy!"}


@app.get("/")
def index():
    """
    Root endpoint of the application.

    Returns:
        str: A string indicating the service name and version.
    """
    return "Retriever Service (0.1)"


if __name__ == "__main__":
    """
    Entry point for running the application using Uvicorn.

    Runs the FastAPI app on host 0.0.0.0 and port 8000.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)