from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Cia mano pirmasis Flask puslapis</h1><br><h2>antra eilute</h2>'

if __name__ == '__main__':
    app.run(debug=True)