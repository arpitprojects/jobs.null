# Generated by Django 2.0.5 on 2018-05-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApplications', '0003_auto_20180525_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='status',
            field=models.CharField(choices=[('initated', 'Initiated'), ('no_response', 'no_response'), ('process', 'Process'), ('reject', 'Rejected'), ('hired', 'Hired')], default='initated', max_length=22),
        ),
    ]
