# Product Management Suite

A comprehensive inventory, sales, and customer management system built with Django and Supabase.

## 🚀 Features

- **Inventory Management** - Complete stock control with product tracking, categorization, and real-time updates
- **Sales System** - Sales recording, tracking, and automatic calculations with tax integration
- **Customer Management** - Complete CRM with customer database and contact management
- **Real-Time Reports** - Interactive dashboards and charts with Chart.js
- **REST API** - Full-featured API built with Django REST Framework
- **Multi-Platform** - Web interface + mobile app integration via API
- **User Interface** - 8 fully functional screens with Bootstrap 5 responsive design

## 📊 Interface Overview

### **Dashboard** (`Imagen1.jpg`)
- Main control panel with monthly sales overview
- Quick actions panel for common operations
- Inventory status and alerts
- Left navigation menu with all modules

### **Product Management** (`Imagen3.jpg`, `Imagen4.jpg`)
- Product inventory with advanced search and filtering
- Product creation form with SKU and barcode support
- Category management system
- Stock level tracking and alerts

### **Customer Management** (`Imagen5.jpg`, `Imagen6.jpg`)
- Customer database with search capabilities
- Detailed customer registration (tax ID, contact info, address)
- Customer type filtering (Individual/Company)
- Notes and additional information fields

### **Sales Management** (`Imagen7.jpg`, `Imagen8.jpg`)
- Sales tracking with date filtering
- Financial KPIs (Total Sales, Revenue, Paid/Pending)
- Sales creation interface with automatic calculations
- Product selection and quantity management
- Tax calculation (12%) and payment method tracking



## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | Django 4.x | Web framework for rapid development |
| **API** | Django REST Framework | RESTful API for web + mobile integration |
| **Database** | PostgreSQL (Supabase) | Cloud-native database with real-time capabilities |
| **Frontend** | Bootstrap 5 | Responsive UI components and layout |
| **Charts** | Chart.js | Interactive data visualization |
| **Templates** | Django Templates | Server-side rendering with Django |
| **Authentication** | Django User System | User management and permissions |
| **Deployment** | (Configurable) | AWS/Heroku/DigitalOcean ready |



## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Presentation Layer                   │
│  Bootstrap 5 + Django Templates + 8 Interface Screens   │
└──────────────────────────┬──────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                    Business Logic Layer                 │
│  Django Views + REST API + 4 Core Business Modules      │
└──────────────────────────┬──────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                      Data Layer                         │
│         Supabase PostgreSQL + Django Models             │
└─────────────────────────────────────────────────────────┘
```



## 🔌 REST API Endpoints

| Module | Endpoint | Method | Description |
|--------|----------|--------|-------------|
| **Products** | `/api/products/` | `GET` / `POST` | List all products or create new |
| **Products** | `/api/products/search/` | `GET` | Search products by query or barcode |
| **Sales** | `/api/sales/quick_sale/` | `POST` | Register fast sale transaction |
| **Sales** | `/api/sales/top_products/` | `GET` | Get top-selling products |
| **Clients** | `/api/clients/search/` | `GET` | Search clients by name, email, or tax ID |
| **Inventory** | `/api/inventory/low_stock/` | `GET` | Get products with low stock levels |
| **Reports** | `/api/reports/sales_summary/` | `GET` | Get sales summary for dashboard |

### Sample API Request
```python
POST /api/sales/quick_sale/
Content-Type: application/json

{
    "product_id": 123,
    "quantity": 2,
    "customer_id": 456,
    "payment_method": "credit_card"
}
```




## 📦 Installation & Setup

### 1. Prerequisites
```bash

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
