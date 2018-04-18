from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from PIL import Image

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/result')

def result():


    return render_template('result.html')
