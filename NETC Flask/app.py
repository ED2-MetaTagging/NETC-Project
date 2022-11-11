from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from BackEnd.Python.s3upload import upload_to_aws
from BackEnd.Python.Image_Extraction import IteratePDF
import os
import fitz


app = Flask(__name__,template_folder='FrontEnd',static_folder='static')


BUCKET_NAME = 'netc-filestorage'

#routes to html pages

#initial page
@app.route('/', methods=['GET',"POST"])
def index():
    return render_template('index.html')

#Home Page
@app.route('/home')
def home():
    return render_template('index.html')

#PDF Upload page
@app.route('/PDF-upload')
def PDFupload():
    return render_template('PDF-upload.html')

#Upload to AWS
@app.route('/AWS-File-upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                uploaded = upload_to_aws(filename,BUCKET_NAME,'File-Storage/' + filename)
                msg = "Upload Done ! "

    #Opens file and runs Image Extraction, closes and removes file after
    pdf_file = fitz.open(os.path.dirname(__file__) + "\\" + filename)
    IteratePDF(pdf_file)
    pdf_file.close()
    os.remove(filename)

    return render_template("PDF-upload.html",msg =msg)

#Video Upload page
@app.route('/video-upload')
def videoupload():
    return render_template('video-upload.html')

#upload to AWS
@app.route('/AWS-Video-File-upload',methods=['post'])
def AWSVideoupload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                uploaded = upload_to_aws(filename,BUCKET_NAME,'Video-File-Storage/' + filename)
                msg = "Upload Done ! "

    os.remove(filename)

    return render_template("video-upload.html",msg =msg)


if __name__ == '__main__':
    app.run(debug=True)
