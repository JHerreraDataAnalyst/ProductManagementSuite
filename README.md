# Product Management Suite

A comprehensive inventory, sales, and customer management system built with Django and Supabase.

## 🚀 Features

- **Inventory Management** - Stock and product control
- **Sales System** - Sales recording and tracking
- **Customer Management** - Customer database
- **Real-Time Reports** - Charts with Chart.js
- **REST API** - Product configuration with Django REST Framework

## 🛠️ Technologies

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (Supabase)
- **Frontend:** Bootstrap 5, Chart.js
- **Authentication:** Django user system

## 📦 Installation

1. Clone the repository:
```bash
git clone [https://github.com/YourUsername/ProductManagementSuite.git](https://github.com/YourUsername/ProductManagementSuite.git)
cd ProductManagementSuite
```
2.  Install Python dependencies (assuming you have a virtual environment active):
```bash
pip install -r requirements.txt
```

3.  Apply database migrations and create a superuser for administration:
```bash
python manage.py migrate
python manage.py createsuperuser
```
4.  Run the development server:
```bash
python manage.py runserver
```
The web application will be accessible at http://127.0.0.1:8000/.
---

## 🔗 REST API Endpoints (Django REST Framework)

The backend provides a comprehensive API, also used by the companion mobile application (Inventory Mobile App).

| Module | Endpoint | Method | Description |
| :--- | :--- | :--- | :--- |
| **Products** | `/api/products/` | `GET` / `POST` | List all products or create a new one. |
| **Products** | `/api/products/search/` | `GET` | Search products by query or barcode. |
| **Sales** | `/api/sales/quick_sale/` | `POST` | Register a new fast sale transaction. |
| **Sales** | `/api/sales/top_products/` | `GET` | Get a list of top-selling products. |
| **Clients** | `/api/clients/search/` | `GET` | Search clients by name, email, or tax ID. |

---

## ⚖️ License

This project is licensed under the **MIT License**.
