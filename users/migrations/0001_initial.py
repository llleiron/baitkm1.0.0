# Generated by Django 2.0.12 on 2020-03-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('FullName', models.CharField(max_length=100, verbose_name='Full Name')),
                ('BirthDate', models.DateField(verbose_name='Birth date')),
                ('Phone', models.IntegerField(verbose_name='Phone number')),
                ('City', models.CharField(max_length=100, verbose_name='City')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
    ]
