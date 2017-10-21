"""To handle all manager commands from the command line"""
from flask_script import Manager

from project import APP

MANAGER = Manager(APP)

if __name__ == '__main__':
    MANAGER.run()
