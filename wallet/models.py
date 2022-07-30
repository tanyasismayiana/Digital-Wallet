from datetime import datetime
from distutils.command.upload import upload
from enum import unique
from mailbox import BabylMessage
from random import choices
from re import A
from secrets import choice
# from tkinter import CASCADE
# from tkinter import CASCADE
from unicodedata import name
from xml.etree.ElementInclude import default_loader
# import profile
from django.db import models


class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    Address=models.TextField()
    email= models.EmailField()
    phone_number= models.CharField(max_length=15)
    gender= models.CharField(max_length=10)
    nationality=models.CharField(null=True,max_length=24)
    profile_picture=models.ImageField(null=True,blank=True,upload_to="images/")
    age= models.PositiveBigIntegerField()

class Account(models.Model):
        account_number= models.PositiveIntegerField()
        customer=models.ForeignKey(null=True,on_delete = models.CASCADE,to=Customer)
        balance=models.IntegerField()
        pin=models.PositiveSmallIntegerField()

class Walletb(models.Model):
    customer=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Customer)
    currency_supported=models.CharField(max_length=27)

class Transaction(models.Model):
    walletb=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Walletb)
    account=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account)
    account=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account)
    transaction_code=models.CharField(max_length=14)
    transaction_charge=models.IntegerField()
    transaction_amount=models.IntegerField()
    transaction_date=models.DateTimeField(default=datetime.now)
    # receipt=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Receipt)
    date=models.DateTimeField(default=datetime.now)
class Card(models.Model):
    card_number=models.IntegerField()
    card_holder_name=models.CharField(max_length=23)
    expiry_date=models.DateTimeField(default=datetime.now)
    card_type_choices=(
        ('D','debit'),
        ('C','credit')


    )
    card=models.CharField(max_length=6,choices=card_type_choices,null=True)
    card_security_code=models.CharField(max_length=5)
    issuer=models.CharField(max_length=32)
    account=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account)
    walletb=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Walletb)
class ThirdParty(models.Model):
    transaction_cost=models.IntegerField()
    account=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account)
class Notifcation(models.Model):
    Message=models.CharField(max_length=10000)
    title=models.CharField(max_length=900)
    date=models.DateTimeField(default=datetime.now)
    notifiaction_type=models.CharField(max_length=6)
    state=(
        ('r','read'),
        ('u','unread')
    )
    status=models.CharField(max_length=7,choices=state,null='True')
    walletb=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Walletb)
class Receipt(models.Model):
    receipt_date=models.DateTimeField(default=datetime.now)
    receipt_number=models.CharField(max_length=6)
    total_amount=models.IntegerField()
    receipt_file=models.FileField()  
    transaction=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Transaction)
class Loan(models.Model):
    Amount=models.IntegerField()
    loan_typ=(
        ('Faulu','Mshwari'),
        ('Tala','fuliza')
    )
    loan_type=models.CharField(max_length=10,choices=loan_typ,null='True')
    interest_rate=models.SmallIntegerField()
    Date=models.DateTimeField(default=datetime.now)
    loan_Id=models.CharField(max_length=30)
    walletb=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Walletb)
    
    loan_term=models.IntegerField()
class Reward(models.Model):
     date=models.DateTimeField(default=datetime.now)
     recepient=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Customer)
     transaction=models.ForeignKey(default=1,on_delete=models.CASCADE,to=Transaction)







        



        


# Create your models here.
