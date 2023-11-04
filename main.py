import sounddevice as sd
import wavio as wv
import whisper
import multiprocessing
import os
import redis
import json
from deep_translator import GoogleTranslator


def record():
    freq = 44100
    duration = 5

    print('Recording')
    
    while True:
        # Start recorder with the given values of duration and sample frequency
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

        sd.wait()

        # Convert the NumPy array to audio file
        print('Converting to wav...')
        wv.write("recording.wav", recording, freq, sampwidth=2)

def transcribe():
    model = whisper.load_model("small")

    while True:
        audio = whisper.load_audio("recording.wav")
        audio = whisper.pad_or_trim(audio)
        
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
    mic = multiprocessing.Process(target=record)
    whisp = multiprocessing.Process(target=transcribe)
    mic.start()
    whisp.start()
    mic.join()
    whisp.join()