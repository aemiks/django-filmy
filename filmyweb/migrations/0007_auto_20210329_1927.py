# Generated by Django 3.1.6 on 2021-03-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0006_auto_20210329_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (3, 'Sci-fi'), (4, 'Drama'), (2, 'Komedy'), (0, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(5, 'awesome'), (4, 'good'), (2, 'not bad'), (3, 'not bad not good'), (1, 'disaster')], default=3),
        ),
    ]
