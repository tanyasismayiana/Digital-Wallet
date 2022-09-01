#import libr
from dataclasses import fields
from email.headerregistry import Address
from pyexpat import model
from django import forms

#.current directory
from .models import Card, Customer, Loan, Notifcation, Receipt, Reward, ThirdParty, Transaction, Walletb
from .models import Account

class CustomerRegisterationForm(forms.ModelForm):
    class Meta:   #inherits from the parent and overrides
        model=Customer
        fields=("first_name","last_name","Address","email","phone_number")
        widgets={
             "first_name".
        }
class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Walletb
        fields='__all__'

class RegisterTransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields='__all__'

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

