from flask import Flask

app = Flask(__name__)

@app.route("/<username>")
def index(username):
    return "My first web page.. on Sunday from {}".format(username)

if __name__ == "__main__":
    app.run()