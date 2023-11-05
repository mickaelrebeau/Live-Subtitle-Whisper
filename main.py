import io
import numpy as np
import sounddevice as sd
import whisper
import multiprocessing
import json
import logging
from deep_translator import GoogleTranslator


def record(connexion):
    freq = 44100
    duration = 5

    print('Recording')
    
    while True:
        # Start recorder with the given values of duration and sample frequency
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

        sd.wait()

        # Convert the NumPy array to audio file
        print('Converting to wav...')
        
        buffer = io.BytesIO()
        buffer.write(recording.tobytes())
        connexion.send(buffer.getvalue())

def transcribe(connexion):
    model = whisper.load_model("base")

    while True:
        buffer = connexion.recv()
    
        bufferFloatArray = whisper.load_audio(buffer)
        audio = whisper.pad_or_trim(bufferFloatArray)
        
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(language= 'fr', fp16=False)
        result = whisper.decode(model, mel, options)
        if result.text != '.':
            print(result.text)
            
            translated = GoogleTranslator(source='fr', target='en').translate(result.text)

            f = open("recording.json","w",encoding="utf-8")
            text = {"text": translated}
            f.write(json.dumps(text))
            f.close()

if __name__ == '__main__':
    to_mic, to_whisper = multiprocessing.Pipe()
    mic = multiprocessing.Process(target=record , args=(to_whisper, ))
    whisp = multiprocessing.Process(target=transcribe , args=(to_mic, ))
    mic.start()
    whisp.start()
    mic.join()
    whisp.join()