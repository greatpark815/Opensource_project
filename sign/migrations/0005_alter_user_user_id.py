# Generated by Django 4.2 on 2023-05-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0004_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
