
import cv2
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from flask import render_template
from flask import Flask
app = Flask(__name__)



UPLOAD_FOLDER = '/Users/assimaddous/jobs_project/python_opencv/storage'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def inputView():
    return render_template('input.html')


@app.route('/results')
def outputView():
    return render_template('input.html')

