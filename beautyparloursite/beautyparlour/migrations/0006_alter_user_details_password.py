# Generated by Django 4.1.5 on 2023-03-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyparlour', '0005_alter_user_details_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
