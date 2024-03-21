import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from faker import Faker
fake = Faker()

from django.contrib.auth.models import User


# Creating User
def add_user(): user = User.objects.create_user(
    username=fake.user_name(),
    email=fake.email(),
    password=fake.password(),
    first_name=fake.first_name(),
    last_name=fake.last_name()
).save(); return user


# Generating data
def populate(n):
    for entry in range(n):
        add_user()


# Executing populate(): python generate_fake_data.py
if __name__ == '__main__':
    print("** Generating fake data...")
    populate(2)  # change value based on needs
    print('** Generated successfully **')
