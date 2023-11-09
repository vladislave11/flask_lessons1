from flask import Flask, request
import sqlite3
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
@app.route("/order/", methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        pizza_name = request.form['pizza_name']
        pizza_count = request.form['pizza_count']
        address = request.form['address']
        phone_number = request.form['phone_number']
        with sqlite3.connect("sqlite_python_oderman.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO orders2 \
            (pizza_name,pizza_count,address,phone_number) VALUES (?,?,?,?)",
                           (pizza_name, pizza_count, address, phone_number))
            users.commit()
        return render_template("pizza.html")
    else:
        return render_template('order.html')


app.run(host="0.0.0.0", port=12320, debug=True)