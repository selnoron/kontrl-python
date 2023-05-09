from flask import Flask, redirect, url_for, render_template, request, session
from services.interface import *

app = Flask(__name__)
app.secret_key = "8374tgrdsf8sdf973d4gf873gt36fgd7"
search_key: str = ""


# ---------------------------------------------
# Главная страница со всеми компами
# ---------------------------------------------
@app.route("/", methods=["GET", "POST"])
def main_page():
    global search_key
    print(search_key)
    if not session.get("login") is None:
        if request.method == 'POST':
            data: dict = request.form
            result_of_carting = carte(data=data, user_login=session.get('login'))
            if result_of_carting == 0:
                return redirect(url_for("main_page"))
            request.method = "GET"
        if request.method == "GET":
            if search_key == "":
                return render_template("views/index.html", pcs=all_pcs())
            else:
                pcs: list[tuple] = []
                for pc in all_pcs():
                    if pc[3] == search_key:
                        pcs.append(pc)
                    print(pc[3])
                return render_template("views/index.html", pcs=pcs)
    return redirect(url_for("registration"))


# ---------------------------------------------
# Страница добавления компьютера
# ---------------------------------------------
@app.route("/addbook", methods=["GET"])
def comp_page():
    if not session.get("login") is None:
        return render_template("views/add_comp.html")
    return redirect(url_for("registration"))

# ---------------------------------------------
# Страница поиска
# ---------------------------------------------
@app.route("/search", methods=["GET", "POST"])
def search_page():
    global search_key
    if not session.get("login") is None:
        if request.method == "POST":
            print(request.form.get('search'))
            search_key = request.form.get('search')
            return redirect(url_for("main_page"))
        return render_template('views/search.html')
    return redirect(url_for("registration"))

# ---------------------------------------------
# Страница корзины
# ---------------------------------------------
@app.route("/cart", methods=["GET", "POST"])
def cart_page():
    if not session.get("login") is None:
        if len(all_user_carts(data=session.get('login'))) == 0:
            return redirect(url_for("main_page"))
        if request.method == 'POST':
            print(request.form.get('id'))
            result_of_delete = delete_cart(request.form.get('id'))
            if result_of_delete == 0:
                return redirect(url_for("main_page"))
        return render_template("views/cart.html", carts=all_user_carts(data=session.get('login')))
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


# ---------------------------------------------
# API авторизации 
# ---------------------------------------------
@app.route("/api/v1/computering", methods=["GET", "POST"])
def computering_api():
    data = request.get_json()
    result_of_computering = compit(data=data)
    return json.dumps(result_of_computering)


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )
