# Generated by Django 4.2.4 on 2023-09-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email_alter_user_mail_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail_key',
            field=models.CharField(default='', max_length=30, verbose_name='key'),
        ),
    ]