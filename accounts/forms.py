from allauth.account.forms import SignupForm
from django import forms
from .models import User
from .models import *

class SimpleSignupForm(SignupForm):
    phone = forms.CharField(max_length=10, label='Phone')
    gender = forms.ChoiceField(choices=gender)
    city = forms.CharField(max_length=10, label='City')
    Area = forms.CharField(max_length=10, label='Area')
    state = forms.CharField(max_length=10, label='state')
    country = forms.CharField(max_length=10, label='country')
    pin_code = forms.CharField(max_length=10, label='pin_code')
    type_of_workplace = forms.ChoiceField(choices=workplace)

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        # import pdb;pdb.set_trace()
        user.phone = self.cleaned_data['phone']
        user.gender = self.cleaned_data['gender']
        user.city = self.cleaned_data['city']
        user.Area = self.cleaned_data['Area']
        user.state = self.cleaned_data['state']
        user.country = self.cleaned_data['country']
        user.pin_code = self.cleaned_data['pin_code']
        user.type_of_workplace = self.cleaned_data['type_of_workplace']
        user.save()
        return user

        