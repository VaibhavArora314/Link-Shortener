# Generated by Django 4.1 on 2022-09-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tag',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
