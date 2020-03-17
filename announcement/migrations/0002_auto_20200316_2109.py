# Generated by Django 2.0.12 on 2020-03-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='ForRent_status',
            field=models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=30, null=True, verbose_name='Select rental frequency'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='OtherPeriods_status',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Property is also available for other rental periods (price is on request via chat or call)', max_length=30, null=True, verbose_name='Is available ? '),
        ),
    ]
