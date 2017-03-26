from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class DepositeForm(forms.Form):
    Text1=forms.IntegerField(required=True,max_value=9999,min_value=0,label='Serial Key')
    Text2 = forms.IntegerField(required=True, max_value=9999, min_value=0, label=' ')
    Text3 = forms.IntegerField(required=True, max_value=9999, min_value=0, label=' ')
    Text4 = forms.IntegerField(required=True, max_value=9999, min_value=0, label=' ')

class Transaction(forms.Form):
    amt=forms.IntegerField(required=True,min_value=0,label='Amount to be Transfer')


class OtherAccountForm(forms.Form):
    account=forms.CharField(required=True,label='Account in which amount is to be transfer')
    name=forms.CharField(required=True,label='Username of reciever')
    ifsc=forms.CharField(required=True,label='IFSC code of reciever')
    phone=forms.CharField(required=True,label='Phone no. of reciever')
    email=forms.EmailField(required=True,label='email of reciever')

class AccountForm(forms.ModelForm):
    accountno=forms.CharField(required=True)
    class Meta:
        model=UserProfile
        fields=(
            'accountno',
            'IFSC_Code',
            'name',
            'description',
            'city',
            'phone',
            'address',
            'balance',
        )


class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user =super(RegistrationForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Editform(UserChangeForm):
    class Meta:
        model=User
        fields=(
            'first_name',
            'last_name',
            'email',
            'password'
        )