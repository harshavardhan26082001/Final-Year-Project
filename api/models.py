from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import secrets
from flask_sqlalchemy import SQLAlchemy
from app import db
 


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    password  = db.Column(db.String(50))
    email  = db.Column(db.String(50))
    address = db.Column(db.String(50))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    api_id = db.Column(db.String(16), default =  secrets.token_hex(16))
    api_token = db.Column(db.String(16), default =  secrets.token_hex(16))

class Data(db.Model):
    __tablename__ = 'Data'
    id= db.Column(db.Integer, primary_key = True)
    Client_id = db.Column(db.Integer)
    age =  db.Column(db.Integer)
    asv =  db.Column(db.Integer)
    amount = db.Column(db.Integer)
    cardNo = db.Column(db.Integer)
    label =  db.Column(db.Boolean)
    location = db.Column(db.String(50))
    bank = db.Column(db.String(50))
    card_type = db.Column(db.String(50))


class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    api_key = db.Column(db.String(50), default =  secrets.token_hex(32))



#-----------------------------------------------------------------------
