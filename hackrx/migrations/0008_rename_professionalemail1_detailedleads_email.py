# Generated by Django 4.2.3 on 2023-07-21 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackrx', '0007_rename_email_detailedleads_professionalemail1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailedleads',
            old_name='professionalEmail1',
            new_name='email',
        ),
    ]