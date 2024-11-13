from flask import Flask, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import random
import string

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gif', 'jpg', 'jpeg', 'png', 'heif'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(file):
    return (
        '.' in file.filename and 
        file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS and
        file.mimetype in ['image/gif', 'image/jpeg', 'image/png', 'image/heif']
    )

def generate_filename(extension):
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f"{timestamp}_{random_str}.{extension}"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file and allowed_file(file):
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            if file_size > MAX_CONTENT_LENGTH:
                return "File too large", 413
            
            file.seek(0)
            extension = file.filename.rsplit('.', 1)[1].lower()
            filename = secure_filename(generate_filename(extension))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # 自動偵測並生成當前域名的完整圖片連結
            file_url = url_for('uploaded_file', filename=filename, _external=True)
            return file_url
    return send_from_directory('templates', 'upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=False)
