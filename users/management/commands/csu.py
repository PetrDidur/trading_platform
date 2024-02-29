from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help('Creates superuser if it doesn\'t exist')

    def handle(self, *args, **options):
        user = User.objects.create(
            email="petr@mail.ru",
            is_superuser=True,
            is_active=True,
            is_staff=False
        )

        user.set_password("9184")
        user.save()