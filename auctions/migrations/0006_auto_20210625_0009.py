# Generated by Django 3.2.4 on 2021-06-25 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_watchlist_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]