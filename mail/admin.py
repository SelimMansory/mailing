from django.contrib import admin
from mail.models import Client, Mailing, SettingMail, Log
# Register your models here.


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment',)
    search_fields = ('email', 'full_name',)


@admin.register(SettingMail)
class SettingMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'mailing_time', 'period', 'status',)
    list_filter = ('status',)
    search_fields = ('client',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'setting', 'subject', 'text',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail', 'date_last_try', 'status_try', 'answer',)
    list_filter = ('answer',)