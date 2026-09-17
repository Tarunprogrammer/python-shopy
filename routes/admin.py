from flask import Blueprint, render_template, request, redirect, url_for, session
from firebase_admin import db

admin_bp = Blueprint('admin', __name__)

def is_admin():
    return session.get('user') and session['user'].get('role') == 'admin'

@admin_bp.route('/')
def dashboard():
    if not is_admin(): return redirect(url_for('auth.login'))
    products = db.reference('products').get() or {}
    return render_template('admin_dashboard.html', products=products)

@admin_bp.route('/add', methods=['POST'])
def add():
    if not is_admin(): return redirect(url_for('auth.login'))
    data = {
        "name": request.form.get('name'),
        "price": request.form.get('price'),
        "image_url": request.form.get('image_url')
    }
    db.reference('products').push(data)
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete/<id>')
def delete(id):
    db.reference(f'products/{id}').delete()
    return redirect(url_for('admin.dashboard'))