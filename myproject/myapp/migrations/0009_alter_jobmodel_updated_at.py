# Generated by Django 5.0.3 on 2024-10-31 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_jobmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
