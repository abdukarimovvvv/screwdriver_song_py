from flask import Flask, render_template, request, redirect, flash, jsonify, send_from_directory
import os

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.secret_key = 'super_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.static_folder = 'static'

ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
        else:
            flash('Invalid file type: Only mp3, ogg, and wav files allowed')
            return redirect(request.url)
    else:
        return 'Method Not Allowed', 405


@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/list')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])

    data = []
    for i, f in enumerate(files, 1):
        data.append({"id": i, "name": f})

    return jsonify({"files": data})


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, port=8888)
