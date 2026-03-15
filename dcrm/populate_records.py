"""
populate_records.py

This script generates fake customer records in the database for testing or development purposes.
It uses the Faker library to create realistic German data, including:

- First name
- Last name
- Email
- Phone number
- Address
- City
- State (mapped to your model's state codes)
- Zipcode

If your Record model has a 'user' field, it will associate all generated records with the first user found.
Before running this script, ensure your Django environment is properly set up and your database is migrated.

Usage:
    python dcrm/populate_records.py
"""

import os
import django
from faker import Faker
import random

# 1️⃣ Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcrm.settings")

# 2️⃣ Initialize Django
django.setup()

# 3️⃣ Import your models AFTER setup
from website.models import Record
from django.contrib.auth.models import User

# Initialize Faker
fake = Faker('de_DE')

# Optional: get a user if your Record model requires it
user = User.objects.first()  # or None if your Record model's user field is optional

# Map full German state names to codes
STATE_MAP = {
    "Bayern": "BY",
    "Nordrhein-Westfalen": "NW",
    "Berlin": "BE",
    "Hamburg": "HH",
    "Hessen": "HE",
    "Sachsen": "SN",
    "Baden-Württemberg": "BW",
    "Niedersachsen": "NI",
    # add other states if needed
}

# 4️⃣ Create records
for _ in range(100):
    state_full = fake.state()
    state_code = STATE_MAP.get(state_full, "BE")  # default to BE if not found

    data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.unique.email(),
        'phone': fake.phone_number()[:15],
        'address': fake.street_address(),
        'city': fake.city(),
        'state': state_code,
        'zipcode': fake.postcode(),
    }

    if hasattr(Record, 'user') and user is not None:
        data['user'] = user

    Record.objects.create(**data)

print("✅ 100 records created successfully!")
