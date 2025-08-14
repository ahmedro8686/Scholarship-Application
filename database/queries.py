from database.models import db, Scholarship, User
from sqlalchemy.exc import SQLAlchemyError

def add_scholarship(data):
    try:
        scholarship = Scholarship(**data)
        db.session.add(scholarship)
        db.session.commit()
        return scholarship
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def get_all_scholarships():
    return Scholarship.query.order_by(Scholarship.deadline.asc()).all()

def find_scholarships_by_country(country):
    return Scholarship.query.filter_by(country=country).all()
