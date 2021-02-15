from flask import Flask
from flask_login import LoginManager

import views
from database import Database
from product import Product
from user import *

lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule(
        "/",
        view_func=views.home_page
    )
    app.add_url_rule(
        "/login",
        view_func=views.login_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/logout",
        view_func=views.logout_page
    )
    app.add_url_rule(
        "/products",
        view_func=views.products_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/products/<int:product_key>",
        view_func=views.product_page
    )
    app.add_url_rule(
        "/products/<int:product_key>/edit",
        view_func=views.product_edit_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/add-product",
        view_func=views.product_add_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/users",
        view_func=views.users_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/users/<int:user_key>",
        view_func=views.user_page
    )
    app.add_url_rule(
        "/users/<int:user_key>/edit",
        view_func=views.user_edit_page,
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/sign-in",
        view_func=views.sign_in_page,
        methods=["GET", "POST"]
    )

    lm.init_app(app)
    lm.login_view = "login_page"

    db = Database("postgreSQL")
    app.config["db"] = db
    
    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 8080)
    app.run(host="127.0.0.1", port=port)