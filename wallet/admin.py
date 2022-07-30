from django.contrib import admin

from .models import Customer
from .models import Account
from .models import Walletb
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notifcation
from .models import Receipt
from .models import Loan
from .models import Reward




admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Walletb)
admin.site.register(Transaction)
admin.site.register(Card)
# admin.site.register(Transaction)
admin.site.register(ThirdParty)
admin.site.register(Notifcation)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)




# class CustomerAdmin(admin.ModelAdmin):
#      list_display=('first_name','last_name','age','email')
#      search_fields=('first_name','last_name')
# admin.site.register(Customer,CustomerAdmin)

# Register your models here.
