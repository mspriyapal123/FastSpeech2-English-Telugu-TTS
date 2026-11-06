from pathlib import Path
import csv

LANGUAGE = "Telugu"
ROOT = Path("/content/drive/MyDrive/FastSpeech2_Internship")
processed = ROOT / LANGUAGE / "processed"

with open(processed / "metadata.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Language:", LANGUAGE)
print("Processed samples:", len(rows))
print("Mel files:", len(list((processed / "mels").glob("*.npy"))))
print("Feature files:", len(list((processed / "features").glob("*.npz"))))

# Original preprocessing was executed in Google Colab.
# This script verifies the saved preprocessing outputs.
