# Generated by Django 5.0.3 on 2024-10-22 03:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewersprofilemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='Display_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('recuriters', 'Recuriters'), ('seeker', 'Seeker')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='recuritersProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(max_length=100, null=True)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, null=True)),
                ('Profile_Pic', models.ImageField(upload_to='Media/recuriters_Profile_Pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recuritersProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seekerProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(max_length=100, null=True)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, null=True)),
                ('Profile_Pic', models.ImageField(upload_to='Media/seeker_Profile_Pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seekerProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BloggerProfileModel',
        ),
        migrations.DeleteModel(
            name='viewersProfileModel',
        ),
    ]
