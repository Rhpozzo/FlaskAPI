from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "address" : self.address,
            "phone": self.phone
        }
