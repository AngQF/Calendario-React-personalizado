"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, CalendarAvailability
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/available_datetime', methods=['GET'])
def get_available_datetime():
    current_user_id = get_jwt_identity()
    user = Users.query.get(current_user_id)
    dates = CalendarAvailability.query.filter(CalendarAvailability.is_available == True)
    dates_serialized = list(map(lambda x: x.serialize(), dates))
    if user:
        return jsonify({"resp": dates_serialized}), 200
    else: return jsonify({"No se ha podido traer la información"}), 400

@api.route('/available_datetime/<body_date>', methods=['GET'])
def get_available_datetime_of_selected_date(body_date):
    current_user_id = get_jwt_identity()
    user = Users.query.get(current_user_id)
    datetime = CalendarAvailability.query.filter(CalendarAvailability.date == body_date, CalendarAvailability.is_available == True)
    datetime_serialized = list(map(lambda x: x.serialize(), datetime))
    if user:
        return jsonify({"resp": datetime_serialized}), 200
    else: return jsonify({"No se ha podido traer la información"}), 400      