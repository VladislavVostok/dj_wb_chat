from django.contrib import admin
from django.urls import path, include
from chat import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('chats/',include('chat.urls')),
    path('', views.index)
]
