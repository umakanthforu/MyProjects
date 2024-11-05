from flask import Flask

app = Flask(__name__)

@app.route("/<int:name>") ## Converting given input to integer

def index(name):
    if name > 10:
        return "Given number is greater than 10"
    else:
        return "Given number is not greater than 10"

if __name__ == "__main__":
    app.run()