import pytest
from database.models import db, Scholarship
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", "TESTING": True})
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_add_scholarship(app):
    from database.queries import add_scholarship
    data = {"title": "Test", "url": "http://test.com"}
    scholarship = add_scholarship(data)
    assert scholarship.id is not None
