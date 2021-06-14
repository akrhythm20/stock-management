from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stockmg.urls')),
    path('accounts/', include('registration.backends.default.urls')),
]
