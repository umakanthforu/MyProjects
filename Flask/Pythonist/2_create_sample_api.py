## importing flask package and utisling Flask class
from flask import Flask


## creating an instance of Flask by passing argument "__name__", which can be name of package or function.
app = Flask(__name__)

## creating a route for Webserver Gateway Interface to follow the path
@app.route('/uma')

##creating a view function for the path accessed
def index():
    return ("WELCOME PAGE..!")

## creating programatic run to application
if __name__ == "__main__":
    app.run()