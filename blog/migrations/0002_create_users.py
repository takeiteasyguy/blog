# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password


# noinspection PyPep8Naming
def create_common_admin_group(apps, schema_editor):
    """
    Migrate data from remote DB for initial data population
    """

    # get models
    User = apps.get_registered_model("auth", "User")

    # create simple user
    simple_user = User(username='simple_user',
                       email='ringostar@beatles.com',
                       is_active=True)
    simple_user.password = make_password('1234')
    simple_user.save()

    # create admin
    admin = User(username='admin',
                 email='jlennon@beatles.com',
                 is_staff=True,
                 is_active=True,
                 is_superuser=True)
    admin.password = make_password('1234')
    admin.save()



# noinspection PyUnusedLocal
def fake_reverse_func(apps, schema_editor):
    # NOTE: nothing to do, data migration wrapped as one transaction, data will not be partially committed if exception
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_common_admin_group, fake_reverse_func),
    ]
