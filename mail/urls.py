from mail.apps import MailConfig
from django.urls import path
from mail.views import ClientListView, ClientCreateView, SettingMailListView, SettingMailCreateView, ClientUpdateView, \
    SettingUpdateView, ClientDeleteView, MailingCreateView, MailingListView, MailingUpdateView, SettingMailDeleteView, \
    MailingDeleteView, LogListView, title

app_name = MailConfig.name

urlpatterns = [
    path('', title, name='home'),

    path('client', ClientListView.as_view(), name='client'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('list_setting/', SettingMailListView.as_view(), name='list_setting'),
    path('create_setting/', SettingMailCreateView.as_view(), name="create_setting"),
    path('list_setting/edit/<int:pk>', SettingUpdateView.as_view(), name='edit_setting'),
    path('list_setting/delete/<int:pk>', SettingMailDeleteView.as_view(), name='delete_setting'),

    path('list_mail/', MailingListView.as_view(), name='list_mail'),
    path('create_mail/', MailingCreateView.as_view(), name="create_mail"),
    path('list_mail/edit/<int:pk>', MailingUpdateView.as_view(), name='edit_mail'),
    path('list_mail/delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mail'),

    path('list_log/', LogListView.as_view(), name='list_log'),

]