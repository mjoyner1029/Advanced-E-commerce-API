import unittest
from app.utils.app import create_app, db

class TestProduct(unittest.TestCase):
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

    def test_create_product(self):
        response = self.client.post('/api/products', json={'name': 'Product 1', 'price': 10.0})
        self.assertEqual(response.status_code, 201)

    # Add more tests for read, update, delete

if __name__ == '__main__':
    unittest.main()
