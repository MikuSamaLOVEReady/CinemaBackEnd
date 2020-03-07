import os

WTF_CSRF_ENABLED = True
SECRET_KEY ='MKMKMKMKKMKMKMKMKKM'

basedir = os.path.abspath(os.path.dirname(__file__))

JSON_AS_ASCII = False  # support Chinese
JSON_SORT_KEYS = False  # don't sort when jsonify

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
