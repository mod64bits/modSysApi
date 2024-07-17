from django.contrib import admin
from django.urls import path, include
from apps.users import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_authtoken.urls')),
    path('usuarios/', include(user_urls)),
]
