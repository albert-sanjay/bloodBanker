# Generated by Django 3.0.2 on 2020-06-02 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='blood_donation',
        ),
    ]
