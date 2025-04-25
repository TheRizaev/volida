from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Стандартная админ-панель Django
    path('', include('accounts.urls')),  # Включение URL из приложения accounts
    path('', RedirectView.as_view(url='login/')),  # Перенаправление с корня на страницу входа
]