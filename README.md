# Project-Arya
Indic Accent Stress Analysis leveraging Speech and Environmental Noise Dynamics

Our findings indicate that low-footprint custom deep neural network models, which are computationally efficient, have outperformed existing complex architectures like ResNet-50, RNN and EfficientNet in stress level classification. These models can be utilized in real-time consumer devices due their computational efficiency, offering better accuracy than existing models while being computationally less expensive.

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


## Future work 
We will be improving the results given by our transformer model pipeline

<br/>
<img src="https://i.ibb.co/4ZfWSzL/transformer.png" width="512">
