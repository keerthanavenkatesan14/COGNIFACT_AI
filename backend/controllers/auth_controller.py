from flask import request, jsonify

from services.auth_service import AuthService


auth_service = AuthService()


# ==========================================
# REGISTER CONTROLLER
# ==========================================

def register():

    data = request.get_json()

    if not data:

        return jsonify({
            "message": "Invalid request"
        }), 400

    try:

        success, result = auth_service.register(data)

        if not success:

            return jsonify({
                "message": result
            }), 400

        return jsonify({
            "message": result
        }), 201

    except Exception as e:

        print("REGISTER ERROR:", e)

        return jsonify({
            "message": "Registration failed"
        }), 500


# ==========================================
# LOGIN CONTROLLER
# ==========================================

def login():

    data = request.get_json()

    if not data:

        return jsonify({
            "message": "Invalid request"
        }), 400

    email = data.get("email", "")
    password = data.get("password", "")

    if not email or not password:

        return jsonify({
            "message": "Email and password are required"
        }), 400

    try:

        success, result = auth_service.login(
            email,
            password
        )

        if not success:

            return jsonify({
                "message": result
            }), 401

        return jsonify({
            "message": "Login successful",
            "token": result["token"],
            "user": result["user"]
        }), 200

    except Exception as e:

        print("LOGIN ERROR:", e)

        return jsonify({
            "message": "Login failed"
        }), 500