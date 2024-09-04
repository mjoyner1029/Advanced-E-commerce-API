from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    account = db.relationship('CustomerAccount', back_populates='customer', uselist=False)
    orders = db.relationship('Order', back_populates='customer')
