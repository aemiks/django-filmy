# Generated by Django 3.1.6 on 2021-02-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_auto_20210203_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
    ]
