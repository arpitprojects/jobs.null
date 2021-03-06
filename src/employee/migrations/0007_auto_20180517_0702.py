# Generated by Django 2.0.5 on 2018-05-17 07:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180516_0713'),
        ('employee', '0006_basicemployeeprofile_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEducationDetails',
            fields=[
                ('employeeeducationdetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='basicemployeeprofile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 5, 17, 7, 2, 27, 112015, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicemployeeprofile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='basicemployeeprofile',
            name='preffered_place',
            field=models.CharField(choices=[('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Kolkata', 'Kolkata'), ('Hyderabad', 'Hyderabads'), ('Banglore', 'Banglore'), ('Delhi', 'Delhi'), ('Gurugram', 'Gurugram'), ('Jaipur', 'Jaipur')], max_length=100),
        ),
    ]
