# Generated by Django 3.1.6 on 2021-06-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmg', '0005_auto_20210613_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issue_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receive_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
