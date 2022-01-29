from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Myapp(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500))


@app.route('/')
def home():
    return 'this is my first page'


@app.route('/insert', methods=['POST'])
def home2():
    c_name = request.form.get("c_name")
    new_c_name = Myapp(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()
    # return render_template("base.html", c_name=c_name)
    return redirect(url_for("home1"))


@app.route('/delete/<int:c_id>')
def delete(c_id):
    c_name = Myapp.query.get_or_404(c_id)
    db.session.delete(c_name)
    db.session.commit()
    # return render_template("base.html", c_name=c_name)
    return redirect(url_for("home1"))

@app.route('/base')
def home1():
    my_list = Myapp.query.all()
    var = "hello this is my first variable"

    return render_template("base.html", my_list=my_list)


if __name__ == "__main__":
    app.run()
