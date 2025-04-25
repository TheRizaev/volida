from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def clean_phone_number(value):
    """
    Очищает и проверяет номер телефона.
    """
    # Удаляем все пробелы, скобки, дефисы и другие символы форматирования
    cleaned_number = re.sub(r'[\s\(\)\-\+]', '', value)
    
    # Проверяем, что номер состоит только из цифр
    if not cleaned_number.isdigit():
        raise ValidationError('Номер телефона должен содержать только цифры')
    
    # Проверяем минимальную длину номера (минимум 5 цифр)
    if len(cleaned_number) < 5:
        raise ValidationError('Длина номера телефона должна быть не менее 5 цифр')
    
    return value  # Возвращаем номер телефона как есть, без форматирования

class CustomAuthenticationForm(AuthenticationForm):
    """Форма авторизации с кастомными стилями"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Телефон',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
        })
    )
    
    def clean_username(self):
        """
        Проверяет номер телефона перед авторизацией.
        """
        username = self.cleaned_data.get('username')
        try:
            # Только проверяем валидность, но не меняем формат
            clean_phone_number(username)
            return username
        except ValidationError:
            # Если не является телефоном, оставляем как есть (для совместимости)
            return username

class CustomUserCreationForm(UserCreationForm):
    """Форма создания пользователя для админ-панели"""
    first_name = forms.CharField(required=False, label='Имя')
    last_name = forms.CharField(required=False, label='Фамилия')
    email = forms.EmailField(required=False, label='Email')
    is_staff = forms.BooleanField(required=False, label='Администратор')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы к полям формы
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Изменяем метку для поля username
        self.fields['username'].label = 'Телефон'
        self.fields['username'].help_text = 'Введите номер телефона пользователя (будет использоваться для входа)'
    
    def clean_username(self):
        """Валидация номера телефона"""
        username = self.cleaned_data.get('username')
        try:
            # Проверяем валидность, но не меняем формат
            clean_phone_number(username)
            return username
        except ValidationError as e:
            raise forms.ValidationError(str(e))
        return username

class CustomUserChangeForm(forms.ModelForm):
    """Форма редактирования пользователя для админ-панели"""
    email = forms.EmailField(required=False, label='Email')
    first_name = forms.CharField(required=False, label='Имя')
    last_name = forms.CharField(required=False, label='Фамилия')
    is_staff = forms.BooleanField(required=False, label='Администратор')
    is_active = forms.BooleanField(required=False, label='Активен')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы к полям формы
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Изменяем метку для поля username
        self.fields['username'].label = 'Телефон'
        self.fields['username'].help_text = 'Введите номер телефона пользователя (будет использоваться для входа)'
    
    def clean_username(self):
        """Валидация номера телефона"""
        username = self.cleaned_data.get('username')
        try:
            # Проверяем валидность, но не меняем формат
            clean_phone_number(username)
            return username
        except ValidationError as e:
            raise forms.ValidationError(str(e))
        return username

class SetPasswordForm(forms.Form):
    """Форма для изменения пароля пользователя"""
    password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Пароли не совпадают')
        
        return cleaned_data