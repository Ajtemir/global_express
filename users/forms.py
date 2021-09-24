from django import forms


class SignForm(forms.Form):

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'sign__input',
                                 'placeholder': 'Email или ваша почта'}))

    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                    'class': 'sign__input',
                                    'placeholder': 'Пароль'}))






