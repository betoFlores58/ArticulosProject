# Generated by Django 3.1.7 on 2021-03-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.TextField(default=''),
        ),
    ]
