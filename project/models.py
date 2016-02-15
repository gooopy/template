from flask_sqlalchemy import SQLAlchemy
from project import db
from datetime import datetime

class DDL(db.Model):
    __tablename__ = 'ddl'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    creation_date = db.Column(db.DateTime)
    field_delimeter = db.Column(db.String(120), nullable=False)
    record_delimeter = db.Column(db.String(120), nullable=False)
    attributes = db.relationship('Attribute', backref='ddl', lazy='dynamic')

    def __init__(self, title, field_delimeter, record_delimeter):
        self.title = title
        self.creation_date = datetime.now()
        self.field_delimeter = field_delimeter
        self.record_delimeter = record_delimeter

    def __repr__(self):
        return '<id:%r, title:%r, creation_date:%r, field_delimeter:%r, record_delimeter:%r>' % (self.id, self.title, self.creation_date, self.field_delimeter, self.record_delimeter)

class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    attr_type = db.Column(db.String(120), nullable=False)
    nullable = db.Column(db.Boolean, default=False)
    default_value = db.Column(db.String, nullable=True)
    ddl_id = db.Column(db.Integer, db.ForeignKey('ddl.id'))

    def __init__(self, name, attr_type, nullable, default_value):
        self.name = name
        self.attr_type = attr_type
        self.nullable = nullable
        self.default_value = default_value


class TaskFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __init__(self, name):
        self.name = name



def seed():

    db.drop_all()
    db.create_all()

    sample = DDL("sample", ",", "\\n")
    if not DDL.query.filter_by(title="sample").first():
        db.session.add(sample)

    sample = DDL.query.filter_by(title="sample").first()

    attributes = []

    attr = Attribute("order_num", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("id", "string", False, None)
    attributes.append(attr)

    attr = Attribute("post_code", "string", False, None)
    attributes.append(attr)

    attr = Attribute("age", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("ip", "string", False, None)
    attributes.append(attr)

    attr = Attribute("buy_date", "string", False, None)
    attributes.append(attr)

    attr = Attribute("total_price", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("itemcode", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("buy_good_count", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("buy_good_price", "integer", False, None)
    attributes.append(attr)

    attr = Attribute("good_cate", "string", False, None)
    attributes.append(attr)

    for a in attributes:
        a.ddl_id = sample.id
        db.session.add(a)

    #preprocessed = DDL("preprocessed", "")


    db.session.commit()