"""To handle all manager commands from the command line"""
from flask_script import Manager

from project import APP, db

MANAGER = Manager(APP)

@MANAGER.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    MANAGER.run()
