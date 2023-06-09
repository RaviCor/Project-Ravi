from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()


#class User(db.Model, UserMixin):
#    __tablename__ = 'user'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#
#    def __repr__(self):
#        return f"<User {self.username}>"
#    def set_password(self, password):
#        self.password = generate_password_hash(password)
#    def check_password(self, password):
#        return check_password_hash(self.password, password)
#    def __repr__(self):
#        return '<User {}>'.format(self.email)
#    
#    @classmethod
#    def get(cls, user_id):
#        return cls.query.get(user_id)
