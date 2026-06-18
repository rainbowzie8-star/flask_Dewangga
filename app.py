from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Halo! Ini web Flask pertama Dewangga!</h1>"

if __name__ == "__main__":
    app.run(debug=True)