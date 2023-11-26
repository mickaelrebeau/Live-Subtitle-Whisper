FROM python:3.11

# Path: /app
WORKDIR /app

COPY . .

# Update
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y portaudio19-dev python3-pyaudio

# Install dependencies with pip
RUN pip install sounddevice
RUN pip install wavio
RUN pip install deep_translator

# Install dependencies with apt-get
RUN apt install ffmpeg -y

# Open-Ai Whisper
RUN pip install openai-whisper --no-cache-dir

# Run the python script
CMD ["python", "main.py"]
