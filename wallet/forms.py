#import libr
from dataclasses import fields
<<<<<<< HEAD
=======
# from email.headerregistry import Address
# from pyexpat import model
>>>>>>> 0b792dfea7a0689969c072de3b428ee6ac422d13
from django import forms

#.current directory
from .models import Card, Customer, Loan, Notifcation, Receipt, Reward, ThirdParty, Transaction, Walletb
from .models import Account

class CustomerRegisterationForm(forms.ModelForm):
    class Meta:   
        model=Customer
        fields=("first_name","last_name","address","email","phone_number","nationality","gender","age","profile_picture")
        widgets={
             "first_name":forms.TextInput(attrs={ 'class': "form-control"}),
             "last_name": forms.TextInput(attrs={ 'class': "form-control"}),
             "address": forms.TextInput(attrs={ 'class': "form-control"}),
             "email": forms.TextInput(attrs={ 'class': "form-control"}),
             "phone_number": forms.TextInput(attrs={ 'class': "form-control"}),
             "gender": forms.Select(attrs={ 'class': "form-control"}),
             "nationality": forms.TextInput(attrs={ 'class': "form-control"}),
             "age": forms.TextInput(attrs={ 'class': "form-control"}),
             "profile_picture":forms.ClearableFileInput(attrs={ 'class': "form-control"}),




        }
class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=("customer","balance","pin","account_number")
        widgets={
            "customer":forms.TextInput(attrs={'class':"form-control"}),
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
            "account_number":forms.TextInput(attrs={'class':"form-control"}),




        }
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Walletb
        fields=("customer","wallet_id","currency_supported")
        widgets={
             "customer":forms.TextInput(attrs={'class':"form-control"}),
             "wallet_id":forms.TextInput(attrs={'class':"form-control"}),
             "currency_supported":forms.NumberInput(attrs={'class':"form-control"}),

        }

class RegisterTransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=("walletb","origin_account","destination_account","transaction_code","transaction_amount","transaction_charge","transaction_date")
        widgets={
            "walletb":forms.TextInput(attrs={'class':"form-control"}),
            "origin_account":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_code":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_charge":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_date":forms.TextInput(attrs={'class':"form-control"}),




        }

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields='__all__'

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields='__all__'

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notifcation
        fields='__all__'
class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields='__all__'
class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields='__all__'
class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields='__all__'

