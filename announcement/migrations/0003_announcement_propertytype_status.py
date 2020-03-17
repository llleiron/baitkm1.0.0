# Generated by Django 2.0.12 on 2020-03-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_auto_20200316_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='PropertyType_status',
            field=models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Retail', 'Retail'), ('Commercial', 'Commercial'), ('Land', 'Land')], max_length=30, null=True, verbose_name='Property type'),
        ),
    ]