from flask_sqlalchemy import SQLAlchemy
from poker_quiz import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/poker_quiz.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    group = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r' % self.username
