# FastSpeech 2 English and Telugu TTS - Experiment Report

## 1. Objective
Implement and evaluate separate English and Telugu text-to-speech models, and analyze duration, pitch and energy predictions.

## 2. Implementation
The experiments use a simplified FastSpeech 2-inspired prototype, not a complete reproduction of the original FastSpeech 2 architecture.
Separate model checkpoints were trained for English and Telugu.
Each language dataset contains 100 processed samples.
Training was limited to 3 epochs per language.

## 3. Model Architecture
The prototype contains phoneme embeddings, an encoder, duration,pitch,energy predictors, pitch,energy embeddings, a duration-based length expansion operation, a decoder, and an 80-bin mel-spectrogram projection.

## 4. Telugu Adaptation
Telugu uses separate metadata, vocabulary, preprocessing outputs, training data and model checkpoints.
This is experimental Telugu support rather than a verified full Telugu phoneme-based FastSpeech 2 implementation.

## 5. Evaluation
Metrics below are calculated from the first processed sample of each language, not from a held-out test-set average.

### English

- Phoneme count: 76
- Mel frames: 755
- Duration MAE: 7.1912
- Duration RMSE: 7.1953
- Pitch MAE: 206.055
- Pitch RMSE: 213.4279
- Energy MAE: 0.0415
- Energy RMSE: 0.0502
- Generated audio: Results/English/english_generated.wav
- Comparison graph: Results/English/variance_comparison.png

### Telugu

- Phoneme count: 10
- Mel frames: 187
- Duration MAE: 15.8075
- Duration RMSE: 15.8142
- Pitch MAE: 171.4364
- Pitch RMSE: 186.4165
- Energy MAE: 0.0516
- Energy RMSE: 0.0585
- Generated audio: Results/Telugu/telugu_generated.wav
- Comparison graph: Results/Telugu/variance_comparison.png

## 6. Speech Generation
Predicted mel spectrograms were converted to WAV using librosa mel inversion with Griffin-Lim phase reconstruction.
A trained neural vocoder was not used in this generation step.
Speech intelligibility and naturalness have not been formally evaluated.

## 7. Limitations
- This model is a simplified prototype rather than full FastSpeech 2.
- Training used 100 samples and 3 epochs per language.
- Ground-truth durations were supplied during mel generation.
- Ground-truth pitch and energy were also supplied during mel generation.
- The generated audio is not fully independent text-to-speech inference.
- The evaluation covers one sample per language.
- No MOS listening study or comprehensive test-set evaluation was performed.

## 8. Conclusion
Separate English and Telugu models were trained and restored.
Mel predictions, WAV files, and duration,pitch,energy analyses were generated for both languages.
Further work requires a faithful FastSpeech 2 implementation, better alignment, more training data, longer training, and improved vocoder-based synthesis.
