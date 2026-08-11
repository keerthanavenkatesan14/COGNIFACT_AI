from flask import Blueprint

from controllers.auth_controller import (
    register,
    login
)


auth_routes = Blueprint(
    "auth_routes",
    __name__,
    url_prefix="/api"
)


auth_routes.route(
    "/register",
    methods=["POST"]
)(register)


auth_routes.route(
    "/login",
    methods=["POST"]
)(login)