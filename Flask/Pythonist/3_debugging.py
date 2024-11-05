from flask import Flask

app = Flask(__name__)

@app.route("/<username>")
def index(username):
    return "My edited web page.. on Sunday from {}".format(username)

if __name__ == "__main__":
    app.run(debug=True) # debug = True to enable debug mode
