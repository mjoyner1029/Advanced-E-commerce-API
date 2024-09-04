from app.models.customer import Customer

def get_customer_by_id(customer_id):
    return Customer.query.get(customer_id)
