# Generated by Django 3.1.6 on 2021-06-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmg', '0002_stockhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='issue_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='receive_quantity',
            field=models.IntegerField(default=0),
        ),
    ]