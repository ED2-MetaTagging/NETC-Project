from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from BackEnd.Python.s3upload import upload_to_aws
from BackEnd.Python.Image_Extraction import IteratePDF


app = Flask(__name__,template_folder='FrontEnd',static_folder='static')

#File key for upload form
app.config['SECRET_KEY'] = 'NETCFILEKEY'
app.config['UPLOAD_FOLDER'] = 'static/files'

#class functions

#Upload file form to upload files to flask
class UploadFileForm(FlaskForm):
    file = FileField("file", validators=[InputRequired()])
    submit = SubmitField("Upload File")


#routes to html pages

#initial page
@app.route('/', methods=['GET',"POST"])
def index():
    return render_template('index.html')

#Home Page
@app.route('/home')
def home():
    return render_template('index.html')

#PDF Upload page, form upload to AWS
@app.route('/PDF-upload', methods=['GET',"POST"])
def PDFupload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file

        IteratePDF (__file__)

        uploaded = upload_to_aws(__file__, 'netc-filestorage', 'File-Storage/' + secure_filename(file.filename)) #Upload to AWS

        return "File has been uploaded."
    return render_template('PDF-upload.html',form=form)

#Video Upload page, form upload to AWS
@app.route('/video-upload', methods=['GET',"POST"])
def videoupload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        uploaded = upload_to_aws(__file__, 'netc-filestorage', 'Video-File-Storage/' + secure_filename(file.filename)) #Upload to AWS
        return "Video File has been uploaded."
    return render_template('video-upload.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
