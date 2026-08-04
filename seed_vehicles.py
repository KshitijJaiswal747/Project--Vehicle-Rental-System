#!/usr/bin/env python
"""Seed the default vehicle fleet."""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikerental.settings")
django.setup()

from rentals.models import Vehicle

Vehicle.seed_defaults()
print("Vehicle fleet seeded successfully.")
