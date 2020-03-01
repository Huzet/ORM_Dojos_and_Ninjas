from flask import Flask, render_template, request, redirect
from config import app, db
from models import ninjas, dojos

def index():
    users = ninjas.query.all()
    dojo_list = dojos.query.all()
    return(render_template('index.html', users=users, dojos=dojo_list))

def add_dojo():
    new_instance_of_a_user = dojos(name=request.form['NA'], city=request.form['CT'], state=request.form['ST'])
    db.session.add(new_instance_of_a_user)
    db.session.commit()   
    return redirect('/')

def add_ninja():
    new_instance_of_a_user = ninjas(first_name=request.form['FN'], last_name=request.form['LN'], dojo_name=request.form['DJ'])
    db.session.add(new_instance_of_a_user)
    db.session.commit()
    return redirect('/')