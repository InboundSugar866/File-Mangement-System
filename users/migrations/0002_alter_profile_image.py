# Generated by Django 5.1.4 on 2024-12-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.png', upload_to='profile_pics'),
        ),
    ]
