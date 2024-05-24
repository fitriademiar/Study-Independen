from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("Profile-Bootstrap.html")

@app.route("/form")
def form():
    return render_template("formbootstrap.html")


if __name__ == "__main__":
    app.run(debug=True)