"""Unit test config"""

import unittest

from flask import current_app
from flask_testing import TestCase
from project import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    """Test dev config"""
    def create_app(self):
        """check dev app creation"""
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        """assert dev configs"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@fma-db:5432/fma_dev'
        )

class TestTestingConfig(TestCase):
    """Test testing config"""
    def create_app(self):
        """check testing app creation"""
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        """assert testing configs"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@fma-db:5432/fma_test'
        )


class TestProductionConfig(TestCase):
    """Test prod config"""
    def create_app(self):
        """check prod app creation"""
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        """assert prod configs"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
