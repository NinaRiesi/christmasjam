from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def project():
    return render_template("Project_page1.html")


@app.route("/page2")
def project2():
    return render_template("Project_page2.html")
app.run(debug=True)
