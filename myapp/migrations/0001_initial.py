# Generated by Django 2.0.3 on 2019-01-25 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('email', models.CharField(blank=True, max_length=10)),
                ('dob', models.DateField(blank=True, max_length=8, null=True)),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='myapp/photo')),
            ],
        ),
    ]
