from flask import Flask,redirect,render_template,flash, url_for,abort
import os
from price_tracker import Object
from forms import MakeObject
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

data = {}


@app.route("/", methods = ['GET','POST'])
def index():
    form = MakeObject()
    if form.validate_on_submit():
        data[f'{form.name.data}'] = Object(form.name.data,form.target_price.data,form.url.data)
        flash("Product sucessfully registered")
        return redirect(f"/track/{form.name.data}")
    return render_template("index.html",form=form,data=data)

@app.route("/track/<name>")
def track(name):
    product = data.get(name)
    if product is None:
        abort(404)

    reached = product.check_if_reached_target()
    if reached:
        data.pop(name)
    return render_template("tracker.html", product=product, reached=reached)


if __name__ == '__main__':
    app.run(debug=True)