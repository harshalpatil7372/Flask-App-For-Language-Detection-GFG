# importing the Packages

from flask import Flask, render_template, url_for, request

import textblob

from textblob import TextBlob

# Create our Flask instance

app = Flask(__name__)

# Set Home Page Template as starter

@app.route('/')
def home():
	return render_template('home.html')

# Set the predict for dectection purpose Using TextBlob package

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        message = request.form['message']
        blobline = TextBlob(message)
        detect = blobline.detect_language()
    return render_template('result.html',prediction = detect)

if __name__ == '__main__':
	app.run(debug=True)