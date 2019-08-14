

        return redirect(url_for('auth.login'))
        title='New Account'
    return render_template('auth/register.html',registration_form=form)

# Log Out
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))