from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/index')
def show_index():
    return render_template("homepage.html")
if __name__ == "__main__":
    app.run(debug=True)
