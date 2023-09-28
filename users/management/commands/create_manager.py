from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='manager@manager.manager',
            first_name='manager',
            last_name='manager',
            is_staff=True,
        )
        user.set_password('manager')
        user.save()