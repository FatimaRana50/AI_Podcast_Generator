🎙️ AI Podcast Generator
A powerful tool that leverages LLMs (via Groq API), gTTS, and FastAPI to generate podcast scripts and corresponding audio on any topic. Perfect for content creators, educators, and podcast enthusiasts!

https://images/p-5.PNG
https://images/p-6.PNG

🌟 Features
AI-Powered Script Generation: Uses state-of-the-art LLMs (like LLaMA3-70B) to create natural podcast dialogues

Text-to-Speech Conversion: Converts generated scripts into high-quality audio using gTTS

REST API Interface: Easy integration with other applications via FastAPI

Customizable Output: Control over script length, speakers, and output formats

Fast Processing: Generates complete podcast episodes in minutes

📦 Project Structure
text
.
├── images/                  # Screenshots for documentation
│   ├── p-5.PNG
│   └── p-6.PNG
├── podcast_generator.py     # Core podcast generation logic
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
├── .env                     # Environment configuration
└── README.md                # This documentation
🚀 Quick Start
Prerequisites
Python 3.8+

Groq API key (free tier available)

FFmpeg (for audio processing)

Installation
Clone the repository

bash
git clone https://github.com/yourusername/ai-podcast-generator.git
cd ai-podcast-generator
Set up virtual environment (recommended)

bash
```
python -m venv venv
`
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```
Install dependencies

bash
```
pip install -r requirements.txt
```
Configure environment variables
Create a .env file with:

env
GROQ_API_KEY=your_groq_api_key_here
🏃 Running the Application
Start the FastAPI server:

bash
```
uvicorn main:app --reload
```
Access the interactive API docs at:

```
http://127.0.0.1:8000/docs
```
📡 API Endpoints
POST /generate_podcast
Generates a podcast script and audio file on the given topic.

Request Body:
```
json
{
  "topic": "The Future of AI in Education",
  "llm_model": "llama3-70b-8192",
  "output_script_filename": "ai_education_script.txt",
  "output_audio_path": "ai_education_podcast.mp3",
  "num_exchanges": 5
}
```
Parameters:

topic (required): Subject for the podcast

llm_model: Groq model to use (default: "llama3-70b-8192")

output_script_filename: Script output path (default: "podcast_script.txt")

output_audio_path: Audio output path (default: "podcast.mp3")

num_exchanges: Number of host/guest exchanges (default: 3)

Successful Response:
```
json
{
  "message": "Podcast generated successfully.",
  "script_file": "ai_education_script.txt",
  "audio_file": "ai_education_podcast.mp3",
  "generation_time": 45.2
}
```
� How It Works
Script Generation:

The system prompts the LLM to create a podcast dialogue with specified number of exchanges

Output is formatted with clear speaker labels (HOST/GUEST)

Audio Production:

Script is parsed into individual speaker segments

Each segment is converted to speech using gTTS

Audio segments are merged with smooth transitions

Final mix is saved as MP3

Output Delivery:

Text script saved to specified file

Audio file saved to specified path

API returns paths to generated files

🛠️ Dependencies
See requirements.txt for complete list:

fastapi: Web framework for the API

uvicorn: ASGI server

python-dotenv: Environment variable management

gTTS: Google Text-to-Speech interface

pydub: Audio processing

requests: HTTP requests for Groq API

📚 Example Use Cases
Content Creation: Quickly generate podcast episodes on trending topics

Education: Create learning materials in podcast format

Prototyping: Test podcast concepts before recording

Accessibility: Generate audio content from text topics

🤝 Contributing
Contributions are welcome! Please open an issue or PR for:

Bug fixes

Additional features

Documentation improvements

📜 License
MIT License
