# Generated by Django 4.1.5 on 2023-03-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyparlour', '0003_alter_user_details_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='password',
            field=models.CharField(default='confidential', editable=False, max_length=20),
        ),
    ]
