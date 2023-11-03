<h1 align="center">OpenAI Whisper Live Transcription</h1>

## What is Live-Subtitle-Whisper ?

Live-Subtitle-Whisper is an open-source project that focuses on enhancing the accessibility of audiovisual content in real-time. It utilizes state-of-the-art speech recognition technology to provide highly accurate transcriptions of spoken words.

## Project Overview

Live-Subtitle-Whisper has several key components that work together to achieve its goal:

1. **Audio Capture**: Python is employed to capture audio from a microphone continuously in 5-second segments. This audio is saved to a .wav file. For more informations check [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.6/) and [Wavio](https://github.com/WarrenWeckesser/wavio) docs.

2. **Parallel Processing**: A second function, executed using multiprocessing, reads the .wav file and processes it. For more informations check [Python Multiprocessing](https://docs.python.org/3/library/multiprocessing.html) doc.

3. **Whisper Speech Model**: The 'small' Whisper model, created by OpenAI, is loaded and used to generate text in French. For more informations check [Whisper](https://github.com/openai/whisper) doc.

4. **Translation**: The generated French text is then translated into another language using Google Translate. For more informations check [Deep Translator](https://github.com/prataffel/deep_translator) doc.

5. **Data Storage**: The translated text is saved in a JSON file for further usage. It can be loaded into a JavaScript file and displayed in an HTML `<p>` element.

## Development Team

| <img src="https://github.com/mickaelrebeau/MusicMate/assets/75978618/58703266-e28a-4e74-b104-341801a6d033" width="50"/> | Mike_DreeMan |
|:---:|:---:|

The development team of MusicMate consists of Mike_Dreeman, who is responsible for the development of the application. Mike_DreeMan has less than 2 years of experience and specializes in web development. He has worked on various projects, including the creation of a mobile application using React and Capacitor.

## Technologies Used

Live-Subtitle-Whisper relies on a variety of technologies to provide its functionality:

### Technologies

- Python: For audio capture and file processing.
- Whisper: Utilizing the 'small' Whisper model by OpenAI for speech recognition.
- JavaScript: For handling data and interacting with the HTML.
- HTML: Creating the user interface for displaying transcriptions.

Credit to https://github.com/hackingthemarkets/openai-whisper-live-transcription
