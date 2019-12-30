# mysite/urls.py
from django.conf.urls import include
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('polls/', include('polls.urls')),
]
