from TTS.api import TTS

tts = TTS(model_name="tts_models/multispeaker/en/hf/vits", progress_bar=False, gpu=False)
print("Speakers:", tts.speakers)

tts.tts_to_file("Welcome to the podcast! I'm your host.", speaker="speaker_0", file_path="host.wav")
tts.tts_to_file("Glad to be here! I'm the guest.", speaker="speaker_3", file_path="guest.wav")
