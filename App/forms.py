from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from App.models import User, Equipement

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already in use. Please choose a different one.')

class EquipmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Equipment')

    def validate_name(self, name):
        equipment = Equipement.query.filter_by(name=name.data).first()
        if equipment:
            raise ValidationError('That equipment name is already in use. Please choose a different one.')

class InterventionForm(FlaskForm):
    maintenanceType = StringField('Maintenance Type', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    equipementId = IntegerField('Equipment ID', validators=[DataRequired()])
    tagEquipement = StringField('Tag Equipment', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Create Intervention')

class MaintenanceScheduleForm(FlaskForm):
    maintenanceType = StringField('Maintenance Type', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    equipementId = IntegerField('Equipment ID', validators=[DataRequired()])
    tagEquipement = StringField('Tag Equipment', validators=[DataRequired(), Length(min=2, max=100)])
    startDate = DateTimeField('Start Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Create Maintenance Schedule')

class CheckListForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    temperature = FloatField('Temperature', validators=[DataRequired()])
    RV1 = FloatField('RV1', validators=[DataRequired()])
    RV2 = FloatField('RV2', validators=[DataRequired()])
    RV3 = FloatField('RV3', validators=[DataRequired()])
    RV4 = FloatField('RV4', validators=[DataRequired()])
    RH1 = FloatField('RH1', validators=[DataRequired()])
    RH2 = FloatField('RH2', validators=[DataRequired()])
    RH3 = FloatField('RH3', validators=[DataRequired()])
    RH4 = FloatField('RH4', validators=[DataRequired()])
    AX1 = FloatField('AX1', validators=[DataRequired()])
    AX2 = FloatField('AX2', validators=[DataRequired()])
    AX3 = FloatField('AX3', validators=[DataRequired()])
    AX4 = FloatField('AX4', validators=[DataRequired()])
    bruit = BooleanField('Bruit', validators=[DataRequired()])
    submit = SubmitField('Create CheckList')