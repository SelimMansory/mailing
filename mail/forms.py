from users.forms import StyleFormMixin
from django import forms
from mail.models import Client, SettingMail, Mailing
from django.contrib.admin import widgets


class ClientForm(StyleFormMixin, forms.ModelForm):
    """

    """

    class Meta:
        model = Client
        exclude = ('owner',)


class SettingMailForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
        if self.user:
            self.fields['client'].queryset = Client.objects.filter(owner=self.user)

    class Meta:
        model = SettingMail
        fields = ('client', 'mailing_time', 'period', 'status',)


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
        if self.user:
            self.fields['setting'].queryset = SettingMail.objects.filter(status=True, owner=self.user)

    class Meta:
        model = Mailing
        fields = ('setting', 'subject', 'text',)