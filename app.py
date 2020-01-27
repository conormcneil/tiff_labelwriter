import os
from flask import Flask, request, render_template, url_for, flash, session, redirect, send_file
from werkzeug.utils import secure_filename
from labelwriter import process
from UploadManager import UploadManager

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UploadManager().get_uploadfolder()
app.secret_key = b'C\n\xe4\x14?\xe5\x94\xa0\x7f\x17\x19Ej\x02l\x9e'

@app.route("/", methods=["GET"])
def root():
    return render_template('upload_form.html')

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        flash("GET /upload: You shouldn't be here.")
        return redirect("/")
    else:
        if 'file' not in request.files:
            flash("no file present")
            return redirect('/')
        file = request.files['file']
        uploader = UploadManager(file)
        if file.filename == '':
            flash("no file selected")
            return redirect('/')
        if file and uploader.allowed_file(file.filename):
            file.save(uploader.get_fullpath())
            process(uploader.get_basename(), request.form)
            return send_file(uploader.get_labelpath())