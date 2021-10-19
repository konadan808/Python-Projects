from django.contrib import admin

# Register your models here.
from .models import Account
admin.site.register(Account)

from .models import Transaction
admin.site.register(Transaction)