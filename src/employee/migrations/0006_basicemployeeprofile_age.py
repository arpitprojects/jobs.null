# Generated by Django 2.0.5 on 2018-05-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_remove_basicemployeeprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicemployeeprofile',
            name='age',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]
