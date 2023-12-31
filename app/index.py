from flask import Flask, render_template,request
import dao
from app import app, login


@app.route("/")
def index():
    kw = request.args.get('kw')

    cates = dao.get_categories()
    prod = dao.get_products(kw)
    return render_template("index.html", categories = cates, products = prod)

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == "__main__":
    from app import Admin
    app.run(debug=True)