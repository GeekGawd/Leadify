# Generated by Django 4.2.3 on 2023-07-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackrx', '0002_alter_leads_category_alter_leads_connectiondegree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='timestamp',
            field=models.CharField(default='', max_length=300),
        ),
    ]
