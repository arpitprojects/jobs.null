# Generated by Django 2.0.5 on 2018-05-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20180518_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
