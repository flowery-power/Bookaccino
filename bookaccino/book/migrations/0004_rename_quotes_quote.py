# Generated by Django 4.0.2 on 2022-03-15 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_profilebook'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quotes',
            new_name='Quote',
        ),
    ]
