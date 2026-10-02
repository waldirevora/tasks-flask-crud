from flask import Flask

app = Flask(__name__) 

@app.route("/")
def hello_world():
    return "Hello Cape Verd!"

@app.route("/about")
def about():
    return "Página sobre."

if __name__ == "__main__":
    app.run(debug=True) # debug