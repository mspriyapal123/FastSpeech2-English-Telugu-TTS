import os
import json
import torch

# Run after loading the dataset and model definitions
# from the original Google Colab training notebook.

LANGUAGE = "English"
ROOT = "/content/drive/MyDrive/FastSpeech2_Internship"

checkpoint_path = os.path.join(
    ROOT, LANGUAGE, "checkpoints",
    "english_latest.pth"
)

checkpoint = torch.load(
    checkpoint_path,
    map_location="cpu",
    weights_only=True
)

print("Language:", LANGUAGE)
print("Completed epochs:", checkpoint["epoch"])
print("Training history:", checkpoint["history"])
