from unicodedata import name
from django.urls import path 
from .views import home_page, list_accounts, list_card, list_customers, list_loan, list_receipts, list_reward, list_thirdparty, list_transaction, list_wallet, notification_list, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet
from .views import search
urlpatterns=[
    path("",home_page,name='home'),
    path("customers/",list_customers,name='all_customers'),
    path("customers_get/",search.as_view(),name='find_customer'),
    path("registercust/",register_customer,name='registration'),
    path("register_account/",register_account,name='account'),
    path("accounts/",list_accounts,name='all_accounts'),

    path("register_wallet/",register_wallet,name='wallet'),
    path("wallets/",list_wallet,name='all_wallets'),


    path("register_transaction/",register_transaction,name='Transaction'),
    path("transactions/",list_transaction,name='all_transactions'),


    path('card/',register_card,name="card"),
    path("cards/",list_card,name='all_cards'),

    path('thirdp/',register_thirdparty,name='thirdparty'),
    path('thirdpartys/',list_thirdparty,name='all_thirdpartys'),

    path('notification/',register_notification,name='notification'),
    path('notifications/',notification_list,name='all_notifications'),



    path('loan/',register_loan,name='loan'),
    path('loans/',list_loan,name='all_loans'),

    path('receipt/',register_receipt,name='receipt'),
    path('receipts/',list_receipts,name='all_receipts'),

    path('reward/',register_reward,name='reward'),
        path('rewards/',list_reward,name='all_rewards'),


    
        


    
]
