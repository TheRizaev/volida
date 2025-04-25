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
    path('suppliers/view/<int:pk>/', views.supplier_details, name='supplier_details'),
    path('suppliers/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('suppliers/product-income/<int:pk>/', views.product_income, name='product_income'),
    path('suppliers/product-return/<int:pk>/', views.product_return, name='product_return'),
    path('suppliers/payments/<int:pk>/', views.payments, name='payments'),

    # Клиенты
    path('clients/', views.clients, name='clients'),
    path('clients/view/<int:pk>/', views.client_details, name='client_details'),
    path('clients/edit/<int:pk>/', views.client_edit, name='client_edit'),
    path('clients/return/<int:pk>/', views.client_product_return, name='client_product_return'),
    path('clients/sale/<int:pk>/', views.client_product_sale, name='client_product_sale'),
    path('clients/payment/<int:pk>/', views.client_payment, name='client_payment'),    
    
    # Производство продукции
    path('production/', views.production, name='production'),
    path('production/view/<int:pk>/', views.production_details, name='production_details'),
    path('production/create/', views.production_create, name='production_create'),
    
    # Приход молока
    path('milk-income/', views.milk_income, name='milk_income'),
    path('milk-income/view/<int:pk>/', views.milk_income_details, name='milk_income_details'),
    path('milk-income/create/', views.milk_income_create, name='milk_income_create'),
    
    # Складской учет
    path('inventory/goods/', views.inventory_goods, name='inventory_goods'),
    path('inventory/raw/', views.inventory_raw, name='inventory_raw'),
    path('inventory/products/', views.inventory_products, name='inventory_products'),
    path('inventory/milk/', views.inventory_milk, name='inventory_milk'),
    path('inventory/writeoff/<str:inventory_type>/', views.inventory_writeoff, name='inventory_writeoff'),
    
    # Отчеты
    path('reports/sales/', views.reports_sales, name='reports_sales'),
    path('reports/production/', views.reports_production, name='reports_production'),
    
    # Пользователи
    path('users/', views.users, name='users'),
]