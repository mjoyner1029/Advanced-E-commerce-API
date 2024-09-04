import unittest
from app import create_app, db
from app.models.customer import Customer

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_customer(self):
        response = self.client.post('/api/customers', json={'name': 'John Doe', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 201)

    def test_get_customer(self):
        response = self.client.post('/api/customers', json={'name': 'Jane Doe', 'email': 'jane@example.com'})
        customer_id = response.json['id']
        response = self.client.get(f'/api/customers/{customer_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        response = self.client.post('/api/customers', json={'name': 'Mike', 'email': 'mike@example.com'})
        customer_id = response.json['id']
        response = self.client.put(f'/api/customers/{customer_id}', json={'name': 'Michael'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Michael')

    def test_delete_customer(self):
        response = self.client.post('/api/customers', json={'name': 'Alex', 'email': 'alex@example.com'})
        customer_id = response.json['id']
        response = self.client.delete(f'/api/customers/{customer_id}')
        self.assertEqual(response.status_code, 204)
