# Generated by Django 4.2.4 on 2023-08-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_alter_settingmail_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingmail',
            name='period',
            field=models.PositiveIntegerField(default=1, max_length=20, verbose_name='периодичность'),
        ),
    ]