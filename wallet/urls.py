from unicodedata import name
from django.urls import path 
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet
urlpatterns=[
    path("registercust/",register_customer,name='registration'),
    path("register_account/",register_account,name='account'),
    path("register_wallet/",register_wallet,name='wallet'),
    path("register_transaction/",register_transaction,name='Transaction'),
    path('card/',register_card,name="card"),
    path('thirdp/',register_thirdparty,name='thirdparty'),
    path('notification/',register_notification,name='notification'),
    path('loan/',register_loan,name='loan'),
    path('receipt/',register_receipt,name='receipt'),
    path('reward/',register_reward,name='reward'),

    
        


    
]
