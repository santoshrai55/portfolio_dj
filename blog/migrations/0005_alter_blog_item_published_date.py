# Generated by Django 4.0.6 on 2022-09-12 18:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_item_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_item',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 18, 27, 49, 979151, tzinfo=utc)),
        ),
    ]
