# E-commerce API

## Overview

The E-commerce API is a RESTful API designed for managing customers, products, and orders within an e-commerce platform. Built using Flask and SQLAlchemy, the API supports CRUD operations, user authentication with JWT, caching, rate limiting, and detailed API documentation.

## Features

- **Customer Management**: Create, read, update, and delete customer records.
- **Product Management**: Add new products, retrieve product details, update product information, and delete products. List all products.
- **Order Processing**: Place new orders and retrieve order details.
- **Authentication**: Secure API endpoints with JWT (JSON Web Tokens).
- **Rate Limiting**: Limit API requests to prevent abuse.
- **Caching**: Cache responses to improve performance.
- **API Documentation**: Comprehensive documentation using Swagger.

## Project Structure


## Setup

### Prerequisites

- Python 3.8 or higher
- MySQL database

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables:**

    Create a `.env` file in the root directory and add the following:

    ```plaintext
    DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
    JWT_SECRET_KEY=your_jwt_secret_key
    ```

    - Replace `user`, `password`, and `dbname` with your MySQL database credentials.
    - Replace `your_jwt_secret_key` with a secure key for JWT.

5. **Initialize the database:**

    Create the database schema by running:

    ```bash
    flask db upgrade
    ```

6. **Run the application:**

    Start the Flask application with:

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Customers

- **Create Customer**
    - **Endpoint:** `/api/customers`
    - **Method:** POST
    - **Request Body:**
      ```json
      {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
      }
      ```
    - **Response:** `201 Created`
    - **Description:** Creates a new customer with the provided details.

- **Get Customer by ID**
    - **Endpoint:** `/api/customers/{id}`
    - **Method:** GET
    - **Response:** `200 OK`
    - **Example Response:**
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
      }
      ```
    - **Description:** Retrieves details of a customer by their ID.

- **Update Customer**
    - **Endpoint:** `/api/customers/{id}`
    - **Method:** PUT
    - **Request Body:**
      ```json
      {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "0987654321"
      }
      ```
    - **Response:** `200 OK`
    - **Description:** Updates the details of an existing customer.

- **Delete Customer**
    - **Endpoint:** `/api/customers/{id}`
    - **Method:** DELETE
    - **Response:** `204 No Content`
    - **Description:** Deletes a customer record.

### Products

- **Create Product**
    - **Endpoint:** `/api/products`
    - **Method:** POST
    - **Request Body:**
      ```json
      {
        "name": "Product A",
        "price": 29.99
      }
      ```
    - **Response:** `201 Created`
    - **Description:** Adds a new product to the catalog.

- **Get Product by ID**
    - **Endpoint:** `/api/products/{id}`
    - **Method:** GET
    - **Response:** `200 OK`
    - **Example Response:**
      ```json
      {
        "id": 1,
        "name": "Product A",
        "price": 29.99
      }
      ```
    - **Description:** Retrieves details of a product by its ID.

- **Update Product**
    - **Endpoint:** `/api/products/{id}`
    - **Method:** PUT
    - **Request Body:**
      ```json
      {
        "name": "Product B",
        "price": 34.99
      }
      ```
    - **Response:** `200 OK`
    - **Description:** Updates the details of an existing product.

- **Delete Product**
    - **Endpoint:** `/api/products/{id}`
    - **Method:** DELETE
    - **Response:** `204 No Content`
    - **Description:** Deletes a product from the catalog.

- **List Products**
    - **Endpoint:** `/api/products`
    - **Method:** GET
    - **Response:** `200 OK`
    - **Example Response:**
      ```json
      [
        {
          "id": 1,
          "name": "Product A",
          "price": 29.99
        },
        {
          "id": 2,
          "name": "Product B",
          "price": 34.99
        }
      ]
      ```
    - **Description:** Lists all products available in the catalog.

### Orders

- **Place Order**
    - **Endpoint:** `/api/orders`
    - **Method:** POST
    - **Request Body:**
      ```json
      {
        "order_date": "2024-09-04T00:00:00",
        "customer_id": 1,
        "product_ids": [1, 2]
      }
      ```
    - **Response:** `201 Created`
    - **Description:** Places a new order with the specified products and customer.

- **Get Order by ID**
    - **Endpoint:** `/api/orders/{id}`
    - **Method:** GET
    - **Response:** `200 OK`
    - **Example Response:**
      ```json
      {
        "id": 1,
        "order_date": "2024-09-04T00:00:00",
        "customer_id": 1,
        "products": [
          {
            "id": 1,
            "name": "Product A",
            "price": 29.99
          },
          {
            "id": 2,
            "name": "Product B",
            "price": 34.99
          }
        ]
      }
      ```
    - **Description:** Retrieves details of an order by its ID.

## Authentication

- **Login**
    - **Endpoint:** `/api/login`
    - **Method:** POST
    - **Request Body:**
      ```json
      {
        "username": "user",
        "password": "password"
      }
      ```
    - **Response:** `200 OK`
    - **Response Body:**
      ```json
      {
        "access_token": "your_jwt_token"
      }
      ```
    - **Description:** Authenticates a user and returns a JWT token.

- **Protected Routes**
    - Include the JWT token in the `Authorization` header for requests to protected endpoints:
      ```
      Authorization: Bearer <your_jwt_token>
      ```

## Rate Limiting

- **Rate Limit:** All API endpoints are rate-limited to 100 requests per day per user. This helps prevent abuse and ensures fair usage of the API.

## Caching

- **Caching Strategy:** API responses are cached to improve performance. Cached responses reduce the load on the server and improve response times for frequently accessed data.

## Testing

### Running Tests

To run the unit tests:

```bash
python -m unittest discover -s tests
