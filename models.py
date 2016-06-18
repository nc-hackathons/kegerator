from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import IPython

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://nc:kegerator1234@localhost:3306/kegerator'
db = SQLAlchemy(app)

class Batch(db.Model):
    __tablename__ = 'batches'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    current = db.Column(db.Boolean)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'))
    keg_id = db.Column(db.Integer, db.ForeignKey('kegs.id'))
    
    def __init__(self, beer, keg, current):
        self.current = current
        self.beer_id = beer.id
        self.keg_id = keg.id
        self.created_at = datetime.utcnow()
        
    def to_json(self):
        return {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%T.620Z"),
            'current': self.current,
            'beer': Beer.query.filter_by(id=self.beer_id).first().to_json(),
            'keg': Keg.query.filter_by(id=self.keg_id).first().to_json(),
            'pours': [ pour.to_json() for pour in Pour.query.filter_by(batch_id=self.id).all() ]
        }

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    batches = db.relationship('Batch', backref='beer', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
class Keg(db.Model):
    __tablename__ = 'kegs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    total_volume = db.Column(db.Float)
    units = db.Column(db.String(32))
    batches = db.relationship('Batch', backref='keg', lazy='dynamic')
    
    def __init__(self, name, total_volume, units):
        self.name = name
        self.total_volume = total_volume
        self.units = units
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'total_volume': self.total_volume,
            'units': self.units
        }
    
class Pour(db.Model):
    __tablename__ = 'pours'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    volume_poured = db.Column(db.Float)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    
    def __init__(self, batch, volume):
        self.batch_id = batch.id
        self.volume_poured = volume
        self.created_at = datetime.utcnow()
    
    def to_json(self):
        return {
	    'created_at': self.created_at.strftime("%Y-%m-%dT%T.620Z"),
            'volume_poured': self.volume_poured
        }

