# Project-Arya
Indic Accent Stress Analysis leveraging Speech and Environmental Noise Dynamics


## Performance comparison of different models to predict stress levels in audio

| Model                | Augmented Data | Test Accuracy | Spectrogram Images | MFCC  |
|----------------------|----------------|---------------|--------------------|-------|
| LSTM                 | No             | 75.00%        | No                 | Yes   |
| LSTM                 | Yes            | 80.90%        | No                 | Yes   |
| ResNet50             | Yes            | 77.04%        | Yes                | No    |
| ResNet50             | Yes            | 79.00%        | No                 | Yes   |
| EfficientNet B0      | Yes            | 75.60%        | Yes                | No    |
| EfficientNet B0      | Yes            | 75.04%        | No                 | Yes   |
| **Modified EdgeSpeechNet** | **Yes**  | **87.00%**    | **No**             | **Yes** |
| Modified CNN         | No             | 66.00%        | Yes                | No    |
| **Modified CNN**     | **Yes**        | **82.00%**    | **Yes**            | **Yes** |

