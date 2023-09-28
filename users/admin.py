from django.contrib import admin
from users.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        self.exclude = ('mail_key', 'password', )
        return True


admin.site.register(User, UserAdmin)