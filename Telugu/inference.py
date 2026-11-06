from pathlib import Path

LANGUAGE = "Telugu"
ROOT = Path("/content/drive/MyDrive/FastSpeech2_Internship")

audio_dir = (
    ROOT / "Results" / LANGUAGE / "test_generated_audios"
)

files = sorted(audio_dir.glob("*.wav"))

print("Language:", LANGUAGE)
print("Generated WAV files:", len(files))

for file in files:
    print(file.name)

# Audio generation was performed in the original Colab notebook.
# This script lists the saved inference outputs.
