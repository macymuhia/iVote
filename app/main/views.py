from flask import render_template, request,redirect, url_for
import datetime
import os
import jwt
from . import main
from ..email import mail_message
from ..utils import token_url



# views
@main.route("/", methods=['GET', 'POST'])
def index():
    users = [{'email':'macymuhia@gmail.com', 'id':'2163748'}, {'email':'mercy8muhia@gmail.com', 'id':'2167748'}, {'email':'maretekent@gmail.com', 'id':'2163708'}]
    expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*24)
    for user in users:
        create_pwd_url = token_url(user['id'], user['email'], expiry)
        print(create_pwd_url)
        # mail_message('iVote', 'email/welcome_user', user['email'], url=create_pwd_url)
    return render_template('index.html')


@main.route("/create_password", methods=['GET', 'POST'])
def create_password():
    
    if 'token' in request.args:
        # Token exist, etxract, decode an redirect to the create password page
        secret_key = os.environ.get('JWT_SECRET')
        algorithm  = os.environ.get('JWT_ALGORITHM')
        token = request.args.get('token')
        try:
            payload = jwt.decode(
                token,
                secret_key,
                algorithm=algorithm
            )
            print(payload)
            # verify user exist with email and id from the payload
            # reditrect user to create password page

        except (jwt.ExpiredSignatureError, jwt.DecodeError) as e:
            return redirect(url_for('main.four_o_four'))

    else:
        # render the token does not exist error page 
        return redirect(url_for('main.four_o_four'))

    return render_template('test.html')

@main.route('/404')
def four_o_four():
    return render_template('404.html')
