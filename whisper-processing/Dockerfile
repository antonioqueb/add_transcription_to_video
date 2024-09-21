# Dockerfile para el servicio processing
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos dependencias básicas
RUN apt-get update && \
    apt-get install -y git build-essential libssl-dev libffi-dev python-dev

# Clonamos el repositorio de Whisper
RUN git clone https://github.com/openai/whisper.git

# Instalamos las dependencias de Python para Whisper

# Instalamos las dependencias de compilación para Whisper
RUN cd whisper && \
    python setup.py install

# Copiamos los archivos de configuración o de entrada al contenedor
COPY . .

# Comando para ejecutar el procesamiento de audio con Whisper
CMD ["whisper", "transcribe", "--model", "base", "--task", "transcribe", "--language", "es", "--output_format", "vtt", "--output_dir", "/app/subtitles", "/app/videos/input.mp4"]