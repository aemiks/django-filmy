# Generated by Django 3.1.6 on 2021-03-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0004_auto_20210203_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (3, 'Sci-fi'), (2, 'Komedy'), (0, 'Other'), (4, 'Drama')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='extra',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.extrainfo'),
        ),
    ]
