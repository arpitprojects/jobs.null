# Generated by Django 2.0.5 on 2018-05-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyprofile',
            old_name='company_logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='companyprofile',
            old_name='company_name',
            new_name='name',
        ),
    ]