# Dockerfile para el servicio processing
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos dependencias básicas
RUN apt-get update && \
    apt-get install -y git build-essential libssl-dev libffi-dev python3-dev

# Clonamos el repositorio de Whisper
RUN git clone https://github.com/openai/whisper.git

# Cambiamos al directorio de Whisper
WORKDIR /app/whisper

# Instalamos las dependencias de Python para Whisper
RUN pip install --no-cache-dir -r requirements.txt

# Instalamos las dependencias de compilación para Whisper
RUN python setup.py install

# Copiamos los archivos de configuración o de entrada al contenedor
COPY . .

# Comando para ejecutar el procesamiento de audio con Whisper
CMD ["whisper", "transcribe", "--model", "base", "--task", "transcribe", "--language", "es", "--output_format", "vtt", "--output_dir", "/app/subtitles", "/app/videos/input.mp4"]