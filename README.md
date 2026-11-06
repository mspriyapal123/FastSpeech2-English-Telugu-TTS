# English and Telugu FastSpeech2-Style TTS Prototype

## Project Overview
This project implements a FastSpeech2-style text-to-speech
prototype for English and Telugu language.

## Dataset
- English: 100 samples from ai4bharat/Svarah
- Telugu: 100 samples from SPRINGLab/IndicTTS_Telugu
- Training samples: 90 per language
- Validation samples: 10 per language

## Model
- Phoneme embedding
- Transformer encoder
- Duration, pitch and energy predictors
- Duration-based length regulator
- Transformer decoder
- Mel-spectrogram projection


## Training
- 3 epochs per language
- CPU execution
- Adam optimizer, learning rate 0.001
- Batch size 1
- 80-bin log-mel spectrograms

## Results
Results-English and Results-Telugu contain:
- Training and validation loss graphs
- Five generated test WAV files per language
- Duration, pitch and energy prediction plots

Audio is reconstructed with Griffin-Lim rather than a neural vocoder.

## Limitations
- Small dataset
- Approximate phoneme durations rather than forced alignment
- No neural vocoder
- No formal MOS or intelligibility evaluation

## Checkpoints
English/checkpoints/english_latest.pth
Telugu/checkpoints/telugu_latest.pth

## Reproducibility
Install requirements and use the language-specific scripts and
the original Google Colab notebook.
