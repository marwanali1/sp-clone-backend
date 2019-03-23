# Python script at the top-level that defines the Flask application instance
from app import create_app, db
from app.models import User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    shell_instances = {'db': db, 'User': User}
    return shell_instances
