from flask import Flask

app = Flask(__name__)

@app.route("/<myname>")
def dyn_name(myname):
    return "Hi There, How are you {}. This is the first webpage.".format(myname)

if __name__ == "__main__":
    app.run()