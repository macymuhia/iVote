from flask import render_template
from . import main
from ..email import mail_message


# views
@main.route("/", methods=['GET', 'POST'])
def index():
    users = ['michellemukami.g@gmail.com', 'macymuhia@gmail.com', 'sylviah.rutto@gmail.com']
    for user in range(len(users)):
        mail_message('iVote', 'email/welcome_user', users[user])
    return render_template('index.html')
