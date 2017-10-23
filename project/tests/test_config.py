"""Unit test config"""

import unittest

from flask import current_app
from flask_testing import TestCase

from project import APP

class TestDevelopmentConfig(TestCase):
    """Test dev config"""
    def create_app(self):
        """check dev app creation"""
        APP.config.from_object('project.config.DevelopmentConfig')
        return APP

    def test_app_is_development(self):
        """assert dev configs"""
        self.assertTrue(APP.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(APP.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            APP.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@fma-db:5432/fma_dev'
        )

class TestTestingConfig(TestCase):
    """Test testing config"""
    def create_app(self):
        """check testing app creation"""
        APP.config.from_object('project.config.TestingConfig')
        return APP

    def test_app_is_testing(self):
        """assert testing configs"""
        self.assertTrue(APP.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(APP.config['DEBUG'])
        self.assertTrue(APP.config['TESTING'])
        self.assertFalse(APP.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            APP.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@fma-db:5432/fma_test'
        )


class TestProductionConfig(TestCase):
    """Test prod config"""
    def create_app(self):
        """check prod app creation"""
        APP.config.from_object('project.config.ProductionConfig')
        return APP

    def test_app_is_production(self):
        """assert prod configs"""
        self.assertTrue(APP.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(APP.config['DEBUG'])
        self.assertFalse(APP.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
