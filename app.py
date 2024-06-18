from flask import Flask, render_template, redirect, url_for , request 
from werkzeug.utils import secure_filename 
# from werkzeug.datastructures import  FileStorage
import os
from PIL import Image
from rembg import remove 


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/upload'
@app.route("/", methods=['GET'])

def index():
    return render_template('index.html')

@app.route("/upload_proses", methods=['POST'])
def upload_proses():
    msg = ''
    if request.method == 'POST':
        f = request.files['upload_files']
        filename = app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename)
        try:
            f.save(filename)  
            names = 'output.png'
            input = Image.open(filename)
            output = remove(input)
            output.save(app.config['UPLOAD_FOLDER'] + '/' + names)
            return render_template('success.html')
        except:
            return render_template('failed.html', msg = filename)


if __name__ == '__main__':
    app.run(debug=True)
