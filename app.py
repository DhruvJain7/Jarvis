from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():

    return jsonify({"message": "AI response will be printed here"})


if __name__ == "__main__":
    app.run(debug=True)
