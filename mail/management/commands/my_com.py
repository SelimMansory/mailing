from mail.service import shipment_check
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        shipment_check()