import firebase_admin
from firebase_admin import credentials
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "super_secret_key" # Required for sessions

# 1. Setup Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pyshopy-3fe4c-default-rtdb.firebaseio.com/'
})

# 2. Register Blueprints
from routes.home import home_bp
from routes.admin import admin_bp
from routes.auth import auth_bp

app.register_blueprint(home_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)