# Generated by Django 5.0.4 on 2024-05-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmembership',
            name='last_sub_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='gymmembership',
            name='next_sub_date',
            field=models.DateField(null=True),
        ),
    ]