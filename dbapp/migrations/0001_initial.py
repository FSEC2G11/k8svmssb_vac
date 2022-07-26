# Generated by Django 4.0.2 on 2022-02-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('gIDType', models.IntegerField(choices=[(1, 'Aadhaar'), (2, 'Passport'), (3, 'Birth Cert')])),
                ('gIDNum', models.IntegerField(max_length=20)),
                ('mobileNumber', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacID', models.IntegerField(choices=[(1, 'Covaxin'), (2, 'Covishield')])),
            ],
        ),
        migrations.CreateModel(
            name='VacDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vacID', models.IntegerField(choices=[(1, 'Covaxin'), (2, 'Covishield')])),
                ('numDoses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VacDoseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacDoseNum', models.IntegerField()),
                ('vacID', models.IntegerField(choices=[(1, 'Covaxin'), (2, 'Covishield')])),
                ('vacDate', models.DateTimeField(auto_now_add=True)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.student')),
            ],
        ),
    ]
