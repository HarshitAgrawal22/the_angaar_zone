# Generated by Django 4.2.7 on 2024-03-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='isTeacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='isStudent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='isTeacher',
            field=models.BooleanField(default=True),
        ),
    ]