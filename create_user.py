import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volida.settings')
django.setup()

# Импорт модели User после настройки Django
from django.contrib.auth.models import User
from django.db import IntegrityError

def create_superuser():
    """Создает суперпользователя с заданными параметрами"""
    username = '12345'  # Простой номер телефона администратора
    password = 'admin123'      # Пароль администратора
    
    try:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email='',  # Email необязательный
                password=password,
                first_name='Администратор',
                last_name='Системы'
            )
            print(f'Администратор успешно создан: {username}')
        else:
            print(f'Администратор уже существует: {username}')
    except IntegrityError as e:
        print(f'Ошибка создания администратора: {e}')

if __name__ == '__main__':
    create_superuser()