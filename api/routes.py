from flask import Blueprint, jsonify
from database.queries import get_all_scholarships

api_bp = Blueprint("api", __name__)

@api_bp.route("/scholarships", methods=["GET"])
def scholarships_list():
    scholarships = get_all_scholarships()
    return jsonify([{
        "title": s.title,
        "description": s.description,
        "country": s.country,
        "level": s.level,
        "deadline": s.deadline.isoformat() if s.deadline else None,
        "url": s.url
    } for s in scholarships])
