from flask import Flask, render_template, request, redirect					
from sqlalchemy.sql import func                         
from config import app, db, migrate

class ninjas(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_name = db.Column(db.String(45))
    dojos_id = db.Column(db.Integer, db.ForeignKey("dojos.id"))
    dojo = db.relationship("dojos", foreign_keys=[dojos_id], backref="ninjas", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())  
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class dojos(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())  
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

@app.route("/")
def index():
    users = ninjas.query.all()
    dojo_list = dojos.query.all()
    return(render_template('index.html', users=users, dojos=dojo_list))

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    new_instance_of_a_user = dojos(name=request.form['NA'], city=request.form['CT'], state=request.form['ST'])
    db.session.add(new_instance_of_a_user)
    db.session.commit()
    
    return redirect('/')

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    new_instance_of_a_user = ninjas(first_name=request.form['FN'], last_name=request.form['LN'], dojo_name=request.form['DJ'])
    db.session.add(new_instance_of_a_user)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)