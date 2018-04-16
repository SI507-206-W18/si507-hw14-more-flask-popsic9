from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    entries = model.get_entries()
    return render_template("index.html", entries=entries)

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/admin")
def admin():
    return render_template("admin.html", entries = model.get_entries())

@app.route("/delete", methods=["POST"])
def deleteentry():
    id_ = request.form["id"]
    model.delete_entry(id_)
    return redirect("/admin")

@app.route('/change', methods = ['POST'])
def changeentry():
    id_ = request.form["id"]
    entry = model.get_entry(id_)
    name = entry['author']
    return render_template("changeentry.html", name = name)

@app.route('/postchange', methods = ['POST'])
def postchange():
    message = request.form["changemessage"]
    model.change_message(message)
    return redirect("/admin")

if __name__=="__main__":
    model.init()
    app.run(debug=True)
