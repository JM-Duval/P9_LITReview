# Generated by Django 3.2.6 on 2021-09-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.CharField(max_length=128),
        ),
    ]
