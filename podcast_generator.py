import argparse
import os
from dotenv import load_dotenv
from pydub import AudioSegment
from gtts import gTTS
import requests

# Load environment variables
load_dotenv() 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DEFAULT_MODEL = "llama3-70b-8192"
DEFAULT_SCRIPT_FILE = "podcast_script.txt"
DEFAULT_AUDIO_FILE = "podcast.mp3"


def generate_script_groq(topic, llm_model):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        f"Write a podcast with exactly 3 exchanges from HOST and 3 from GUEST on the topic: '{topic}'.\n"
        "Use this format:\nHOST: ...\nGUEST: ...\nHOST: ...\nGUEST: ...\nHOST: ...\nGUEST: ..."
    )

    data = {
        "model": llm_model,
        "messages": [
            {"role": "system", "content": "You are a helpful podcast scriptwriter."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print("Failed to parse Groq response")
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        raise e


def parse_script(script):
    lines = script.strip().split("\n")
    parsed = []
    for line in lines:
        if line.startswith("HOST:"):
            parsed.append(("host", line[5:].strip()))
        elif line.startswith("GUEST:"):
            parsed.append(("guest", line[6:].strip()))
    return parsed


def generate_audio_gtts(text, filename):
    tts = gTTS(text)
    tts.save(filename)
    return AudioSegment.from_file(filename, format="mp3")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--output_script_file", default=DEFAULT_SCRIPT_FILE)
    parser.add_argument("--output_audio_file", default=DEFAULT_AUDIO_FILE)
    parser.add_argument("--llm_model", default=DEFAULT_MODEL)
    args = parser.parse_args()
    print("Starting AI Podcast Generation...")

    print("Generating script...")
    script = generate_script_groq(args.topic, args.llm_model)
    with open(args.output_script_file, "w", encoding="utf-8") as f:
        f.write(script)

    print("Parsing script...")
    parsed = parse_script(script)

    print("Converting to audio...")
    full_audio = AudioSegment.silent(duration=1000)
    temp_files = []

    for i, (speaker, line) in enumerate(parsed):
        print(f"{speaker.upper()} says: {line}")
        temp_filename = f"temp_{speaker}_{i}.mp3"
        audio = generate_audio_gtts(line, temp_filename)
        full_audio += audio + AudioSegment.silent(duration=500)
        temp_files.append(temp_filename)

    print("Saving audio to", args.output_audio_file)
    full_audio.export(args.output_audio_file, format=args.output_audio_file.split(".")[-1])

    # Optional cleanup
    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)

    print("Done!")


if __name__ == "__main__":
    main()
