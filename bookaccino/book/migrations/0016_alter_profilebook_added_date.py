# Generated by Django 4.0.2 on 2022-03-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_alter_book_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilebook',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]