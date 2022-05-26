from app import app
from db import db

db.init_app(app)

@app.before_first_rerquest
def create_tables():
    db.create_all()
