from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from users.forms import AccountRegisterForm, UserUpdateForm
from users.models import Profile


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = "User Account has been created!"

    def form_valid(self, form):
        user = form.save(commit=False)
        user_type = form.cleaned_data['user_types']
        if user_type == 'is_employee':
            user.is_employee = True

        elif user_type == 'is_employer':
            user.is_employer = True

        user.save()
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'


@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    success_message = "Profile Successfully Updated"
    template_name = 'users/update.html'
    form_class = UserUpdateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserUpdateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserUpdateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:update_profile', kwargs={'pk': self.object.pk})
