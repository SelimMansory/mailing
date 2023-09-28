import os

from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from mail.service import _send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, LoginForm, UserProfiledFrom
from users.services import generate_random_key
from dotenv import load_dotenv
from users.models import User

load_dotenv()


# Create your views here.


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            key = generate_random_key()
            new_user.mail_key = key
            new_user.is_active = False
            new_user.save()
            _send_mail('Верификация',
                       f'Пройдите по ссылки для верификации:\n http://{os.getenv("DOMAIN_NAME")}\
/users/verification/?key={key}', new_user.email)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfiledFrom
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification(request):
    key = request.GET.get('key')
    user = User.objects.filter(mail_key=key)[0]
    if user:
        user.is_active = True
        user.save()
    return redirect('users:login')


def forgotten_password(request):
    pass


class UserLoginView(LoginView):
    form_class = LoginForm