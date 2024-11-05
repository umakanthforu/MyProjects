from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<int:num>")
def greater(num):
    if num > 10:
        result = {
            "Number": num,
            "Condition": True,
            "Description" : "Given number is greater than 10"
        }
    else:
        result = {
            "Number": num,
            "Condition": False,
            "Description" : "Given number is not greater than 10"
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)