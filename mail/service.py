
from mail.models import Mailing, Log, SettingMail, Client
from blog.models import Blog
from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.core.cache import cache
from users.models import User


def _send_mail(subject: str, text: str, mail: list) -> None:
    send_mail(
        subject,
        text,
        settings.EMAIL_HOST_USER,
        [mail]
    )


def shipment_check():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)

    mails = Mailing.objects.all()

    for mail in mails:
        if mail.setting.status == True:
            last_mail = Log.objects.filter(mail=mail, setting=mail.setting, status_try='finish').last()
            if last_mail:
                if (datetime_now - last_mail.date_last_try).days >= mail.setting.period:
                    _send_mail(mail.subject, mail.text, mail.setting.client.email)
                    Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')
            else:
                _send_mail(mail.subject, mail.text, mail.setting.client.email)
                Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')


def random_blog() -> list:
    """
    Возвращает список из 3 случайных статей
    """
    return Blog.objects.order_by('?')[:3]


class OwnerMixin:

    def form_valid(self, form):
        self.object = form.save()
        owner = self.request.user
        self.object.owner = owner
        self.object.save()
        return super().form_valid(form)


def get_cached_count_mailing():
    if settings.CACHE_ENABLE:
        key = 'count_mailing'
        count_mailing = cache.get(key)
        if count_mailing is None:
            count_mailing = Log.objects.filter(status_try='finish')
            cache.set(key, count_mailing)

        return count_mailing
    else:

        return Log.objects.filter(status_try='finish')


def get_cached_count_active():
    if settings.CACHE_ENABLE:
        key = 'count_active'
        count_active = cache.get(key)
        if count_active is None:
            count_active = SettingMail.objects.filter(status=True)
            cache.set(key, count_active)

        return count_active
    else:

        return SettingMail.objects.filter(status=True)


def get_cached_count_client():
    if settings.CACHE_ENABLE:
        key = 'count_client'
        count_client = cache.get(key)
        if count_client is None:
            count_client = User.objects.all()
            cache.set(key, count_client)

        return count_client
    else:

        return Client.objects.all()