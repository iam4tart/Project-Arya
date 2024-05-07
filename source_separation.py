import torch
import torchaudio
import numpy as np
import scipy
import stempeg
import os
import scipy.io.wavfile as wav
import librosa
import librosa.display
import IPython.display as ipd
from IPython.display import Audio, display
import noisereduce as nr
from openunmix import predict


use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

feature_audio = "/content/GF_Scene.wav"
audio, rate = librosa.load(feature_audio)
rate = rate
ipd.Audio(audio, rate=rate)

estimates = predict.separate(
    torch.as_tensor(audio).float(),
    rate=rate,
    device=device
)

view_rate = rate*2
speech = []
environment = []

estimates = predict.separate(
    torch.as_tensor(audio).float(),
    rate=rate,
    targets=['vocals'],
    residual=True,
    device=device,
)

for target, estimate in estimates.items():
    print(target)
    display(Audio(estimate.detach().cpu().numpy()[0], rate=view_rate))
    
for target, estimate in estimates.items():
  if target=="vocals":
    speech = estimate.detach().cpu().numpy()[0]
  if target=="residual":
    environment = estimate.detach().cpu().numpy()[0]
  else:
    continue

speech = nr.reduce_noise(y=speech, sr=view_rate)
display(Audio(speech, rate=view_rate))