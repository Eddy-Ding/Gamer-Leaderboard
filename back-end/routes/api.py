from flask import Blueprint, jsonify
from pymongo import MongoClient

api_bp = Blueprint('api', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['ultimate_gamer']

@api_bp.route('/leaderboard', methods=['GET'])
def leaderboard():
    users = db.users.find()
    leaderboard = sorted(users, key=lambda x: x['stats'].get('total_points', 0), reverse=True)
    return jsonify(list(leaderboard))
