from flask import Flask,render_template,request,url_for
app = Flask(__name__)
@app.route("/")
def hello_World():
    return render_template('index.html')

@app.route("/dashboard2")
def h():
    return render_template('dashboard2.html')

@app.route("/dashboard3")
def i():
    return render_template('dashboard3.html')

@app.route("/dashboard1")
def j():
    return render_template('dashboard1.html')

@app.route("/detail")
def a():
    return render_template('detail.html')

@app.route("/feature")
def b():
    return render_template('feature.html')


@app.route("/insight1")
def k():
    return render_template('insight1.html')

@app.route("/insight2")
def l():
    return render_template('insight2.html')

@app.route("/insight3")
def m():
    return render_template('insight3.html')

@app.route("/insight4")
def n():
    return render_template('insight4.html')

@app.route("/insight5")
def o():
    return render_template('insight5.html')

@app.route("/report")
def p():
    return render_template('report.html')

@app.route("/report1")
def q():
    return render_template('report1.html')

@app.route("/report2")
def r():
    return render_template('report2.html')

@app.route("/report3")
def s():
    return render_template('report3.html')

@app.route("/report4")
def t():
    return render_template('report4.html')

@app.route("/story")
def u():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)