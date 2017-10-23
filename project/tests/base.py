"""Base test class"""

from flask_testing import TestCase

from project import APP, db

class BaseTestCase(TestCase):
    """Base test case"""
    def create_app(self):
        """Check app settings"""
        APP.config.from_object('project.config.TestingConfig')
        return APP

    def set_up(self):
        """Check db setup"""
        db.create_all()
        db.session.commit()

    def tear_down(self):
        """Check db drop"""
        db.session.remove()
        db.drop_all()
