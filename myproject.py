from flask import Flask , render_template
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__, static_folder = 'frontend' , template_folder = 'frontend')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproject.db'
db = SQLAlchemy(application)
