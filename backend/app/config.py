import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'talesmith.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
