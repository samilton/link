from app import db


class Realm(db.Model):
    __tablename__ = 'realms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    #aliases = db.relationship("Alias")


class Alias(db.Model):
    __tablename__ = 'aliases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    #realm_id = db.Column(db.Integer, db.ForeignKey('realm.id'))
    #realm = db.relationship("Realm", back_populates="aliases")
