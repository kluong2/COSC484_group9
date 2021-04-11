from flask import Blueprint, render_template, flash

auth = Blueprint('auth', __name__)



@auth.route ('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template("login.html", boolean = True)

@auth.route ('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route ('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     firstName = request.form.get('firstName')
    #     password1 = request.form.get('password1')
    #     password2 = request.form.get('password2')

    #     if len(email) < 4:
    #         flash (" Email must be at least 4 characters", category="error")
    #     elif len(firstName) <2 :
    #         flash (" name must be at least 2 characters", category="error")
    #     elif password1 != password2:
    #         flash (" Password dont much", category="error")
    #     elif len(password2)<7:
    #         flash (" Password too short", category="error")
    #     else:
    #         flash (" created", category="success")

    return render_template("sign_up.html")
