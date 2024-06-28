from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@example.com',
            first_name='Admin',
            last_name='Example',
            role="admin",
            is_active=True,
        )

        user.set_password('111')
        user.save()