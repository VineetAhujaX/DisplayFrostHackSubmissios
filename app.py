from flask import Flask, redirect, url_for, render_template, request, session,abort
import csv
def fetchall():
    data = list(csv.reader(open("submission.csv",encoding="utf8")))
    return data

app = Flask(__name__)


@app.route("/")
def index():
    data = fetchall()
    return render_template("projects.html",data=data[1:])

@app.route("/details/<id>")
def detail(id):
    data = fetchall()
    id= int(id)
    if(id<1 or id>len(data)-1):
        abort(404)
    head=data[0]
    head=head[1:]
    row= data[id]
    row=row[1:]
    return render_template("details.html", row=row,head=head,row_head=zip(row,head))

if __name__ == "__main__":
    app.run(debug=True,port=5000)
