# Django CRM

A simple **Customer Relationship Management (CRM)** web application built with **Python** and **Django**.

This project allows users to **register, log in, and manage customer records** using a clean Bootstrap‑powered interface. Core functionality includes viewing, adding, updating, and deleting customer records.

## 🧠 Key Features

- User authentication (register, login, logout)  
- View all customer records in a table  
- Add new customer records  
- Update existing records  
- View individual record details  
- Delete customer records  
- Bootstrap UI for responsive design

This project follows a typical Full‑Stack Django pattern where models are defined in Django, views handle request logic, and templates render user pages.

## 🔧 Tech Stack

- **Python 3**
- **Django 6**
- **HTML + Bootstrap**
- **PostgreSQL** (or SQLite for development)
- Django built‑in authentication

Here’s a clean Markdown version ready to copy into your README.md with proper code blocks, lists, and headings:

## 📁 Project Structure

| File/Folder | Description |
|------------|-------------|
| `dcrm/`     | Django project configuration |
| `website/`  | Main app for CRM functionality |
| `models.py` | Record model defined here |
| `views.py`  | View logic (list, add, update, delete) |
| `urls.py`   | URL routes |
| `templates/`| HTML templates |
| `static/`   | CSS and JS assets |
| `manage.py` | Django CLI entrypoint |

## 🚀 Getting Started

### 1. Clone the repository
```commandline
git clone https://github.com/abushka110/Django_CRM.git
cd Django_CRM
```
### 2. Create and activate a virtual environment

On macOS / Linux:
```commandline
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```commandline
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```commandline
pip install -r requirements.txt
```
### 4. Apply database migrations
```commandline
python dcrm/manage.py migrate
```
### 5. (Optional) Create a superuser
```commandline
python dcrm/manage.py createsuperuser
```
This allows you to access the Django admin if needed.

### 6. Run the development server
```commandline
python dcrm/manage.py runserver
```
Open your browser at:

http://localhost:8000/

## 📌 Usage
	1.	Register a new user account
	2.	Log in with your credentials
	3.	View the list of customer records
	4.	Add, update, or delete records
	5.	Click on a record to see details