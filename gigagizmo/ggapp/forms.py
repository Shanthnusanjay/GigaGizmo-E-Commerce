from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Address

class UserFrom(UserCreationForm):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=15)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        ]


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = [
            'phone'
        ]

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'building_name',
            'street',
            'landmark',
            'city',
            'state',
            'zipcode'
        ]

class SetAddressForm(forms.Form):
    delivery_address = forms.CharField()