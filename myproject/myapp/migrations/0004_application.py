# Generated by Django 4.2.6 on 2024-10-27 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_jobmodel_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('cover_letter', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobmodel')),
            ],
        ),
    ]
