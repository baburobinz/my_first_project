# Generated by Django 4.1.5 on 2023-04-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyparlour', '0014_gallery_offers_quotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='offer',
        ),
        migrations.AddField(
            model_name='offers',
            name='hair',
            field=models.CharField(default='h', max_length=10),
        ),
        migrations.AddField(
            model_name='offers',
            name='makeup',
            field=models.CharField(default='h', max_length=10),
        ),
        migrations.AddField(
            model_name='offers',
            name='massage',
            field=models.CharField(default='h', max_length=10),
        ),
    ]