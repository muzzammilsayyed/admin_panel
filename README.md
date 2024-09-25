# Admin Panel for Partner Management

## Overview

This is a Django-based web application for managing partner information. It allows admins to log in, view a list of partners, add new partners, edit partner details, and log out. 

## Features

- Secure login for admin users
- Dashboard with a summary view
- Partner listing with search functionality
- Add new partners
- Edit existing partner details
- Logout functionality

## Technologies Used

- Python 3.x
- Django 4.x
- SQLite (default database)
- HTML/CSS for frontend

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```
git clone (https://github.com/muzzammilsayyed/admin_panel/)
cd admin_panel
```

### 2. Create a Virtual Environment
Run the following commands:

```
python -m venv venv
```

###3. Activate the Virtual Environment
Activate the virtual environment:

For Windows:
```
venv\Scripts\activate
```

For macOS/Linux:
```
source venv/bin/activate
```

### 4. Install Dependencies
Install the required packages using requirements.txt:
```
pip install -r requirements.txt
```

### 5. Database Setup
Run the following commands to apply migrations and create the database:
```
python manage.py migrate
```

### 6. Create a Superuser
Create a superuser to log in to the admin panel:
```
python manage.py createsuperuser
```
Follow the prompts to set up your admin credentials.

### 7. Run the Development Server
Start the Django development server:
```
python manage.py runserver
```

### 8. Access the Application
Open your web browser and go to:
```
http://127.0.0.1:8000/login/
```

Log in using the superuser credentials you created.

## Usage
- After logging in, you'll be redirected to the dashboard.
- From the dashboard, you can navigate to the partner list, add new partners, and edit existing partner details.
- Use the search functionality to quickly find partners.

### Security Practices
- Ensure that your application is protected against common web vulnerabilities.
- Use strong passwords for admin accounts.



### Acknowledgements
- Django Documentation: https://docs.djangoproject.com/


