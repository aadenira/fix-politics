# Generated by Django 3.0.8 on 2020-08-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0009_auto_20200804_2241'),
        ('users', '0002_auto_20200804_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='fixpol.Location'),
        ),
    ]
