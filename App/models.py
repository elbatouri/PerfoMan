from datetime import datetime
from flask_login import UserMixin
from App import db, login_manager
from sqlalchemy import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)
    

class Equipement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    isActive = db.Column(db.Boolean, default=True, nullable=False)

class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maintenanceType = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    equipementId = db.Column(db.Integer, db.ForeignKey('equipement.id'), nullable=False)
    tagEquipement = db.Column(db.String(100), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    dateDeleted = db.Column(db.DateTime, nullable=True)
    dateClosed = db.Column(db.DateTime, nullable=True)
    dateReopened = db.Column(db.DateTime, nullable=True)
    isClosed = db.Column(db.Boolean, default=False, nullable=False)
    isReopened = db.Column(db.Boolean, default=False, nullable=False)
    isDeleted = db.Column(db.Boolean, default=False, nullable=False)
    equipement = db.relationship('Equipement', backref='interventions')
    user = db.relationship('User', backref='interventions')
    Ressource = db.relationship('Ressource', backref='interventions')

class Ressource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class MaintenanceType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class MaintenanceSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maintenanceType = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    equipementId = db.Column(db.Integer, db.ForeignKey('equipement.id'), nullable=False)
    tagEquipement = db.Column(db.String(100), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    dateDeleted = db.Column(db.DateTime, nullable=True)
    startDate = db.Column(db.DateTime, nullable=False)
    equipement = db.relationship('Equipement', backref='maintenanceSchedules')
    user = db.relationship('User', backref='maintenanceSchedules')
    Ressource = db.relationship('Ressource', backref='maintenanceSchedules')

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    temperature = db.Column(db.Float, nullable=False)
    RV1 = db.Column(db.Float, nullable=False)
    RV2 = db.Column(db.Float, nullable=False)
    RV3 = db.Column(db.Float, nullable=False)
    RV4 = db.Column(db.Float, nullable=False)
    RH1 = db.Column(db.Float, nullable=False)
    RH2 = db.Column(db.Float, nullable=False)
    RH3 = db.Column(db.Float, nullable=False)
    RH4 = db.Column(db.Float, nullable=False)
    AX1 = db.Column(db.Float, nullable=False)
    AX2 = db.Column(db.Float, nullable=False)
    AX3 = db.Column(db.Float, nullable=False)
    AX4 = db.Column(db.Float, nullable=False)
    bruit = db.Column(db.Boolean, nullable=False)
    