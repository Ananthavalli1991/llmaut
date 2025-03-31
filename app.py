from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def answer_question():
    data = request.form.get("question", "No question provided")
    return jsonify({"answer": f"Processed: {data}"})

# Vercel requires this:
def handler(request, *args, **kwargs):
    return app(request.environ, start_response)
