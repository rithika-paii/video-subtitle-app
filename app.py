from flask import Flask, request, jsonify
from flask_cors import CORS #import cors
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SUBTITLES_FOLDER'] = 'subtitles'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully'}), 200

# ... add create_subtitles and get_subtitles routes here ...

@app.route('/create_subtitles', methods=['POST'])
def create_subtitles():
    data = request.json
    video_id = data.get('video_id')
    subtitles = data.get('subtitles')

    if not video_id or not subtitles:
        return jsonify({'error': 'Invalid data'}), 400

    subtitle_filename = f'subtitles_{video_id}.srt'
    subtitle_filepath = os.path.join(app.config['SUBTITLES_FOLDER'], subtitle_filename)

    with open(subtitle_filepath, 'w') as f:
        for idx, subtitle in enumerate(subtitles, start=1):
            start_time = subtitle.get('start_time')
            end_time = subtitle.get('end_time')
            text = subtitle.get('text')
            f.write(f"{idx}\n{start_time} --> {end_time}\n{text}\n\n")

    return jsonify({'message': 'Subtitles created successfully'}), 200

@app.route('/get_subtitles/<video_id>', methods=['GET'])
def get_subtitles(video_id):
    subtitle_filename = f'subtitles_{video_id}.srt'
    subtitle_filepath = os.path.join(app.config['SUBTITLES_FOLDER'], subtitle_filename)

    if not os.path.exists(subtitle_filepath):
        return jsonify({'error': 'Subtitles not found'}), 404

    with open(subtitle_filepath, 'r') as f:
        subtitles = f.read()

    return subtitles, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['SUBTITLES_FOLDER'], exist_ok=True)
    app.run(debug=True)
