from app.models.base import db


#以下为一对多关系
class Parent(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(30), unique=True)
	test = db.Column(db.String(30), unique=True)
	test1 = db.Column(db.String(30), unique=True)

	children = db.relationship("Child", backref="parent")

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "name is %r" % self.name


class Child(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(30), unique=True)

	parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "name is %r"



class ad(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True)
	test = db.Column(db.String(30), unique=True)
	test1 = db.Column(db.String(30), unique=True)
	test2= db.Column(db.String(30), unique=True)

