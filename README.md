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

### **Dashboard**
![Dashboard Interface](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen1.jpg?raw=true)
- Main control panel with monthly sales overview
- Quick actions panel for common operations
- Inventory status and alerts
- Left navigation menu with all modules

### **Product Management**
| Inventory View | Create Product |
|----------------|----------------|
| ![Product Inventory](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen3.jpg?raw=true) | ![Create Product](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen4.jpg?raw=true) |

- Product inventory with advanced search and filtering
- Product creation form with SKU and barcode support
- Category management system
- Stock level tracking and alerts

### **Customer Management**
| Customer List | Create Customer |
|---------------|-----------------|
| ![Customer List](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen5.jpg?raw=true) | ![Create Customer](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen6.jpg?raw=true) |

- Customer database with search capabilities
- Detailed customer registration (tax ID, contact info, address)
- Customer type filtering (Individual/Company)
- Notes and additional information fields

### **Sales Management**
| Sales Overview | Create Sale |
|----------------|-------------|
| ![Sales Management](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen7.jpg?raw=true) | ![Create Sale](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen8.jpg?raw=true) |

- Sales tracking with date filtering
- Financial KPIs (Total Sales, Revenue, Paid/Pending)
- Sales creation interface with automatic calculations
- Product selection and quantity management
- Tax calculation (12%) and payment method tracking

---

**Gallery View - All Interfaces**
| Dashboard | Product Inventory | Create Product | Customer List |
|-----------|-------------------|----------------|---------------|
| ![Dashboard](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen1.jpg?raw=true) | ![Product Inventory](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen3.jpg?raw=true) | ![Create Product](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen4.jpg?raw=true) | ![Customer List](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen5.jpg?raw=true) |

| Create Customer | Sales Management | Create Sale |
|-----------------|------------------|-------------|
| ![Create Customer](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen6.jpg?raw=true) | ![Sales Management](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen7.jpg?raw=true) | ![Create Sale](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/blob/main/static/images/Imagen8.jpg?raw=true) |


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
Python 3.8+
PostgreSQL (or Supabase account)
Git
```

### 2. Clone Repository
```bash
git clone https://github.com/JHerreraDataAnalyst/ProductManagementSuite.git
cd ProductManagementSuite
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate    # Windows
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create `.env` file in project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Supabase Configuration
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
DATABASE_URL=postgresql://user:password@host:port/database

# Email Configuration (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
```

### 6. Database Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load initial data (optional)
python manage.py loaddata initial_data.json
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**



## 📁 Project Structure

```
ProductManagementSuite/
├── api/                    # REST API app
│   ├── views.py           # API views
│   ├── serializers.py     # Data serializers
│   └── urls.py            # API endpoints
├── clients/               # Customer management app
│   ├── models.py          # Customer models
│   ├── views.py           # Customer views
│   └── templates/         # Customer templates
├── products/              # Product management app
│   ├── models.py          # Product models
│   ├── views.py           # Product views
│   └── templates/         # Product templates
├── sales/                 # Sales management app
│   ├── models.py          # Sales models
│   ├── views.py           # Sales views
│   └── templates/         # Sales templates
├── dashboard/             # Dashboard app
│   ├── views.py           # Dashboard views
│   └── templates/         # Dashboard templates
├── templates/             # Base templates
│   ├── base.html          # Base template
│   └── navigation/        # Navigation components
├── inventory_project/     # Main project config
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URLs
│   └── wsgi.py            # WSGI config
├── static/                # Static files
│   ├── css/               # CSS files
│   ├── js/                # JavaScript files
│   ├── images/            # Images (8 interface screens)
│   └── fonts/             # Font files
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── manage.py              # Django management script
└── README.md              # This file
```



## 🧪 Django Models

### Product Model
```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    barcode = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def is_in_stock(self):
        return self.stock_quantity > 0
```

### Customer Model
```python
class Customer(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company'),
    ]
    
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES)
    tax_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

### Sale Model
```python
class Sale(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('transfer', 'Bank Transfer'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    is_paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Sale #{self.id} - {self.customer}"
```



## 📊 Key Features Detailed

### Inventory Management
- **Real-time stock tracking** with automatic updates
- **Barcode scanning** support for quick product lookup
- **Category management** for product organization
- **Low stock alerts** and reorder notifications
- **Batch operations** for bulk updates

### Sales Processing
- **Quick sale** functionality for fast transactions
- **Automatic tax calculation** (12% configurable)
- **Multiple payment methods** support
- **Sales history** with detailed tracking
- **Invoice generation** (PDF export)

### Customer Relationship
- **Complete customer profiles** with contact information
- **Purchase history** tracking per customer
- **Customer segmentation** by type and purchase behavior
- **Notes and follow-ups** for customer interactions

