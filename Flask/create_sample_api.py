from flask import Flask

app = Flask(__name__)

@app.route('/uma')
def index():
    return ("WELCOME PAGE..!")

# @app.route('/priyanka')
# def index():
#     return ("WELCOME PRIYANKA PAGE..!")

# @app.route('/shannu')
# def index():
#     return ("WELCOME SHANMUKHI PAGE..!")


if __name__ == "__main__":
    app.run()