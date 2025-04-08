from flask import Flask, render_template, request
import pdfkit

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form
        pdf = pdfkit.from_string(render_template("resume.html", data=data), False)
        with open("Vaishnavi_Resume.pdf", "wb") as f:
            f.write(pdf)
    return render_template("form.html")
