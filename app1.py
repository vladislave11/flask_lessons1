from flask import Flask, url_for, request, send_file, abort, redirect
from flask import render_template
from datetime import datetime
import random as r

app = Flask(__name__, template_folder="templates", static_folder="static")


# list = ["Сьогодні вас чекає гарний день", "У вас буде поповнення бюджету", "В вас заберуть квартиру", "Вас чекає радісна звістка"]


list1 = ["Сьогодні", "Завтра", "Незабаром"]
list2 = ["Ви отримаєте", "Ви дізнаєтесь", "Вас очікує", "Буде"]
list3 = ["Гарну звістку", "Приємну новину", "Погану звістку", "Лист від тцк"]

max_core = 100
test_name = "Python Challenge"
student = [
    {"name": "Vlad", "score": 100},
    {"name": "Jack", "score": 22},
    {"name": "Vadim", "score": 37},
    {"name": "Vova", "score": 11},
    {"name": "David", "score": 87},
    {"name": "Danil", "score": 46},
    {"name": "Kirill", "score": 51},
    {"name": "Misha", "score": 92},
    {"name": "Katya", "score": 19},
    {"name": "John", "score": 7},


]

@app.route("/result/")
def results(max_core=100):
    context = {
        "title": "Results",
        "students": student,
        "test_name": test_name,
        "max_score": max_core
    }
    student.append({"name": "Katya zi lvova", "score": 19})
    return render_template("results.html", **context)


@app.route("/")
def index():
    return render_template("base.html", title="San Francisco")


@app.route("/login.html")
def send_login():
    return send_file("templates/login.html")


@app.route("/login", methods = ("POST", "GET"))
def login():
    if request.method == "POST":
        user = request.form["name"]
        return f"Запит метода POST, name =  {user}"
    else:
        user = request.args.get("name")
        return f"Запит метода GET, name =  {user}"


@app.route("/hello")
def hello():
    return "Good day today" + str(datetime.now())


@app.route("/horoskope2/")
def horoskope():
    return f"{r.choice(list1)} {r.choice(list2)} {r.choice(list3)}"

@app.route("/url_for_test/")
def url_for_test():
    return url_for("horoskope")


@app.route("/redirect-to-login-page")
def redirected():
    return redirect(url_for("send_login"))

def this_is_never_executed():
    pass

@app.route("/aborted_page")
def aborted_page():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return"такої сторінки не знайдено", 404


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("hello"))
    print(url_for("horoskope"))


app.run(host="0.0.0.0", port=12320, debug=True)