# Generated by Django 2.0.2 on 2019-05-08 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190508_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['title'], 'verbose_name': 'Pagina', 'verbose_name_plural': 'Paginas'},
        ),
    ]
