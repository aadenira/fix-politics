# Generated by Django 3.0.8 on 2020-08-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0015_law'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
