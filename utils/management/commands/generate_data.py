# region				-----External Imports-----
import os
from django.core.management.base import BaseCommand
from django import apps as django_apps
# endregion


class Command(BaseCommand):
    help = "Generates records for each declared model"

    def add_arguments(self, parser):
        parser.add_argument("-n", "--number", nargs="?", type=int, default=1)

    def handle(self, *args, **options):
        number = options.get("number")

        for app in django_apps.apps.get_app_configs():
            if "site-packages" not in app.path:
                if app.models:
                    os.system(f"python manage.py seed {app.name} --number={number}")

        self.stdout.write(
                self.style.SUCCESS("Data is successfully generated")
            )
