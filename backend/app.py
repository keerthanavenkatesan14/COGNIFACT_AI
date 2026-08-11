from flask import Flask, jsonify

from flask_cors import CORS

from routes.auth_routes import auth_routes


app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_routes)

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "status":
            "CogniFact AI backend is running"
    })

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )