from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_share import Share

from app import app
from flask_admin import Admin

import pymysql
pymysql.install_as_MySQLdb()



admin = Admin(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type = True)

share = Share(app)