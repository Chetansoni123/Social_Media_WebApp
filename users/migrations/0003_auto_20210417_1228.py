# Generated by Django 3.1.7 on 2021-04-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
