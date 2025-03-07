from app.src.stt_main.factory import STTFactory


async def main(**kwargs):
    """
    Asynchronous main driver function to process and transcribe audio using a
    specified STT processor.

    Args:
        **kwargs: Dictionary containing:
            - "stt_type" (str): The STT technique to use (e.g., "whisper",
                                "deepspeech").
            - "audio_data" (str): Base64-encoded audio data.
            - "audio_metadata" (dict): Metadata for the audio (e.g., sample
                                       rate, model name).

    Returns:
        str: The transcribed text.
    """
    try:
        stt_type = kwargs.get("stt_type", "whisper")  # Default to "whisper"
        audio_data = kwargs.get("audio_data")
        audio_metadata = kwargs.get("audio_metadata", {})

        if not audio_data:
            raise ValueError("Missing audio_data in kwargs")

        # Step 1: Create an STT processor using the factory
        stt_processor = STTFactory.create_stt_processor(
            stt_type,
            audio_data,
            audio_metadata,
        )

        # Step 3: Run transcription
        transcription = await stt_processor.transcribe()

        return transcription

    except Exception as e:
        return f"Error during STT processing: {e}"
