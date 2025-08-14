# app.py
from flask import Flask, render_template, request
from database.models import db, Scholarship
from utils.filters import filter_scholarships
from config import Config

# Import blueprints لو عملت Routes منفصلة
# from routes.scraper_routes import scraper_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # تهيئة قاعدة البيانات
    db.init_app(app)

    # تسجيل Blueprints (لو فيه)
    # app.register_blueprint(scraper_bp)

    @app.route("/", methods=["GET", "POST"])
    def index():
        results = []
        query_params = {}

        if request.method == "POST":
            country = request.form.get("country")
            field = request.form.get("field")
            degree = request.form.get("degree")

            query_params = {
                "country": country,
                "field": field,
                "degree": degree
            }

            # جلب المنح من قاعدة البيانات
            scholarships = Scholarship.query.all()

            # تطبيق الفلترة
            results = filter_scholarships(scholarships, query_params)

        return render_template("index.html", results=results, query=query_params)

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # إنشاء الجداول إذا لم تكن موجودة
    app.run(debug=True)
