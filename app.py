from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file'] 
        f.save(f.filename) 
        return render_template('/Acknowledgement.html')
    return render_template('/home.html')

@app.route('/column', methods=['POST', 'GET'])
def column():
    return render_template('column.html')

@app.route('/process_data', methods=['POST', 'GET'])
def process():
    return render_template('process.html')

if __name__ == "__main__":
    app.run(debug=True)