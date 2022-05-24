from app import app, db

@app.shell_context_processor
def make_context():
    return { 'db': db}