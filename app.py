from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from database.models import db, User
from api.routes import api_bp
from utils.logger import init_logger
from utils.validator import is_valid_email
from scraper.scraper import fetch_scholarships

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config_class)
    
    # Logger
    init_logger(app)
    
    # Database
    db.init_app(app)
    
    # API routes
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Health check
    @app.route("/health")
    def health_check():
        return {"status": "ok"}, 200

    # Home page
    @app.route("/")
    def index():
        return render_template("index.html")
    
    # Results page
    @app.route("/results")
    def results():
        query = request.args.get("query", "")
        scholarships = fetch_scholarships("https://example.com/scholarships")
        if query:
            scholarships = [s for s in scholarships if query.lower() in s['title'].lower()]
        return render_template("results.html", scholarships=scholarships)

    # Login page
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            if not is_valid_email(email):
                flash("Invalid email!", "error")
                return redirect(url_for("login"))
            user = User.query.filter_by(email=email).first()
            if user and user.password_hash == password:  # Replace with hashed check
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))
            flash("Invalid credentials!", "error")
            return redirect(url_for("login"))
        return render_template("login.html")

    # Dashboard page
    @app.route("/dashboard")
    def dashboard():
        user = User.query.first()  # Dummy user for demo
        return render_template("dashboard.html", user=user)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
