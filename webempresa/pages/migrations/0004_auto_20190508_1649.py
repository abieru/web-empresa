# Generated by Django 2.0.2 on 2019-05-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190508_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-title'], 'verbose_name': 'Pagina', 'verbose_name_plural': 'Paginas'},
        ),
    ]
