# Generated by Django 2.0.5 on 2018-05-16 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180516_0713'),
        ('employee', '0002_auto_20180516_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicEmployeeProfile',
            fields=[
                ('employeeprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('current_city', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='media')),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('preffered_place', models.CharField(max_length=100)),
                ('current_status', models.CharField(choices=[('Salaried', 'Salaried'), ('Jobless', 'Jobless'), ('Freelance', 'Freelance'), ('Contract', 'Contract')], default='JObless', max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='employeeprofile',
        ),
        migrations.DeleteModel(
            name='EmployeeProfile',
        ),
    ]
