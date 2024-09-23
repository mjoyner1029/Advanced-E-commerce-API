import unittest
from app.utils.app import create_app, db

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_customer(self):
        response = self.client.post('/api/customers', json={'name': 'John Doe', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 201)

    # Add more tests for read, update, delete

if __name__ == '__main__':
    unittest.main()
