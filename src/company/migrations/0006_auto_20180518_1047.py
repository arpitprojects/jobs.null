# Generated by Django 2.0.5 on 2018-05-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20180518_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]