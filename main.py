from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os


from podcast_generator import (
    generate_podcast_script_text,
    parse_script_to_segments,
    generate_and_combine_audio_from_segments
)
load_dotenv()
app = FastAPI()

class PodcastRequest(BaseModel):
    topic: str
    llm_model: str = "llama3-70b-8192"
    output_script_filename: str = "podcast_script.txt"
    output_audio_path: str = "podcast.mp3"

class PodcastResponse(BaseModel):
    message: str
    script_file: str
    audio_file: str

@app.post("/generate_podcast",response_model=PodcastResponse)
async def generate_podcast(req: PodcastRequest):
    try:
        script = generate_podcast_script_text(req.topic, req.llm_model)

        with open(req.output_script_filename, "w", encoding="utf-8") as f:
            f.write(script)

        segments = parse_script_to_segments(script)
        if not segments:
            raise HTTPException(status_code=500, detail="Script parsing failed")

        generate_and_combine_audio_from_segments(segments, req.output_audio_path)

        return {
            "message": "Podcast generated successfully.",
            "script_file": req.output_script_filename,
            "audio_file": req.output_audio_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))