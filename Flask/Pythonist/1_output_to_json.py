from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Team.. Welcome to our API page."

@app.route("/<int:num>")
def calculation(num):
    if num >= 10:
        result = {
            "Number" : num,
            "Greater": True,
            "Condition" : "Satisfied",
            "Odd Numbers": [1, 3, 5, 7, 9]
        }
    else:
        result = {
            "Number" : num,
            "Greater": False,
            "Condition" : "Not Satisfied",
            "Even Numbers": [2, 4, 6, 8, 10]
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)