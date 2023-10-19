from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder="templates", static_folder="static")

menus = [
    {"dishes": "Poultry", "price": 46},
    {"dishes": "Salami", "price": 51},
    {"dishes": "Sausage", "price": 92},
    {"dishes": "Beef", "price": 19},
    {"dishes": "Pepperoni", "price": 7},
]
@app.route("/")
@app.route("/index/")
def picture():
    context = {
        'pizzas': menus
    }
    return render_template("pizza.html", **context)







app.run(host="0.0.0.0", port=12320, debug=True)