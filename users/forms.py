from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Account, Profile


class AccountRegisterForm(UserCreationForm):
    CHOICES = [('is_employee', 'Employee'), ('is_employer', 'Employer')]
    user_types = forms.CharField(label="User Types", widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'})
        }
