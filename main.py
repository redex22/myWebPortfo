import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode="a", newline="\n") as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/contact.html")
        except:
            return "The database saving went wrong :("
    else:
        return "Ups!, something went wrong :("

