from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create demo users: admin/admin123 (staff) and user/user123."

    def handle(self, *args, **options):
        User = get_user_model()
        users = [
            ("admin", "admin123", True),
            ("user", "user123", False),
        ]
        for username, password, is_staff in users:
            user, created = User.objects.get_or_create(username=username)
            user.is_staff = is_staff
            user.set_password(password)
            user.save()
            status = "created" if created else "updated"
            self.stdout.write(f"{username}: {status} (is_staff={is_staff})")
