from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SignForm(forms.Form):

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'sign__input',
                                 'placeholder': 'Email или ваша почта',
                                 'id': 'sign_email'}))

    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                    'class': 'sign__input',
                                    'placeholder': 'Пароль'}))

    def clean_email(self):
        data = self.cleaned_data
        email = data['email']
        if email:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Email не найден попробуйте снова')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        if password and email:
            qs = User.objects.filter(email=email)[0]
            if not check_password(password, qs.password):
                raise forms.ValidationError('Неверный пароль')
        return password

    def get_user(self):
        from django.contrib.auth import authenticate
        return authenticate(
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignForm, self).__init__(*args, **kwargs)


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Email или ваша почта',
        'id': 'reg-email',
        'name': 'reg-email',
        'type': 'text'
    }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Пароль',
        'id': 'reg-password',
        'name': 'reg-password',
        'type': 'password'
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Повторите пароль',
        'id': 'reg-repeat-password',
        'name': 'reg-password',
        'type': 'password'
    }))

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'name',
        'name': 'name',
        'class': 'sign__input required',
        'placeholder': 'Например Айбек'
    }))

    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'surname',
        'name': 'surname',
        'class': 'sign__input required',
        'placeholder': 'Ваша Фамилия'
    }))

    patronymic = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'patronymic',
        'name': 'patronymic',
        'class': 'sign__input',
        'placeholder': 'Ваше Отчество'
    }))

    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'phone',
        'name': 'phone',
        'class': 'sign__input required',
        'placeholder': 'Ваш номер телефона:996555777222'
    }))

    telegram = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'telegram',
        'name': 'telegram',
        'class': 'sign__input',
        'placeholder': '@Nickname'
    }))

    city = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'city',
        'name': 'city',
        'class': 'sign__input required',
        'placeholder': 'Ваш город'
    }))

    address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'address',
        'name': 'address',
        'class': 'sign__input required',
        'placeholder': 'Адрес фактического проживания'
    }))

    apartment = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'apartment',
        'name': 'apartment',
        'class': 'sign__input required',
        'placeholder': 'Например Третий'
    }))

    postcode = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'id': 'postcode',
        'name': 'postcode',
        'class': 'sign__input required',
        'placeholder': 'Например Третий'
    }))

    scan_out = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'scan-out',
        'accept': 'image/*'
    }))

    scan_in = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'scan-in',
        'accept': 'image/*'
    }))

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return data['password2']

    def clean_email(self):
        data = self.cleaned_data
        email = data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Такая почта уже регистрирована'))
        return email

    def clean_scan_in(self):
        scan_in = self.cleaned_data.get('scan_in', False)
        if scan_in:
            if scan_in._size > 4*1024*1024:
                raise forms.ValidationError(_('File too big'))
            return scan_in

    def clean_scan_out(self):
        scan_out = self.cleaned_data.get('scan_out', False)
        if scan_out:
            if scan_out._size > 4*1024*1024:
                raise forms.ValidationError(_('File too big'))
            return scan_out

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        if validate_password(password):
            raise forms.ValidationError(_('Введите более защищённый пароль'))
        return super().clean()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'is_superuser',
                   'last_login', 'date_joined']


class ResetForm(forms.Form):

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Ваш новый пароль'
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Повторите новый пароль'
    }))

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        if validate_password(password):
            raise forms.ValidationError(_('Введите более защищённый пароль'))
        return super().clean()




