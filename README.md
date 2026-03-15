# Django CRM

A simple **Customer Relationship Management (CRM)** web application built with **Python** and **Django**.

This project allows users to **register, log in, and manage customer records** using a clean Bootstrap‑powered interface. Core functionality includes viewing, adding, updating, and deleting customer records.

## 🧠 Key Features

### Authentication

- User registration

- User login

- User logout

- Authentication-based access to CRM features

### Customer Record Management

- View all customer records

- Add new records

- Update existing records

- Delete records

- Detailed view for each record

### Data Organization

- Customer contact information

- Address and state tracking

- Record timestamps

- Structured database models

### User Experience

- Flash messages for user feedback

- Form validation

- Clean UI using Bootstrap

- Navigation for quick access to CRM functions

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

### 6. Regenerate translation files
Extract messages
```commandline
python dcrm/manage.py makemessages -l de
```
Since .mo files are ignored by Git, you need to compile translations from the .po files:
Compile all .po files to .mo
```commandline
python dcrm/manage.py compilemessages
```

> Make sure you have **gettext** installed on your system; Django needs it to compile `.po` → `.mo`.

### Install `gettext`:

* **macOS:**

```bash
brew install gettext
```

* **Ubuntu/Linux:**

```bash
sudo apt install gettext
```

* **Windows:**
  Install via **GnuWin32** or use **WSL**.

### 7. Run the development server
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