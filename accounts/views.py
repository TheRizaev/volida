from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import (
    CustomAuthenticationForm, 
    CustomUserCreationForm, 
    CustomUserChangeForm,
    SetPasswordForm
)

# Проверка, является ли пользователь администратором
def is_admin(user):
    return user.is_authenticated and user.is_staff

# Кастомное представление для авторизации
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        # Если пользователь администратор, перенаправляем на админ-панель
        if self.request.user.is_staff:
            return reverse_lazy('admin_dashboard')
        # Иначе на обычную страницу Dashboard
        return reverse_lazy('dashboard')

# Базовая страница после авторизации для обычных пользователей
@login_required
def dashboard(request):
    context = {
        'active_menu': 'dashboard',
    }
    return render(request, 'accounts/dashboard.html', context)

# Страница поставщиков
@login_required
def suppliers(request):
    context = {
        'active_menu': 'suppliers',
    }
    return render(request, 'accounts/suppliers.html', context)

# Редактирование поставщика
@login_required
def supplier_edit(request, pk):
    context = {
        'active_menu': 'suppliers',
        'supplier_id': pk,
    }
    return render(request, 'accounts/supplier_edit.html', context)

# Страница прихода товара
@login_required
def product_income(request, pk):
    context = {
        'active_menu': 'suppliers',
        'supplier_id': pk,
    }
    return render(request, 'accounts/product_income.html', context)

# Страница возврата товара
@login_required
def product_return(request, pk):
    context = {
        'active_menu': 'suppliers',
        'supplier_id': pk,
    }
    return render(request, 'accounts/product_return.html', context)

# Страница выплат
@login_required
def payments(request, pk):
    context = {
        'active_menu': 'suppliers',
        'supplier_id': pk,
    }
    return render(request, 'accounts/payments.html', context)

# Заглушки для остальных страниц

@login_required
def production(request):
    context = {
        'active_menu': 'production',
    }
    return HttpResponse("Страница Производство продукции будет реализована позже")

@login_required
def clients(request):
    context = {
        'active_menu': 'clients',
    }
    return HttpResponse("Страница Клиенты будет реализована позже")

@login_required
def milk_income(request):
    context = {
        'active_menu': 'milk_income',
    }
    return HttpResponse("Страница Приход молока будет реализована позже")

# Складской учет
@login_required
def inventory_goods(request):
    context = {
        'active_menu': 'inventory_goods',
    }
    return HttpResponse("Страница Склад товара будет реализована позже")

@login_required
def inventory_raw(request):
    context = {
        'active_menu': 'inventory_raw',
    }
    return HttpResponse("Страница Склад сырья будет реализована позже")

@login_required
def inventory_products(request):
    context = {
        'active_menu': 'inventory_products',
    }
    return HttpResponse("Страница Склад продукции будет реализована позже")

@login_required
def inventory_milk(request):
    context = {
        'active_menu': 'inventory_milk',
    }
    return HttpResponse("Страница Склад молока будет реализована позже")

# Отчеты
@login_required
def reports_sales(request):
    context = {
        'active_menu': 'reports_sales',
    }
    return HttpResponse("Страница Отчет по продажам будет реализована позже")

@login_required
def reports_production(request):
    context = {
        'active_menu': 'reports_production',
    }
    return HttpResponse("Страница Отчет по производству будет реализована позже")

@login_required
def users(request):
    context = {
        'active_menu': 'users',
    }
    return HttpResponse("Страница Пользователи будет реализована позже")

# Админ-панель - Главная страница
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    # Собираем статистику
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    admin_users = User.objects.filter(is_staff=True).count()
    
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'admin_users': admin_users,
    }
    
    return render(request, 'accounts/admin/dashboard.html', context)

# Админ-панель - Список пользователей
@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'accounts/admin/user_list.html', {'users': users})

# Админ-панель - Создание пользователя
@login_required
@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Пользователь {user.username} успешно создан')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/admin/user_create.html', {'form': form})

# Админ-панель - Редактирование пользователя
@login_required
@user_passes_test(is_admin)
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    # Не даем изменить данные суперпользователя, если редактор не суперпользователь
    if user.is_superuser and not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав для редактирования этого пользователя')
        return redirect('user_list')
    
    if request.method == 'POST':
        # Если запрос на изменение пароля
        if 'action' in request.POST and request.POST['action'] == 'change_password':
            password_form = SetPasswordForm(request.POST)
            if password_form.is_valid():
                user.set_password(password_form.cleaned_data['password1'])
                user.save()
                messages.success(request, f'Пароль пользователя {user.username} успешно изменен')
                return redirect('user_list')
        # Если запрос на изменение данных пользователя
        else:
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, f'Данные пользователя {user.username} успешно обновлены')
                return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
        password_form = SetPasswordForm()
    
    context = {
        'user_form': form,
        'password_form': password_form,
        'user_obj': user
    }
    
    return render(request, 'accounts/admin/user_edit.html', context)

# Админ-панель - Удаление пользователя
@login_required
@user_passes_test(is_admin)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    # Не даем удалить суперпользователя
    if user.is_superuser:
        messages.error(request, 'Невозможно удалить суперпользователя')
        return redirect('user_list')
    
    # Не даем удалить самого себя
    if user == request.user:
        messages.error(request, 'Вы не можете удалить свою учетную запись')
        return redirect('user_list')
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'Пользователь {username} был успешно удален')
        return redirect('user_list')
    
    return render(request, 'accounts/admin/user_delete.html', {'user': user})