# Generated by Django 4.2.3 on 2023-07-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackrx', '0009_alter_detailedleads_allskills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='lead_score',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
