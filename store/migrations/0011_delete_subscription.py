# Generated by Django 5.1.3 on 2024-12-26 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_subscription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]