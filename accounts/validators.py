import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    """
    Валидатор для номера телефона.
    Проверяет, что введенное значение является корректным номером телефона.
    """
    # Удаляем все пробелы, скобки, дефисы и другие символы форматирования
    cleaned_number = re.sub(r'[\s\(\)\-\+]', '', value)
    
    # Проверяем, что номер состоит только из цифр
    if not cleaned_number.isdigit():
        raise ValidationError('Номер телефона должен содержать только цифры')
    
    # Проверяем длину номера (минимум 10, максимум 15 цифр)
    if len(cleaned_number) < 10 or len(cleaned_number) > 15:
        raise ValidationError('Длина номера телефона должна быть от 10 до 15 цифр')
    
    # Форматируем номер для стандартного отображения (опционально)
    # Если номер начинается с 8 и имеет длину 11 цифр, преобразуем в +7
    if cleaned_number.startswith('8') and len(cleaned_number) == 11:
        formatted_number = '+7' + cleaned_number[1:]
    else:
        formatted_number = '+' + cleaned_number if not value.startswith('+') else value
    
    return formatted_number