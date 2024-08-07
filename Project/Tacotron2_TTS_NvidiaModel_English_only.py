'''
[Reperence]
https://m.blog.naver.com/ditajrj147/222855952939
'''

'''
[cmd]
pip install tacotron2
git clone https://github.com/NVIDIA/tacotron2.git
'''

import torch

#Tacotron2 Dataset load (만약 GPU가 없다면, 'cuda'부분을 지워야 함)
tacotron2 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tacotron2', model_math='fp16')
tacotron2 = tacotron2.to('cuda')
tacotron2.eval()

waveglow = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_waveglow', model_math='fp16')
waveglow = waveglow.remove_weightnorm(waveglow)
waveglow = waveglow.to('cuda')
waveglow.eval()

from IPython.display import Audio


# 오디오 저장
from scipy.io.wavfile import write

text = """
Smooth like butter Like a criminal undercover 
Gon' pop like trouble Breakin' into your heart like that Cool shade stunner 
Yeah I owe it all to my mother Hot like summer.
"""

utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tts_utils')
sequences, lengths = utils.prepare_input_sequence([text])

with torch.no_grad():
    mel, _, _ = tacotron2.infer(sequences, lengths)
    audio = waveglow.infer(mel)
audio_numpy = audio[0].data.cpu().numpy()
rate = 22050

write("audio.wav", rate, audio_numpy)
