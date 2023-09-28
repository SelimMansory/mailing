from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.models import User
from mail.models import Mailing, SettingMail, Client


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        new_group, created = Group.objects.get_or_create(name='manager')
        ct_user = ContentType.objects.get_for_model(User)
        ct_mail = ContentType.objects.get_for_model(Mailing)
        ct_setting = ContentType.objects.get_for_model(SettingMail)
        ct_client = ContentType.objects.get_for_model(Client)

        view_user = Permission.objects.get(codename='view_user', name='Can view user', content_type=ct_user)
        change_user = Permission.objects.get(codename='change_user', name='Can change user', content_type=ct_user)
        view_mail = Permission.objects.get(codename='view_mailing', name='Can view сообщение', content_type=ct_mail)
        view_setting = Permission.objects.get(codename='view_settingmail', name='Can view настройка',
                                              content_type=ct_setting)
        view_client = Permission.objects.get(codename='view_client', name='Can view клиент', content_type=ct_client)
        change_setting = Permission.objects.get(codename='change_settingmail', name='Can change настройка',
                                                content_type=ct_setting)

        new_group.permissions.add(view_user, change_user, view_client, view_mail, view_setting, change_setting)