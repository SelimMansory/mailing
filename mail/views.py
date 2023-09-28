from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mail.forms import ClientForm, SettingMailForm, MailingForm
from mail.models import Client, SettingMail, Mailing, Log
from django.contrib.auth.mixins import LoginRequiredMixin

from mail.service import random_blog, get_cached_count_mailing, get_cached_count_active, get_cached_count_client


class ListMixin:
    """
    Миксин для ограничения видимости объектов
    """
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return super().get_queryset().all()
        else:
            return super().get_queryset().filter(owner=self.request.user)


class CreateMixin:

    """
    Миксин для указания владельца
    """
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientCreateView(LoginRequiredMixin, CreateMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:client')


class ClientListView(ListMixin, ListView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:client')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:client')


class SettingMailListView(LoginRequiredMixin, ListMixin, ListView):
    model = SettingMail


class SettingMailCreateView(LoginRequiredMixin, CreateMixin, CreateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')

    def get_form_kwargs(self):
        """
        Переопределяем метод для передачи user в форму SettingMailForm
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class SettingUpdateView(LoginRequiredMixin, UpdateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')


class SettingMailDeleteView(LoginRequiredMixin, DeleteView):
    model = SettingMail
    success_url = reverse_lazy('mail:list_setting')


class MailingListView(LoginRequiredMixin, ListMixin, ListView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:list_mail')

    def get_form_kwargs(self):
        """
        Переопределяем метод для передачи user в форму MailingForm
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:list_mail')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail:list_mail')


class LogListView(LoginRequiredMixin, ListView):
    model = Log


def title(request):
    context = {'blog_list': random_blog(),
               'count_mailing': len(get_cached_count_mailing()),
               'count_active': len(get_cached_count_active()),
               'count_client': len(get_cached_count_client())}
    return render(request, 'mail/home.html', context=context)