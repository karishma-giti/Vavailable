from allauth.account.forms import SignupForm
from django import forms
from .models import User
from .models import *

class SimpleSignupForm(SignupForm):
    phone = forms.CharField(max_length=10, label='Phone')

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        # import pdb;pdb.set_trace()
        user.phone = self.cleaned_data['phone']
        user.save()
        return user

        