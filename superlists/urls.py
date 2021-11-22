from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from lists.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home_page, name='home'),
]
