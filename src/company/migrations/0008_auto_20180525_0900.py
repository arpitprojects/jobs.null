# Generated by Django 2.0.5 on 2018-05-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20180525_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='name',
            field=models.CharField(max_length=254, primary_key=True),
        ),
    ]