import unittest
from app import create_app, db
from app.models.product import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_product(self):
        response = self.client.post('/api/products', json={'name': 'Product1', 'price': 10.99})
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        response = self.client.post('/api/products', json={'name': 'Product2', 'price': 15.49})
        product_id = response.json['id']
        response = self.client.get(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        response = self.client.post('/api/products', json={'name': 'Product3', 'price': 20.00})
        product_id = response.json['id']
        response = self.client.put(f'/api/products/{product_id}', json={'price': 22.50})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['price'], 22.50)

    def test_delete_product(self):
        response = self.client.post('/api/products', json={'name': 'Product4', 'price': 30.00})
        product_id = response.json['id']
        response = self.client.delete(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 204)
