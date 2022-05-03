# Generated by Django 3.2.13 on 2022-05-02 20:49
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzedurl',
            name='last_ad_served_date',
            field=models.DateField(blank=True, default=None, help_text='Last date an ad was served for this URL', null=True),
        ),
        migrations.AlterField(
            model_name='historicalanalyzedurl',
            name='last_ad_served_date',
            field=models.DateField(blank=True, default=None, help_text='Last date an ad was served for this URL', null=True),
        ),
    ]
