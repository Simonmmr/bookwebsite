# Generated by Django 5.1.3 on 2024-12-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]