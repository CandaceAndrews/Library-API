# Generated by Django 4.1.7 on 2023-03-22 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_author_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]
