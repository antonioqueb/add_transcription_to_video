from flask import Flask, request, send_from_directory, render_template
import os
import docker
import time

app = Flask(__name__)

# Configuración de Docker
client = docker.from_env()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No video part', 400
    file = request.files['video']
    if file.filename == '':
        return 'No selected video', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Procesar el video y generar subtítulos
        process_video(filename)
        return 'Video uploaded and processed successfully!'

def process_video(filename):
    # Aquí puedes llamar a un script o función que use docker-compose para procesar el video
    pass

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)