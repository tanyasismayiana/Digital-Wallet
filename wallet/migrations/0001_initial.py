# Generated by Django 4.0.6 on 2022-08-02 16:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField()),
                ('balance', models.IntegerField()),
                ('pin', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=24, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('age', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Walletb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_supported', models.CharField(max_length=27)),
                ('wallet_id', models.IntegerField(null=True)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=14)),
                ('transaction_charge', models.IntegerField()),
                ('transaction_amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=datetime.datetime.now)),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_x', to='wallet.account')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_w', to='wallet.account')),
                ('walletb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.walletb')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.BigIntegerField(null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acc', to='wallet.account')),
                ('walletb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wall', to='wallet.walletb')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('points', models.IntegerField(null=True)),
                ('recepient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(default=datetime.datetime.now)),
                ('receipt_number', models.CharField(max_length=6)),
                ('receipt_file', models.FileField(upload_to='')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notifcation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=10000)),
                ('title', models.CharField(max_length=900)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('r', 'read'), ('u', 'unread')], max_length=7, null='True')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('loan_type', models.CharField(choices=[('Faulu', 'Mshwari'), ('Tala', 'fuliza')], max_length=10, null='True')),
                ('interest_rate', models.SmallIntegerField()),
                ('Date', models.DateTimeField(default=datetime.datetime.now)),
                ('loan_Id', models.CharField(max_length=30)),
                ('loan_term', models.IntegerField()),
                ('walletb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.walletb')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('card', models.CharField(choices=[('D', 'debit'), ('C', 'credit')], max_length=6, null=True)),
                ('card_security_code', models.CharField(max_length=5)),
                ('issuer', models.CharField(max_length=32)),
                ('walletb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.walletb')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer'),
        ),
    ]
