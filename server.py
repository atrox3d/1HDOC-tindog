from flask import Flask, render_template
import util.network
import time
import pprint
from os import walk
import pathlib


app = Flask(__name__)
print(app.url_map.strict_slashes)


@app.route("/")
def home():
    reload = time.time()
    return render_template("index.html", reload=reload)


@app.route('/help')
def url_map():
    return "<pre>" + str(pprint.pformat(app.url_map, indent=4)) + "</pre>"


@app.route("/codeply/")
# @app.route("/codeply/")
def codeply():
    # reload = time.time()
    _, _, templates = next(walk('templates/codeply'))
    anchors = [f'<a href="/codeply/{pathlib.Path(template).stem}">{template}</a>' for template in templates]
    anchors.insert(0, '<a href="/">home</a>')
    return "<br>".join(anchors)


@app.route("/codeply/<page>")
def codeply_page(page):
    reload = time.time()
    return render_template(f"/codeply/{page}.html", reload=reload)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
