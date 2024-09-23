import unittest
from app.utils.app import create_app, db

class TestOrder(unittest.TestCase):
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

    def test_place_order(self):
        response = self.client.post('/api/orders', json={'order_date': '2023-01-01', 'customer_id': 1, 'product_ids': [1]})
        self.assertEqual(response.status_code, 201)

    # Add more tests for retrieve order

if __name__ == '__main__':
    unittest.main()
