# Generated by Django 2.0.5 on 2018-05-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_auto_20180518_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicemployeeprofile',
            name='picture',
            field=models.ImageField(upload_to='media'),
        ),
    ]