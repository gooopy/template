#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request, redirect, flash, url_for, make_response, session
from project import app
from project import db
from project.models import DDL, Attribute, TaskFile
from ddl_maker import make_ddl
from dasie_runner import run_dasie, kill_dasie, shoot_data
from wtforms import Form, BooleanField, TextField, PasswordField, SelectField, SelectMultipleField, validators, widgets, FieldList, FormField


# wtforms Form Class
class DDLForm(Form):
    title = TextField('Title', [validators.Length(max=25)])
    field_delimeter = TextField('Field_delimeter')
    record_delimeter = TextField('Record_delimeter')

class DDLAttributeForm(Form):
	name1 = TextField('Name')
	name2 = TextField('Name')
	name3 = TextField('Name')
	name4 = TextField('Name')
	name5 = TextField('Name')
	name6 = TextField('Name')
	name7 = TextField('Name')
	name8 = TextField('Name')
	name9 = TextField('Name')
	name10 = TextField('Name')
	name11 = TextField('Name')
	name12 = TextField('Name')
	type1 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type2 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type3 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type4 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type5 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type6 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type7 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type8 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type9 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type10 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type11 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	type12 = SelectField('Type', choices =[
		('string', 'string'),
		('int', 'int'),
		('long', 'long'),
		('double', 'double')
		])
	nullable1 = BooleanField('Allow NULLS')
	nullable2 = BooleanField('Allow NULLS')
	nullable3 = BooleanField('Allow NULLS')
	nullable4 = BooleanField('Allow NULLS')
	nullable5 = BooleanField('Allow NULLS')
	nullable6 = BooleanField('Allow NULLS')
	nullable7 = BooleanField('Allow NULLS')
	nullable8 = BooleanField('Allow NULLS')
	nullable9 = BooleanField('Allow NULLS')
	nullable10 = BooleanField('Allow NULLS')
	nullable11 = BooleanField('Allow NULLS')
	nullable12 = BooleanField('Allow NULLS')
	default1 = TextField('Default value')
	default2 = TextField('Default value')
	default3 = TextField('Default value')
	default4 = TextField('Default value')
	default5 = TextField('Default value')
	default6 = TextField('Default value')
	default7 = TextField('Default value')
	default8 = TextField('Default value')
	default9 = TextField('Default value')
	default10 = TextField('Default value')
	default11 = TextField('Default value')
	default12 = TextField('Default value')



@app.route('/')
def hello_world():
    #make_ddl()
    return redirect(url_for('ddl_choose'))

@app.route('/ddl')
def ddl_choose():
	form = DDLForm(request.form)
	existing_ddls = DDL.query.all()
	return render_template('ddl_choose.html',form=form, ddls=existing_ddls)

@app.route('/ddl/new', methods=['GET', 'POST'])
def ddl_add():
	form = DDLForm(request.form)
	if request.method == 'POST' and form.validate:
		ddl = DDL(form.title.data, form.field_delimeter.data, form.record_delimeter.data)
		db.session.add(ddl)
		db.session.commit()
		next_form = DDLAttributeForm(request.form)
		return render_template('attributes.html', form=next_form, ddlname=ddl.title)
	return render_template('ddl_add.html', form=form)

@app.route('/ddl/<name>')
def ddl_show(name):
	ddl = DDL.query.filter_by(title=name).first()
	return render_template('ddl_show.html', ddl=ddl)

@app.route('/ddl/select', methods=['GET', 'POST'])
def ddl_select():
	all_ddls = DDL.query.all()
	ddls = []

	selected = request.form
	selected_ddls = ""
	for ddlname in selected:
		ddl = DDL.query.filter_by(title=ddlname).first()
		ddls.append(ddl)
		selected_ddls += ddl.title
		selected_ddls += ","

	session['ddlnames'] = selected_ddls
	ddls.reverse()
	make_ddl(ddls)
	#flash("successfully made.")
	return redirect(url_for('task_choose'))

@app.route('/ddl/delete/<name>')
def ddl_delete(name):
	ddl = DDL.query.filter_by(title=name).first()
	if ddl is None:
		flash("error: There is no DDL which name is " + str(name))
		return redirect(url_for('ddl_choose'))
	db.session.delete(ddl)
	db.session.commit()
	flash(str(name) + " is deleted.")
	return redirect(url_for('ddl_choose'))

