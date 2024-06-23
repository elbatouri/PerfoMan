from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from App import app, db, bcrypt
from App.forms import RegistrationForm, LoginForm, UpdateAccountForm, EquipmentForm, InterventionForm, MaintenanceScheduleForm, CheckListForm
from App.models import User, Equipement, Intervention, MaintenanceSchedule, CheckList
from datetime import datetime

@app.route("/")
@app.route("/home")
def home():
    interventions = Intervention.query.all()
    return render_template('home.html', interventions=interventions)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route("/equipment/new", methods=['GET', 'POST'])
@login_required
def new_equipment():
    form = EquipmentForm()
    if form.validate_on_submit():
        equipment = Equipement(name=form.name.data, description=form.description.data)
        db.session.add(equipment)
        db.session.commit()
        flash('New equipment has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('create_equipment.html', title='New Equipment', form=form, legend='New Equipment')

@app.route("/intervention/new", methods=['GET', 'POST'])
@login_required
def new_intervention():
    form = InterventionForm()
    if form.validate_on_submit():
        intervention = Intervention(maintenanceType=form.maintenanceType.data, description=form.description.data, 
                                    equipementId=form.equipementId.data, tagEquipement=form.tagEquipement.data, 
                                    userId=current_user.id)
        db.session.add(intervention)
        db.session.commit()
        flash('New intervention has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_intervention.html', title='New Intervention', form=form, legend='New Intervention')

@app.route("/maintenance_schedule/new", methods=['GET', 'POST'])
@login_required
def new_maintenance_schedule():
    form = MaintenanceScheduleForm()
    if form.validate_on_submit():
        schedule = MaintenanceSchedule(maintenanceType=form.maintenanceType.data, description=form.description.data, 
                                       equipementId=form.equipementId.data, tagEquipement=form.tagEquipement.data, 
                                       userId=current_user.id, startDate=form.startDate.data)
        db.session.add(schedule)
        db.session.commit()
        flash('New maintenance schedule has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_maintenance_schedule.html', title='New Maintenance Schedule', form=form, legend='New Maintenance Schedule')

@app.route("/checklist/new", methods=['GET', 'POST'])
@login_required
def new_checklist():
    form = CheckListForm()
    if form.validate_on_submit():
        checklist = CheckList(name=form.name.data, description=form.description.data, temperature=form.temperature.data, 
                              RV1=form.RV1.data, RV2=form.RV2.data, RV3=form.RV3.data, RV4=form.RV4.data, 
                              RH1=form.RH1.data, RH2=form.RH2.data, RH3=form.RH3.data, RH4=form.RH4.data, 
                              AX1=form.AX1.data, AX2=form.AX2.data, AX3=form.AX3.data, AX4=form.AX4.data, 
                              bruit=form.bruit.data)
        db.session.add(checklist)
        db.session.commit()
        flash('New checklist has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_checklist.html', title='New Checklist', form=form, legend='New Checklist')


if __name__ == '__main__':
    app.run(debug=True)