from django import forms

from parcels.models import Parcel


class AddForm(forms.ModelForm):
    recipient = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'Ваше ФИО'
    }))

    track = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'Ваш трек номер'
    }))

    name = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'Например Zara, HM'
    }))

    price = forms.DecimalField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': '0.00 $'
    }))

    store = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input country__input',
        'placeholder': 'Выберите страну',
        'readonly': 'readonly'
    }))

    type = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'www.primer.com',
        'maxlength': '324'
    }))

    comment = forms.CharField(required=False, widget=forms.Textarea({
        'class': 'sign__input modal__textarea',
        'placeholder': 'Можете оставить комментарий'
    }))

    site = forms.URLField(required=True, widget=forms.URLInput({
        'class': 'sign__input modal__textarea',
        'placeholder': 'сайт'
    }))

    class Meta:
        model = Parcel
        exclude = ['status', 'is_deleted', 'number',
                   'user', 'amount', 'weight']

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class EditForm(forms.ModelForm):
    id = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'hidden',
    }))


    name = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'Например Zara, HM'
    }))

    type = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input',
        'placeholder': 'www.primer.com',
        'maxlength': '324'
    }))

    store = forms.CharField(required=True, widget=forms.TextInput({
        'type': 'text',
        'class': 'sign__input country__input',
        'placeholder': 'Выберите страну',
        'readonly': 'readonly'
    }))

    site = forms.URLField(required=True, widget=forms.URLInput({
        'class': 'sign__input modal__textarea',
        'placeholder': 'сайт'
    }))

    comment = forms.CharField(required=False, widget=forms.Textarea({
        'class': 'sign__input modal__textarea',
        'placeholder': 'Можете оставить комментарий'
    }))

    class Meta:
        model = Parcel
        fields = ['name', 'type', 'store', 'site', 'comment', 'id']




