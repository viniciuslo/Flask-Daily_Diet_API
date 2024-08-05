from datetime import datetime
from . import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    in_diet = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_time': self.date_time,
            'in_diet': self.in_diet,
            'user_id': self.user_id
        }
