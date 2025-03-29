from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', required=True)
    email = forms.EmailField(label='Электронная почта')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже зарегистрирован.')
        return email