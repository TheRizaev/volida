from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Авторизация пользователей
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Кастомная админ-панель для управления пользователями (только для администраторов)
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/users/', views.user_list, name='user_list'),
    path('admin-panel/users/create/', views.user_create, name='user_create'),
    path('admin-panel/users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('admin-panel/users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    
    # Главная страница после авторизации (можно заменить на другой URL)
    path('dashboard/', views.dashboard, name='dashboard'),
]