# Employee Leave & Asset Management System

A Django-based web application for managing employees, leave requests, and company asset requests.

This project was developed to practice backend web development using **Python and Django**, including authentication, database operations, CRUD functionality, Django ORM, forms, URL routing, and Django Admin.

## Features

### User Authentication

* User registration
* User login and logout
* Password change
* User authentication and protected pages

### Employee Management

* Employee profiles
* Department management
* Profile image upload
* Edit employee profile
* Active/inactive employee status

### Leave Management

* Apply for leave
* Leave types:

  * Sick Leave
  * Casual Leave
  * Earned Leave
* View leave history
* Track leave status
* Approve or reject leave requests

### Asset Management

* Request company assets
* View asset requests
* Approve or reject requests
* Assign assets to employees

### Admin Panel

* Manage employees
* Manage leave requests
* Manage asset requests
* Search and filter employee records

## Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **Git**
* **GitHub**

## Django Concepts Used

This project helped me work with several core Django concepts:

* Django Models
* Django Views
* Django URL Routing
* Django Templates
* Django Forms
* Django ORM
* Authentication
* `login_required`
* Django Admin
* Database migrations
* Static and media files
* CRUD operations

## Project Structure

```text
project1/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── employees/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── leaves/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── assets/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── dashboard/
│   └── ...
│
├── templates/
│   ├── accounts/
│   ├── employees/
│   ├── leaves/
│   ├── assets/
│   └── dashboard/
│
├── media/
├── manage.py
└── db.sqlite3
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Harshith972/Django-employee-leave-asset-management.git
```

### 2. Navigate to the project

```bash
cd Django-employee-leave-asset-management
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django pillow
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Database

The project uses **SQLite** for local development.

The database is created using Django migrations and the Django ORM.

## What I Learned

Through this project, I gained practical experience in building a database-driven web application using Django.

Key areas I worked with include:

* Designing Django models
* Connecting models to a relational database
* Building CRUD functionality
* Implementing authentication
* Processing forms
* Working with Django ORM queries
* Handling file uploads
* Creating protected views
* Managing application data through Django Admin
* Organizing a Django project into multiple applications
* Using Git and GitHub for version control

## Future Improvements

* Build REST APIs using Django REST Framework
* Add role-based access control
* Add email notifications for leave approvals
* Improve frontend design and responsiveness
* Add automated tests
* Deploy the application to a cloud platform

## Author

**Harshith Reddy**

B.Tech Computer Science and Engineering
Vellore Institute of Technology

GitHub: https://github.com/Harshith972
