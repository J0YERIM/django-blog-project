from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('blogs/', include('blogs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
