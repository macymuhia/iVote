from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,,Results
from .forms import PresidentialForm,GovernorForm




@main.route('/')
def vote():
    pw=""
    return render_template('user_list.html')
    return pw

@main.route('/thanks')
def thanks():
    return render_template('thanks.html')


@main.route('/ge_vote', methods=['POST'])
def post_user():
    vote = Votes(request.form['hg'], request.form['hb'])
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for('thanks'))


@main.route('/ge_results')
@login_required
def results():
        ngigi=Votes.query.filter(Votes.hb == "ngigi").count()
        sylviah=Votes.query.filter(Votes.hb == "sylviah").count()
        michelle=Votes.query.filter(Votes.hg == "michelle").count()
        mercy=Votes.query.filter(Votes.hg == "mercy").count()

        print("Total Voters",( ))

        results={"Ngigi":ngigi,"Sylviah":sylviah,"Michellle":michelle,"Mercy":mercy}


        return render_template("results.html", results=results)


