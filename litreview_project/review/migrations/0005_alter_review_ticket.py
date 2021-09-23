# Generated by Django 3.2.6 on 2021-09-23 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_alter_ticket_image'),
        ('review', '0004_alter_review_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket'),
        ),
    ]