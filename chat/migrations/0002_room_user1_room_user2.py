# Generated by Django 5.1.1 on 2025-03-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='user1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='user2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
