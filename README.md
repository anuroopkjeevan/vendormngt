# Django Vendor Management System


## Features

1. **Vendor Profile Management:**
    - Create, retrieve, update, and delete vendor profiles.
2. **Purchase Order Tracking:**
    - Create, retrieve, update, and delete purchase orders.
    - Filter purchase orders by vendor.
3. **Vendor Performance Evaluation:**
    - Retrieve vendor performance metrics.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/django-vendor-management.git
cd django-vendor-management
Create a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Apply migrations:
bash
Copy code
python manage.py migrate
Create a superuser account:
bash
Copy code
python manage.py createsuperuser
Run the development server:
bash
Copy code
python manage.py runserver
#  use the postman to check the working of the  api end points  
API Endpoints
Vendor Management:
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
PUT /api/vendors/{vendor_id}/: Update a vendor's details.
DELETE /api/vendors/{vendor_id}/: Delete a vendor.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Purchase Order Tracking:
POST /api/purchase_orders/: Create a purchase order.
GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
PUT /api/purchase_orders/{po_id}/: Update a purchase order.
DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Vendor Performance Evaluation:
GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.
Backend Logic for Performance Metrics
On-Time Delivery Rate
Quality Rating Average
Average Response Time
Fulfilment Rate
Additional Considerations
Efficient Calculation
Data Integrity
Real-time Updates

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Technical Requirements
Django version:  4.2.7
RESTful API design
Data validations
Django ORM for database interactions
Token-based authentication  : Jwt token used for the authentication
Testing
Run the test suite:

python manage.py test
