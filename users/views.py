from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserRegistrationForm
from users.models import User
from django.conf import settings


class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Сохранение имени пользователя
        user = form.save(commit=False)
        user.first_name = form.cleaned_data.get('first_name')
        user.save()

        send_mail(
            subject='Рады вас видеть!',
            message='Спасибо за регистрацию на сайте "SkyStore"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get('email')],
            fail_silently=False,
        )

        return response
