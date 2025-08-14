from database.models import db, create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("Database and tables created successfully.")
