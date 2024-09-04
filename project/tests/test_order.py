import unittest
from app import create_app, db
from app.models.order import Order
from app.models.product import Product
from app.models.customer import Customer

class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

            # Create a customer and product for order testing
            self.customer = Customer(name='Customer1', email='customer1@example.com')
            db.session.add(self.customer)
            self.product = Product(name='Product1', price=10.00)
            db.session.add(self.product)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_place_order(self):
        response = self.client.post('/api/orders', json={
            'order_date': '2024-09-04T00:00:00',
            'customer_id': self.customer.id,
            'product_ids': [self.product.id]
        })
        self.assertEqual(response.status_code, 201)

    def test_get_order(self):
        response = self.client.post('/api/orders', json={
            'order_date': '2024-09-04T00:00:00',
            'customer_id': self.customer.id,
            'product_ids': [self.product.id]
        })
        order_id = response.json['id']
        response = self.client.get(f'/api/orders/{order_id}')
        self.assertEqual(response.status_code, 200)
