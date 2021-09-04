from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(cat_master_v3)
admin.site.register(sub_cat_v3)
admin.site.register(expense_details_v3)
