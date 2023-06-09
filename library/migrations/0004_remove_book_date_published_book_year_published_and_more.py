# Generated by Django 4.1.7 on 2023-03-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_featured_alter_book_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_published',
        ),
        migrations.AddField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('education', 'Education'), ('graphic novel', 'Graphic Novel'), ('horror', 'Horror'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('mystery', 'Mystery'), ("children's literature", "Children's Literature"), ('biography', 'Biograpy'), ('adventure', 'Adventure'), ('cookbook', 'Cookbook'), ('historical', 'Historical'), ('fiction', 'Fiction'), ('nonfiction', 'Non-fiction')], max_length=50),
        ),
    ]
