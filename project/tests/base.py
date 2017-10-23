"""Base test class"""

from flask_testing import TestCase

from project import create_app, db

app = create_app()

class BaseTestCase(TestCase):
    """Base test case"""
    def create_app(self):
        """Check app settings"""
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        """Check db setup"""
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """Check db drop"""
        db.session.remove()
        db.drop_all()
