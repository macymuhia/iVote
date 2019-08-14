from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    votes = db.relationship('Votes', backref = 'users', lazy="dynamic")
    id = db.Column(db.Integer,primary_key = True)
    id_number =db.Column(db.Integer())
    password = db.Column(db.String(255),index = True)
    password_secure = db.Column(db.String(255))
    
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
   

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
class Vote(db.Model):
    __tablename__="vote"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
      