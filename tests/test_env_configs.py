import unittest
from app import create_app
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask import current_app
from flask_testing import TestCase


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app = create_app(DevelopmentConfig)
        return app

    def test_app_is_development(self):
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['FLASK_ENV'], 'development')

        self.assertTrue(current_app.config['DEBUG'])
        self.assertFalse(current_app.config['TESTING'])

        self.assertEqual(current_app.config['SECRET_KEY'], 'sp-clone-secret')
        self.assertEqual(current_app.config['SQLALCHEMY_DATABASE_URI'],
                         'postgresql://postgres:@localhost/sp_clone')


class TestProductionConfig(TestCase):

    def create_app(self):
        app = create_app(ProductionConfig)
        return app

    def test_app_is_production(self):
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['FLASK_ENV'], 'production')

        self.assertFalse(current_app.config['DEBUG'])
        self.assertFalse(current_app.config['TESTING'])


class TestTestingConfig(TestCase):

    def create_app(self):
        app = create_app(TestingConfig)
        return app

    def test_app_is_testing(self):
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['FLASK_ENV'], 'testing')

        self.assertTrue(current_app.config['DEBUG'])
        self.assertTrue(current_app.config['TESTING'])

        self.assertNotEqual(current_app.config['SECRET_KEY'], 'my_precious')
        self.assertEqual(current_app.config['SQLALCHEMY_DATABASE_URI'],
                         'postgresql://postgres:@localhost/sp_clone_test')


if __name__ == '__main__':
    unittest.main()
