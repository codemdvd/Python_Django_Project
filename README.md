# Engine Parts & Logistics Management System

A full-stack web application for managing orders, inventory, clients, employees, and shipments in an automotive parts distribution company. Built with Django and PostgreSQL.

---

## Overview

This system automates the core business workflow of an auto parts distributor:

- Sales staff create and track customer orders
- Logistics team monitors incoming shipments and stock levels
- Admins manage employees and access rights
- All roles work within a single web interface with role-based access control

---

## Features

| Module | Capabilities |
|---|---|
| **Orders** | Create, view, update orders; add products to orders; track delivery status |
| **Inventory** | Browse parts catalog with search; track stock counts, part numbers, brands, prices |
| **Shipments** | Track incoming deliveries with send/receive dates, weight, and status |
| **Clients** | Search clients; view contact info, personal discounts, and linked vehicles |
| **Employees** | Register staff; assign roles (Admin / Employee / Logistics) |
| **Vehicles** | Store VIN codes, brands, engine types linked to client records |
| **Reports** | Export data to CSV; generate manager-level reports |

---

## Tech Stack

**Backend**
- Python 3.10
- Django 4.0.5
- PostgreSQL 14+
- Django ORM + raw SQL (stored procedures for complex operations)

**Frontend**
- Django Templates
- HTML5 / CSS3 (Flexbox layout)
- Custom template tags for permission checks

**Auth & Permissions**
- Django built-in User / Group authentication
- Three access groups: `Admin`, `Employee`, `Logistics`
- Decorator and template-level permission enforcement

---

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Python_Django_Project.git
cd Python_Django_Project

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Database Setup

```sql
-- In psql, create the database
CREATE DATABASE engine_details;
```

```bash
# Apply Django migrations
python manage.py migrate
```

> **Note:** The app connects to PostgreSQL at `127.0.0.1:5432` with user `postgres`.  
> Update `web_project/settings.py` → `DATABASES` if your credentials differ.

### Run the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Create an Admin User

```bash
python manage.py createsuperuser
```

Then log in at `/admin/` to create Groups (`Admin`, `Employee`, `Logistics`) and assign users.

---

## Project Structure

```
Python_Django_Project/
├── manage.py
├── requirements.txt
├── web_project/              # Project configuration
│   ├── settings.py
│   └── urls.py
└── hello/                    # Main application
    ├── models.py             # 12 business models
    ├── views.py              # 20+ view functions
    ├── forms.py              # ModelForms + auth forms
    ├── urls.py               # URL routing
    ├── admin.py
    ├── migrations/
    ├── templates/hello/      # 24 HTML templates
    ├── static/hello/         # CSS assets
    └── templatetags/
        └── hello_extras.py   # has_group template filter
```

---

## Data Model

```
Client ──< Cars
Client ──< OrderTable ──< OrderProduct >── Product
                                           Product ──< IncomeProduct >── Income

Employee ── RoleClassifier
OrderTable ── OrderStausClassifier
OrderTable ── DeliveryClassifier
```

---

## URL Map

| URL | Access | Description |
|---|---|---|
| `/` | Public | Login |
| `/register/` | Public | Register new user |
| `/clients/` | All | Search clients |
| `/product/` | All | Browse inventory |
| `/all_tasks/` | Employee | All orders with search |
| `/new_task/` | Employee | Create order |
| `/update_order/` | Employee | Edit order |
| `/income/` | Logistics | Incoming shipments |
| `/employees/` | Admin | Staff list |
| `/new_emp/` | Admin | Register employee |
| `/report/` | Admin | Export / reports |

---

## Author

**Vasily Apasov**  
[GitHub](https://github.com/VasilyApasov) · [LinkedIn](https://www.linkedin.com/in/vasily-apasov)

---

## License

This project is for portfolio and demonstration purposes.
