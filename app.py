from flask import Flask, render_template, request, jsonify
from main import createImage
import hashImages
import os

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    flag = False
    return render_template('index.html', flag = flag)

@app.route('/generate', methods = ['POST', 'GET'])
def generate():
    if request.method == 'POST':
        number = request.form['number']
        eth = request.form['eth']
        createImage(int(number), int(eth))
        hists = os.listdir('static/bird_images')
        hists = ['bird_images/' + file for file in hists]
        return render_template('display.html', hists = hists)

@app.route('/hashImage', methods = ['POST', 'GET'])
def hashImage():
    if request.method == 'POST':
        offset = request.form['offset']
        path = os.listdir(os.path.join('static', 'bird_images'))
        for eachPath in path:
            hashImages.encode(os.path.join('static', 'bird_images', eachPath), offset)
        flag = True
        return render_template('index.html', flag = flag)

@app.route('/decode', methods = ['POST', 'GET'])
def decode():
    if request.method == 'POST':
        path = os.listdir(os.path.join('static', 'output'))
        if path:
            result = hashImages.decode(os.path.join('static', 'output', 'encoded_0.png'))
        return jsonify(offset = result, result = "deHashed")

if __name__ == '__main__':
    app.run(debug=True)