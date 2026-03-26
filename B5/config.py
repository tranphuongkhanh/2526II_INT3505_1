import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Cấu hình Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'library.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False