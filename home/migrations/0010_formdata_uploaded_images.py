# Generated by Django 4.2.7 on 2024-01-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='uploaded_images',
            field=models.ManyToManyField(to='home.images'),
        ),
    ]
