from flask import Flask, render_template
import util.network
import time

app = Flask(__name__)


@app.route("/")
def home():
    reload = time.time()
    return render_template("index.html", reload=reload)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
