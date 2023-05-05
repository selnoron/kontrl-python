from flask import Flask, redirect, url_for, render_template, request, session
from services.interface import *

app = Flask(__name__)
app.secret_key = "8374tgrdsf8sdf973d4gf873gt36fgd7"


# ---------------------------------------------
# Главная страница
# ---------------------------------------------
@app.route("/", methods=["GET"])
def main_page():
    if not session.get("login") is None:
        return render_template("views/index.html")
    return redirect(url_for("registration"))

# ---------------------------------------------
# Страница регистрации
# ---------------------------------------------
@app.route("/registration", methods=["GET"])
def registration():
    if not session.get("login") is None:
        return redirect(url_for("main_page"))
    return render_template("views/registration.html")


# ---------------------------------------------
# Страница авторизации
# ---------------------------------------------
@app.route("/authorization", methods=["GET"])
def authorization():
    if not session.get("login") is None:
        return redirect(url_for("main_page"))
    return render_template("views/authorization.html")


# ---------------------------------------------
# Страница деавторизации
# ---------------------------------------------
@app.route("/deauth", methods=["GET"])
def deauth():
    session.clear()
    return redirect(url_for("main_page"))

# ---------------------------------------------
# API's
# ---------------------------------------------
# ---------------------------------------------
# API регистрации
# ---------------------------------------------
@app.route("/api/v1/registration", methods=["GET", "POST"])
def registration_api():
    data = request.get_json()
    result_of_registration = registrate(data=data)
    return json.dumps(result_of_registration)

# ---------------------------------------------
# API авторизации 
# ---------------------------------------------
@app.route("/api/v1/authorization", methods=["GET", "POST"])
def authorization_api():
    data = request.get_json()
    result_of_authorization = authorize(data=data)
    return json.dumps(result_of_authorization)




if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )
