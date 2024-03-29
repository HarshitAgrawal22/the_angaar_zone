# Generated by Django 4.2.7 on 2024-03-09 12:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=10)),
                ('bio', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Prefer not to tell', 'Prefer not to tell')], max_length=30)),
                ('profile_pic', imagekit.models.fields.ProcessedImageField(upload_to='teacher_profile')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teachers', to='accounts.course')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('parent_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male'), ('Prefer not to say', 'Preer not to say')], max_length=30)),
                ('bio', models.TextField()),
                ('isStudent', models.BooleanField()),
                ('profile_pic', imagekit.models.fields.ProcessedImageField(upload_to='students_profile')),
                ('course', models.ManyToManyField(related_name='students', to='accounts.course')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
