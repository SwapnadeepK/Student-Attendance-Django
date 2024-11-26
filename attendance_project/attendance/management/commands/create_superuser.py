from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create a superuser and add to the Teachers group'

    def handle(self, *args, **options):
        username = 'swapnadep'
        password = 'Sdk@2017'  # Replace with a secure password
        email = 'swapnadeep.kapuri1@gmail.com'

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username=username, email=email, password=password)
            teachers_group, created = Group.objects.get_or_create(name='Teachers')
            user.groups.add(teachers_group)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username} and added to Teachers group'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists'))
