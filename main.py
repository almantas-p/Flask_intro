from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    vardai = ['Juozas Juozaitis', 'Jonas Jonaitis', 'Petras Petraitis']
    return render_template('index.html', sarasas=vardai)

if __name__ == '__main__':
    app.run(debug=True)