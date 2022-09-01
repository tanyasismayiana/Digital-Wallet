from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegisterationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RegisterTransactionForm, RewardRegistrationForm, ThirdPartyRegistrationForm, WalletRegistrationForm



# Create your views here.han
def register_customer(request):

   
    form=CustomerRegisterationForm()
    return render(request,"wallet/register_customer.html",
        {"formi":form
    })
def register_account(request):
    form_account=AccountRegistrationForm()
    return render(request,'wallet/register_account.html',
    {"form":form_account}
    )
def register_wallet(request):
    form_wallet=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",
    {"wallet":form_wallet}
    )
def register_transaction(request):
    form_transact=RegisterTransactionForm()
    return render(request,"wallet/register_transaction.html",
    {"transact":form_transact}
    )
def register_card(request):
    card_form=CardRegistrationForm()
    return render(request,"wallet/card_register.html",
    {"card":card_form}
    )
def register_thirdparty(request):
    thirdparty_form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdp.html",
    {"third":thirdparty_form}
    )
def register_notification(request):
    form_notify=NotificationRegistrationForm
    return render(request,"wallet/register_notification.html",
    {"notify":form_notify}
    )
def register_loan(request):
    loan_form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",
    {"loan":loan_form}
    )
def register_reward(request):
    reward_form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",
    {"reward":reward_form}
    )
def register_receipt(request):
    receipt_form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",
    {"receipt":receipt_form}
    )




