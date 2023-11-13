from urllib.parse import quote
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.secret_key = 'fefgqwfjahwiejvneoghqaenfqiuh'
app.config["SQLALCHEMY_DATABASE_URI"]= "mysql+pymysql://root:%s@localhost/labsaledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)