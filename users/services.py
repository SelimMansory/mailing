import random
import string
from users.models import User
from django.contrib.auth.models import Group, Permission

def generate_random_key():
    characters = string.ascii_letters + string.digits
    # проверка на уникальность
    if len(User.objects.filter(mail_key=characters))>0:
        return generate_random_key()
    return ''.join(random.sample(characters, 30))