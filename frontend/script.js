async function generatePodcast() {
  const topic = document.getElementById('topicInput').value;
  if (!topic) {
    alert('Please enter a topic!');
    return;
  }

  const response = await fetch('http://127.0.0.1:8000/generate_podcast/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic: topic })
  });

  if (!response.ok) {
    alert('Error generating podcast');
    return;
  }

  const data = await response.json();

  // Display script file name (you can choose to display contents if needed)
  document.getElementById('scriptOutput').innerText = `Script saved as: ${data.script_file}`;

  // Play audio
  const audioUrl = 'http://127.0.0.1:8000/audio/' + data.audio_file;
  const audioPlayer = document.getElementById('audioPlayer');
  audioPlayer.src = audioUrl;
  audioPlayer.load();

  // Set download links
  const downloadScript = document.getElementById('downloadScript');
  const downloadAudio = document.getElementById('downloadAudio');

  // Link to script file (served from /files/)
  const scriptUrl = 'http://127.0.0.1:8000/files/' + data.script_file;
  downloadScript.href = scriptUrl;
  downloadScript.download = data.script_file;

  // Link to audio file
  downloadAudio.href = audioUrl;
  downloadAudio.download = data.audio_file;
}
