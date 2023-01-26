from flask import (
    Flask, render_template,
    request, redirect, url_for,
    flash, Response
)
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from resources import get_bucket
from config import FLASK_SECRET_KEY

app = Flask(__name__)
Bootstrap(app)
app.secret_key = FLASK_SECRET_KEY
app.jinja_env.filters["datetimeformat"] = datetimeformat
app.jinja_env.filters["file_type"] = file_type


@app.route("/")
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template("files.html", my_bucket=my_bucket, files=summaries)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        my_bucket = get_bucket()
        my_bucket.Object(file.filename).put(Body=file)

        flash("File uploaded successfully")
        return redirect(url_for("files"))
    else:
        flash("Please select a file")
        return redirect(url_for("files"))


@app.route("/download", methods=["POST"])
def download():
    key = request.form["key"]

    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj["Body"].read(),
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename={}".format(key)},
    )


if __name__ == "__main__":
    app.run()
