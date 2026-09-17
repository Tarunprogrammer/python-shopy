from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from firebase_admin import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').replace('.', ',') # Firebase keys can't have dots
        password = request.form.get('password')
        
        user_ref = db.reference(f'users/{email}').get()
        
        if user_ref and user_ref['password'] == password:
            session['user'] = user_ref
            session['user_id'] = email
            return redirect(url_for('home.index'))
        flash("Invalid Credentials")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))