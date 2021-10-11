from django.conf import settings
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView

from users.forms import SignForm, RegistrationForm, ResetForm


User = get_user_model()


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('users:sign')


class SignView(LoginView):
    template_name = 'users/sign.html'
    authentication_form = SignForm

    def get_success_url(self):
        return '/'


class ForgetView(FormView):
    template_name = 'users/reset.html'
    form_class = ResetForm
    success_url = reverse_lazy('users:sign')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        token = self.kwargs.get('token')

        user = get_object_or_404(User, pk=pk)

        password = form.cleaned_data.get('password')
        if default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
        return HttpResponseRedirect(self.get_success_url())


def logout_view(request):
    logout(request)
    return redirect('/')


class PersonalAreaView(LoginRequiredMixin, TemplateView):
    template_name = 'users/personal-area.html'
    login_url = '/sign'


"""AJAX-VIEWS"""


class ForgetPasswordView(View):
    def post(self, request):
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            pk = user.id
            url = f'{request.get_host()}{reverse("users:reset", args=[pk, token])}'
            send_mail("Изменение пароля", f'Чтобы изменить пароль, перейдите по ссылке => {url}',
                      settings.EMAIL_SENDER, [email], fail_silently=False)
            return JsonResponse({'data': True}, status=200)
        else:
            return JsonResponse({'data': False})


class ChangePasswordView(View):
    def post(self, request):
        result = None

        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if check_password(old_password, user.password):
            if old_password != new_password:
                try:
                    validate_password(new_password)
                    if new_password == confirm_password:
                        user.set_password(new_password)
                        user.save()
                        result = 'Пароль изменён'
                    else:
                        result = 'Пароли не совпадают'
                except:
                    result = 'Введите более защищённый пароль'
            else:
                result = 'Старый и новый пароль совпадает'
        else:
            result = 'Неверный старый пароль'

        return JsonResponse({'data': result})


class ChangeProfileView(View):
    def post(self, request):

        scan_in = request.FILES.get('scan-in')
        scan_out = request.FILES.get('scan-out')
        postcode = request.POST.get('postcode')
        city = request.POST.get('city')
        address = request.POST.get('address')
        patronymic = request.POST.get('patronymic')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        name = request.POST.get('name')

        user = request.user

        if user.first_name != name:
            user.first_name = name
        if user.last_name != name:
            user.last_name = surname
        if user.patronymic != patronymic:
            user.patronymic = patronymic
        if user.address != address:
            user.address = address
        if user.city != city:
            user.city = city
        if user.postcode != postcode:
            user.postcode = postcode
        if not User.objects.filter(email=email).exists():
            if user.email != email:
                user.email = email
        else:
            return JsonResponse({'data': False}, status=200)

        if scan_in:
            user.scan_in = scan_in
        if scan_out:
            user.scan_out = scan_out

        user.save()

        return JsonResponse({'data': True}, status=200)
