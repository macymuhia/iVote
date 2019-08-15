from flask import render_template
from . import main
from ..email import mail_message


# views
@main.route("/", methods=['GET', 'POST'])
def index():
    users = ['macymuhia@gmail.com', 'mercy8muhia@gmail.com', 'maretekent@gmail.com']
    for user in range(len(users)):
        mail_message('iVote', 'email/welcome_user', users[user])
    return render_template('index.html')