### Reporting & Analytics
- **Real-time dashboard** with key business metrics
- **Sales trends** and performance analysis
- **Inventory turnover** reports
- **Customer analytics** and segmentation
- **Export functionality** to Excel/PDF


## 🔐 Authentication & Security

### User Management
- Django's built-in authentication system
- Role-based access control (Admin/Staff/User)
- Secure password hashing and storage
- Session management and timeout

### Security Features
- CSRF protection enabled
- XSS protection headers
- SQL injection prevention
- Secure password validation
- HTTPS enforcement in production

### API Security
- Token authentication for API endpoints
- Rate limiting on sensitive endpoints
- Input validation and sanitization
- CORS configuration for frontend access


## 🚀 Deployment

### Option 1: Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(50))")
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Option 2: DigitalOcean
```bash
# Create Droplet with Django One-Click App
# Configure domain and SSL
# Set up PostgreSQL database
# Deploy using Git or CI/CD
```

### Option 3: AWS
```bash
# Use Elastic Beanstalk for Django
# Configure RDS for PostgreSQL
# Set up S3 for static/media files
# Configure CloudFront for CDN
```

### Environment Configuration for Production
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
```




## 📈 Performance Optimizations

### Database Optimization
- **Indexing** on frequently queried fields
- **Query optimization** using Django's ORM best practices
- **Database connection pooling** with PGBouncer
- **Caching** with Redis for frequent queries

### Frontend Optimization
- **Lazy loading** for images and components
- **Minification** of CSS and JavaScript
- **CDN** for static assets
- **Browser caching** headers

### Backend Optimization
- **Gunicorn** with multiple workers for production
- **Nginx** as reverse proxy and load balancer
- **Database connection reuse**
- **Background tasks** with Celery for heavy operations



## 🧪 Testing

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test products

# Run with coverage
coverage run manage.py test
coverage report
coverage html
```

### Test Structure
```python
# Example test for product creation
class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=99.99,
            stock_quantity=10,
            barcode="123456789",
            category=self.category
        )
        self.assertEqual(product.name, "Test Product")
        self.assertTrue(product.is_in_stock())
```

### API Testing
```python
# Using Django REST Framework test client
class APITestCase(APITestCase):
    def test_product_api(self):
        url = '/api/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
```




## 🔄 Development Workflow

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new-module

# Make changes and commit
git add .
git commit -m "Add new inventory module"

# Push to remote
git push origin feature/new-module

# Create pull request
# Merge after code review
```

### Code Quality
```bash
# Run linter
flake8 .

# Format code
black .

# Sort imports
isort .

# Type checking (if using type hints)
mypy .
```

### Continuous Integration
Example `.github/workflows/ci.yml`:
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: python manage.py test
```



## 📝 API Documentation

### Authentication
```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "admin",
    "password": "password123"
}
```

### Products API
```http
GET /api/products/
Authorization: Token your-token-here

Response:
[
    {
        "id": 1,
        "name": "Product Name",
        "price": "99.99",
        "stock_quantity": 50,
        "category": "Electronics"
    }
]
```

### Sales API
```http
POST /api/sales/quick_sale/
Content-Type: application/json
Authorization: Token your-token-here

{
    "product_id": 1,
    "quantity": 2,
    "customer_id": 1,
    "payment_method": "cash"
}
```


## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write tests for new features
- Update documentation when adding/changing features
- Use meaningful commit messages
- Keep pull requests focused on single features


## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 José Herrera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



## 👤 Author

**José Herrera**

- GitHub: [@JHerreraDataAnalyst](https://github.com/JHerreraDataAnalyst)
- LinkedIn: [José Herrera](https://www.linkedin.com/in/jose-herrera-044b2681)
- Portfolio: [Data Analytics Portfolio](https://your-portfolio-link.com)

## 🙏 Acknowledgments

- **Django** team for the amazing web framework
- **Supabase** for the excellent PostgreSQL hosting
- **Bootstrap** team for the responsive CSS framework
- **Chart.js** for interactive data visualization
- All contributors and users of this project


## 📞 Support

For support, email **josehb1995@hotmail.com** or open an issue in the [GitHub repository](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/issues).

## 📊 Project Status

**Version**: 1.0.0  
**Status**: Active Development  
**Last Updated**: November 2025  
**Next Release**: v1.1.0 (Mobile App Integration)



---

## 🔗 Quick Links

- [Live Demo](#) *(Coming soon)*
- [API Documentation](#api-documentation)
- [Issue Tracker](https://github.com/JHerreraDataAnalyst/ProductManagementSuite/issues)
- [Changelog](CHANGELOG.md)
- [Contributing Guidelines](#contributing)

*Note: Replace `#` links with actual URLs when available.*
