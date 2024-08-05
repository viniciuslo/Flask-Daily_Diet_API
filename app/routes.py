from flask import request, jsonify, Blueprint
from datetime import datetime
from . import db
from .models import Meal

bp = Blueprint('main', __name__)

@bp.route('/meals', methods=['POST'])
def create_meal():
    data = request.get_json()
    date_time = datetime.fromisoformat(data['date_time'])  # Convertendo a string para datetime
    new_meal = Meal(
        name=data['name'],
        description=data.get('description', ''),
        date_time=date_time,
        in_diet=data.get('in_diet', True),
        user_id=data['user_id']
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify(new_meal.to_dict()), 201

@bp.route('/meals/<int:id>', methods=['PUT'])
def update_meal(id):
    meal = Meal.query.get_or_404(id)
    data = request.get_json()
    meal.name = data.get('name', meal.name)
    meal.description = data.get('description', meal.description)
    meal.date_time = datetime.fromisoformat(data.get('date_time', meal.date_time.isoformat()))  # Convertendo a string para datetime
    meal.in_diet = data.get('in_diet', meal.in_diet)
    db.session.commit()
    return jsonify(meal.to_dict())

@bp.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
    meal = Meal.query.get_or_404(id)
    db.session.delete(meal)
    db.session.commit()
    return '', 204

@bp.route('/meals', methods=['GET'])
def get_meals():
    meals = Meal.query.all()
    return jsonify([meal.to_dict() for meal in meals])

@bp.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    meal = Meal.query.get_or_404(id)
    return jsonify(meal.to_dict())