@app.route('/ddl/make/<name>')
def ddl_make(name):
	ddl = DDL.query.filter_by(title=name).first()
	ddls = []
	ddls.append(ddl)
	make_ddl(ddls)
	flash("successfully made.")
	return redirect(url_for('ddl_choose'))


@app.route('/task/choose')
def task_choose():
	tasks = TaskFile.query.all()
	ddls = session['ddlnames']
	return render_template('task_choose.html', ddls=ddls, tasks=tasks)

#@app.route('/task/select/<name>', methods=['GET','POST'])
#def task_select(name):
#	task = TaskFile.query.filter_by(name=name).first()
#	run_dasie(task)


@app.route('/register_attributes', methods=['POST'])
def attr_add():
	form = DDLAttributeForm(request.form)
	ddl = DDL.query.filter_by(title=request.form['ddlname']).first()

	if form.name1.data:
		attr1=Attribute(form.name1.data, form.type1.data, form.nullable1.data, form.default1.data)
		attr1.ddl_id = ddl.id
		db.session.add(attr1)
	if form.name2.data:
		attr2=Attribute(form.name2.data, form.type2.data, form.nullable2.data, form.default2.data)
		attr2.ddl_id = ddl.id
		db.session.add(attr2)
	if form.name3.data:
		attr3=Attribute(form.name3.data, form.type3.data, form.nullable3.data, form.default3.data)
		attr3.ddl_id = ddl.id
		db.session.add(attr3)
	if form.name4.data:
		attr4=Attribute(form.name4.data, form.type4.data, form.nullable4.data, form.default4.data)
		attr4.ddl_id = ddl.id
		db.session.add(attr4)
	if form.name5.data:
		attr5=Attribute(form.name5.data, form.type5.data, form.nullable5.data, form.default5.data)
		attr5.ddl_id = ddl.id
		db.session.add(attr5)
	if form.name6.data:
		attr6=Attribute(form.name6.data, form.type6.data, form.nullable6.data, form.default6.data)
		attr6.ddl_id = ddl.id
		db.session.add(attr6)
	if form.name7.data:
		attr7=Attribute(form.name7.data, form.type7.data, form.nullable7.data, form.default7.data)
		attr7.ddl_id = ddl.id
		db.session.add(attr7)
	if form.name8.data:
		attr8=Attribute(form.name8.data, form.type8.data, form.nullable8.data, form.default8.data)
		attr8.ddl_id = ddl.id
		db.session.add(attr8)
	if form.name9.data:
		attr9=Attribute(form.name9.data, form.type9.data, form.nullable9.data, form.default8.data)
		attr9.ddl_id = ddl.id
		db.session.add(attr9)
	if form.name10.data:
		attr10=Attribute(form.name10.data, form.type10.data, form.nullable10.data, form.default10.data)
		attr10.ddl_id = ddl.id
		db.session.add(attr10)
	if form.name11.data:
		attr11=Attribute(form.name11.data, form.type11.data, form.nullable11.data, form.default11.data)
		attr11.ddl_id = ddl.id
		db.session.add(attr11)
	if form.name12.data:
		attr12=Attribute(form.name12.data, form.type12.data, form.nullable12.data, form.default12.data)
		attr12.ddl_id = ddl.id
		db.session.add(attr12)


	db.session.commit()
	return redirect(url_for('ddl_choose'))


@app.route('/run', methods=['GET', 'POST'])
def run():
	if request.method == 'POST':
		run_dasie()
		#flash("Successfully loaded.")
		return render_template('running.html')
	return render_template('run.html')

@app.route('/shoot', methods=['GET', 'POST'])
def shoot():
	if request.method == 'POST':
		shoot_data()
		return render_template('shooting.html')
	flash("error: Wrong access")
	return redirect(url_for('hello_world'))


@app.route('/kill', methods=['GET', 'POST'])
def kill():
	if request.method == 'POST':
		kill_dasie()
		return render_template('killed.html')
	flash("error: Wrong access")
	return redirect(url_for('hello_world'))





