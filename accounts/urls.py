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
    
    # Главная страница после авторизации
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Поставщики
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('suppliers/product-income/<int:pk>/', views.product_income, name='product_income'),
    path('suppliers/product-return/<int:pk>/', views.product_return, name='product_return'),
    path('suppliers/payments/<int:pk>/', views.payments, name='payments'),
    
    # Заглушки для остальных страниц (будут реализованы позже)
    path('production/', views.production, name='production'),
    path('clients/', views.clients, name='clients'),
    path('milk-income/', views.milk_income, name='milk_income'),
    
    # Складской учет
    path('inventory/goods/', views.inventory_goods, name='inventory_goods'),
    path('inventory/raw/', views.inventory_raw, name='inventory_raw'),
    path('inventory/products/', views.inventory_products, name='inventory_products'),
    path('inventory/milk/', views.inventory_milk, name='inventory_milk'),
    
    # Отчеты
    path('reports/sales/', views.reports_sales, name='reports_sales'),
    path('reports/production/', views.reports_production, name='reports_production'),
    
    # Пользователи
    path('users/', views.users, name='users'),
]