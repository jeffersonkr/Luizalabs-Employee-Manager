# Generated by Django 2.2.1 on 2019-05-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(choices=[('A', 'Architeture'), ('E', 'E-commerce'), ('M', 'Mobile')], max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'Employee',
                'managed': True,
            },
        ),
    ]
