from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from django.urls import path
from blog.views import BlogDeleteView, BlogCreateView, BlogDetailView, BlogListView, BlogUpdateView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', cache_page(60)(BlogCreateView.as_view()), name='create_blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit')

]