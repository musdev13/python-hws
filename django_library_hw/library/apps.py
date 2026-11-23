from django.apps import AppConfig
from django.db.models.signals import post_migrate


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    def ready(self):
        post_migrate.connect(
            create_readers_group,
            sender=self,
            dispatch_uid='library.create_readers_group',
        )


def create_readers_group(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    from .models import Book

    content_type = ContentType.objects.get_for_model(Book)
    view_books = Permission.objects.get(
        content_type=content_type,
        codename='view_book',
    )
    group, _ = Group.objects.get_or_create(name='Читачі')
    group.permissions.set([view_books])
