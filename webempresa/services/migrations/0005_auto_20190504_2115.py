# Generated by Django 2.0.2 on 2019-05-05 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190504_2052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='Service',
        ),
    ]
