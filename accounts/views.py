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
    """
    Отображает главную страницу дашборда с финансовой информацией
    """
    # В будущем здесь будет получение реальных данных из базы
    context = {
        'active_menu': 'dashboard',
        # Данные для дашборда
        'balance': 5366814,
        'account_percentage': 81,
        'cash_percentage': 20,
        'debit_amount': 5366814,
        'credit_amount': 5366814,
        'stock_value': 52000000,
        'raw_value': 13000000,
        'raw_percentage': 80,
        'goods_value': 27000000,
        'goods_percentage': 10,
        'products_value': 58000000,
        'products_percentage': 10
    }
    return render(request, 'accounts/dashboard.html', context)

# Страница поставщиков
@login_required
def suppliers(request):
    context = {
        'active_menu': 'suppliers',
    }
    return render(request, 'accounts/suppliers.html', context)

# Страница просмотра деталей поставщика
@login_required
def supplier_details(request, pk):
    # В реальном проекте здесь нужно получить объект поставщика из базы данных
    # supplier = get_object_or_404(Supplier, pk=pk)
    
    context = {
        'active_menu': 'suppliers',
        'supplier_id': pk,
        # В реальном проекте здесь будут данные поставщика
        # 'supplier': supplier,
        # 'transactions': supplier.transactions.all(),
        # 'returns': supplier.returns.all(),
    }
    return render(request, 'accounts/supplier_details.html', context)

# Страница редактирования поставщика
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

@login_required
def clients(request):
    context = {
        'active_menu': 'clients',
    }
    return render(request, 'accounts/clients.html', context)

# Страница просмотра деталей клиента
@login_required
def client_details(request, pk):
    # В реальном проекте здесь нужно получить объект клиента из базы данных
    # client = get_object_or_404(Client, pk=pk)
    
    context = {
        'active_menu': 'clients',
        'client_id': pk,
        # В реальном проекте здесь будут данные клиента
        # 'client': client,
        # 'transactions': client.transactions.all(),
        # 'payments': client.payments.all(),
    }
    return render(request, 'accounts/client_details.html', context)

# Страница редактирования клиента
@login_required
def client_edit(request, pk):
    context = {
        'active_menu': 'clients',
        'client_id': pk,
    }
    return render(request, 'accounts/client_edit.html', context)

# Страница возврата продукции от клиента
@login_required
def client_product_return(request, pk):
    context = {
        'active_menu': 'clients',
        'client_id': pk,
    }
    return render(request, 'accounts/client_product_return.html', context)

# Страница сбыта продукции клиенту
@login_required
def client_product_sale(request, pk):
    context = {
        'active_menu': 'clients',
        'client_id': pk,
    }
    return render(request, 'accounts/client_product_sale.html', context)

# Страница создания поступления от клиента
@login_required
def client_payment(request, pk):
    context = {
        'active_menu': 'clients',
        'client_id': pk,
    }
    return render(request, 'accounts/client_payment.html', context)

@login_required
def production(request):
    context = {
        'active_menu': 'production',
    }
    return render(request, 'accounts/production.html', context)

# Страница деталей производства
@login_required
def production_details(request, pk):
    context = {
        'active_menu': 'production',
        'production_id': pk,
    }
    return render(request, 'accounts/production_details.html', context)

# Страница создания производства
@login_required
def production_create(request):
    if request.method == 'POST':
        # В будущем здесь будет обработка формы
        return redirect('production')
    
    context = {
        'active_menu': 'production',
    }
    return render(request, 'accounts/production_create.html', context)

# Страница прихода молока
@login_required
def milk_income(request):
    context = {
        'active_menu': 'milk_income',
    }
    return render(request, 'accounts/milk_income.html', context)

# Страница деталей прихода молока
@login_required
def milk_income_details(request, pk):
    context = {
        'active_menu': 'milk_income',
        'milk_income_id': pk,
    }
    return render(request, 'accounts/milk_income_details.html', context)

# Страница создания прихода молока
@login_required
def milk_income_create(request):
    if request.method == 'POST':
        # В будущем здесь будет обработка формы
        return redirect('milk_income')
    
    context = {
        'active_menu': 'milk_income',
    }
    return render(request, 'accounts/milk_income_create.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Страница склада товара
@login_required
def inventory_goods(request):
    context = {
        'active_menu': 'inventory_goods',
    }
    return render(request, 'accounts/inventory_goods.html', context)

# Страница склада сырья
@login_required
def inventory_raw(request):
    context = {
        'active_menu': 'inventory_raw',
    }
    return render(request, 'accounts/inventory_raw.html', context)

# Страница склада продукции
@login_required
def inventory_products(request):
    context = {
        'active_menu': 'inventory_products',
    }
    return render(request, 'accounts/inventory_products.html', context)

# Страница склада молока
@login_required
def inventory_milk(request):
    context = {
        'active_menu': 'inventory_milk',
    }
    return render(request, 'accounts/inventory_milk.html', context)

# Общая функция для списания товаров/сырья/продукции/молока
@login_required
def inventory_writeoff(request, inventory_type):
    if request.method == 'POST':
        # В будущем здесь будет обработка формы списания
        if inventory_type == 'goods':
            return redirect('inventory_goods')
        elif inventory_type == 'raw':
            return redirect('inventory_raw')
        elif inventory_type == 'products':
            return redirect('inventory_products')
        elif inventory_type == 'milk':
            return redirect('inventory_milk')
    
    # Если запрос не POST, перенаправляем на соответствующую страницу склада
    return redirect(f'inventory_{inventory_type}')

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