# English and Telugu TTS — FastSpeech 2-Inspired Prototype

## Project Overview

This project focuses on text-to-speech synthesis for English and Telugu using
separate simplified FastSpeech 2-inspired models.


## Model Components

- Phoneme embedding and encoder
- Duration predictor
- Pitch predictor
- Energy predictor
- Pitch and energy embeddings
- Duration-based sequence expansion
- Decoder and 80-bin mel-spectrogram projection

## Experiments

| Setting | English | Telugu |
|---|---|---|
| Processed samples | 100 | 100 |
| Training epochs | 3 | 3 |
| Separate checkpoint | Yes | Yes |
| Generated WAV | Yes | Yes |
| Variance analysis | Yes | Yes |

## Evaluation

Mean absolute errors on the first processed sample:

| Feature | English | Telugu |
|---|---:|---:|
| Duration | 7.1912 | 15.8075 |
| Pitch | 206.0550 | 171.4364 |
| Energy | 0.0415 | 0.0516 |

These metrics are not full test-set results.

## Generated Outputs

- `Results/English/english_generated.wav`
- `Results/Telugu/telugu_generated.wav`
- `Results/English/variance_comparison.png`
- `Results/Telugu/variance_comparison.png`
- `Results/English/evaluation_metrics.json`
- `Results/Telugu/evaluation_metrics.json`
- `Report/Final_Report.md`

## Implementation Notes

English and Telugu have different separate vocabularies, processed datasets,
and trained model checkpoints.

The model requires externally supplied phoneme durations for sequence
expansion. During mel generation, ground-truth durations, pitch, and
energy were provided.

Generated mel spectrograms were converted into WAV files using
Griffin-Lim-based mel inversion, not a trained neural vocoder.


## Limitations

- Simplified architecture rather than complete FastSpeech 2
- Small training datasets
- Only three training epochs
- No independent time-based inference
- Evaluation on one sample per language
- No formal speech quality assessment

## Project Files

The experiment notebook is `fastspeech.ipynb`.

See `Report/Final_Report.md` for methodology, results, and limitations.

## References

- FastSpeech 2: https://arxiv.org/abs/2006.04558
- FastSpeech 2 implementation: https://github.com/ming024/FastSpeech2
