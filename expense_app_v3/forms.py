from .models import *
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = cat_master_v3
        fields = ['cat_name', 'date_created']

class SubCatForm(ModelForm):
    class Meta:
        model = sub_cat_v3
        fields = '__all__'
        exclude = ['date_modified', 'cby', 'mby']

class ExpenseForm(ModelForm):
    class Meta:
        model = expense_details_v3
        fields = '__all__'
        exclude = ['date_modified', 'm_user', 'c_user']