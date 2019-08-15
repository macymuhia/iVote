from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect,  url_for



main = Flask(__name__)




def __init__(self,hg, hb):
        self.hg = hg
        self.hb = hb

def __repr__(self):
        return '<User %r>' % self.hb


@main.route('/')
def vote():
    pw=""
    return render_template('vote.html')
    return pw

@main.route('/thanks')
def thanks():
    return render_template('thanks.html')








if __name__ == "__main__":

    main.run()
