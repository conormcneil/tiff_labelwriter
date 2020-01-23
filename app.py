import os
from osgeo import gdal
from flask import Flask, request, render_template, url_for, flash, session, redirect, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "tmp/"
ALLOWED_EXTENSIONS = {'txt', 'csv', 'tif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'C\n\xe4\x14?\xe5\x94\xa0\x7f\x17\x19Ej\x02l\x9e'

@app.route("/", methods=["GET"])
def root():
    return render_template('upload_form.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    filename = secure_filename(file.filename)
    savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(savepath)

def make_options(form):
    options = []
    for key, value in form.items():
        options.append('-co')
        options.append(key + '=' + value)
    return options

def run_gdal(filename, src_path, translate_options):
    ds = gdal.Open( filename )
    ds = gdal.Translate(src_path + '.xml', ds, options = translate_options)

def sendlabelfile(src_path):
    return send_file( src_path + ".xml" )

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
        if file.filename == '':
            flash("no file selected")
            return redirect('/')
        if file and allowed_file(file.filename):
            src_full = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            
            src_name = os.path.splitext(file.filename)[0]
            src_path = os.path.join(app.config['UPLOAD_FOLDER'], src_name)

            save_file(file)
            run_gdal(src_full, src_path, gdal.TranslateOptions( format = "PDS4", options = make_options(request.form) ))

            flash("PDS4 label generated.")

            return sendlabelfile(src_path)