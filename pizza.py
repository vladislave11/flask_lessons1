from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static")





app.run(host="0.0.0.0", port=12320, debug=True)