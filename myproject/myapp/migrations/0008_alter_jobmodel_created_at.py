# Generated by Django 5.0.3 on 2024-10-31 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_customuser_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
