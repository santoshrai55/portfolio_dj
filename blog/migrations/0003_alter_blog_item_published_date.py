# Generated by Django 4.0.6 on 2022-09-12 18:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_itle_blog_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_item',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 18, 19, 24, 392656, tzinfo=utc)),
        ),
    ]
