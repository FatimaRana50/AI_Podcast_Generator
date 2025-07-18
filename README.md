🎙️ AI Podcast Generator
This project uses LLMs (via Groq API), gTTS, and FastAPI to generate a podcast script and corresponding audio on any topic you choose. You can interact with the service through a REST API powered by FastAPI.

📁 Project Structure

.
├── images/
│   ├── p-5.PNG
│   └── p-6.PNG
├── podcast_generator.py
├── main.py
├── requirements.txt
├── .env
└── README.md
⚙️ Setup Instructions
1. ✅ Clone the Repository
```
git clone https://github.com/yourusername/ai-podcast-generator.git
cd ai-podcast-generator
```
2. 🐍 Create Virtual Environment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```
3. 📦 Install Dependencies
```
pip install -r requirements.txt
```
4. 🔐 Configure Environment Variables
Create a .env file in the root directory with the following content:


GROQ_API_KEY=your_groq_api_key_here
Replace your_groq_api_key_here with your actual API key from Groq.

🚀 Running the Application
Use uvicorn to start the FastAPI server:

```
uvicorn main:app --reload
```
Once running, visit: http://127.0.0.1:8000/docs

🔄 Using the API
▶️ POST /generate_podcast
Request Body:

```
{
  "topic": "Mental Health in Teens",
  "llm_model": "llama3-70b-8192",
  "output_script_filename": "podcast_script.txt",
  "output_audio_path": "podcast.mp3"
}
```
Response:

```
{
  "message": "Podcast generated successfully.",
  "script_file": "podcast_script.txt",
  "audio_file": "podcast.mp3"
}
```
📷 Screenshots
✅ API Test in Swagger UI
<p align="center"> <img src="images/p-5.PNG" width="600" alt="API Input"> </p> <p align="center"> <img src="images/p-6.PNG" width="600" alt="API Output"> </p>
📦 requirements.txt
```
openai
elevenlabs
pydub
python-dotenv
argparse
requests
TTS
fastapi
uvicorn
pydantic
```
🧠 How It Works
You send a topic via POST request to /generate_podcast.

The app calls Groq API (e.g., llama3-70b) to generate a podcast script with 3 exchanges between HOST and GUEST.

The script is parsed into speaker segments.

The gTTS library generates speech for each line.

The speech clips are merged into one podcast audio file.
