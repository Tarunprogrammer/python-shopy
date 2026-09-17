from flask import Blueprint, render_template, session, redirect, url_for
from firebase_admin import db

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    products = db.reference('products').get() or {}
    return render_template('index.html', products=products)

@home_bp.route('/order/<product_id>')
def place_order(product_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    order_data = {
        "user_id": session['user_id'],
        "product_id": product_id,
        "status": "Pending"
    }
    db.reference('orders').push(order_data)
    return "Order Placed Successfully! <a href='/'>Go Back</a>"