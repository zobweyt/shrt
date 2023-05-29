from flask import redirect, render_template

from app import app, db
from app.forms import URLForm
from app.models import URL
from app.services import generate_short_url


@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()

    if form.validate_on_submit():
        short_url = generate_short_url()
        original_url = form.original_url.data

        url = URL(original_url=original_url, short_url=short_url)

        db.session.add(url)
        db.session.commit()

        form = URLForm()

    urls = URL.query.order_by(URL.created_at.desc()).all()

    return render_template("index.html", form=form, urls=urls)


@app.route("/<string:short_url>/")
def get_short(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)
