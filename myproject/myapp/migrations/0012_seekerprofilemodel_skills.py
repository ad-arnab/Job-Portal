# Generated by Django 5.0.3 on 2024-10-31 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_seekerprofilemodel_skills_customuser_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekerprofilemodel',
            name='skills',
            field=models.CharField(choices=[('programming', 'Programming'), ('networking', 'Networking'), ('hardware', 'Hardware'), ('software', 'Software'), ('data science', 'Data Science'), ('cyber security', 'Cyber Security'), ('digital marketing', 'Digital Marketing'), ('cloud computing', 'Cloud Computing')], max_length=100, null=True),
        ),
    ]