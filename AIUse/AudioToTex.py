import whisper

# 🎧 Whisper मॉडल लोड करें
model = whisper.load_model("base")

# 📂 अपनी MP3 फाइल का नाम या path यहां लिखो
result = model.transcribe("HumPadhaiyaKarbe.mp3", language="hi")

# 📝 ट्रांसक्राइब किया गया टेक्स्ट प्रिंट करें
print("\n📄 Transcribed Hindi Text:\n")
print(result["text"])
