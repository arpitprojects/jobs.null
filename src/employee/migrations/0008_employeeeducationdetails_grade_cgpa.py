# Generated by Django 2.0.5 on 2018-05-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20180517_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeeducationdetails',
            name='grade_cgpa',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
