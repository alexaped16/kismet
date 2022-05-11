from app import app, db
from app.models import Contact

@app.shell_context_processor
def make_context():
    return { 'db': db}