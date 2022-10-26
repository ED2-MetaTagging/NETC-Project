from flask import Flask, render_template

app = Flask(__name__,template_folder='Front End',static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/PDF-upload')
def PDFupload():
    return render_template('PDF-upload.html')

@app.route('/video-upload')
def videoupload():
    return render_template('video-upload.html')
