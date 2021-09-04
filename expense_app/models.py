from django.db import models
# Create your models here.
class cat_master_v3(models.Model):
    cat_name = models.CharField(max_length= 50, null = False)
    date_created = models.DateTimeField(auto_created=True, null = True, blank=True)
    cby = models.CharField(max_length=25, default='app_user', null = True, blank=True)
    date_modified = models.DateTimeField(auto_created= True, null = True, blank=True)
    mby = models.CharField(max_length= 25, null = True, blank=True)

    def __str__(self):
        return self.cat_name

class sub_cat_v3(models.Model):
    cat_code = models.ForeignKey(cat_master_v3, on_delete = models.CASCADE)
    sub_name = models.CharField(max_length= 50, null = False)
    date_created = models.DateTimeField(auto_created=True, null = True, blank=True)
    cby = models.CharField(max_length=25, default='app_user', null = True, blank=True)
    date_modified = models.DateTimeField(auto_created= True, null = True, blank=True)
    mby = models.CharField(max_length= 25, null = True, blank=True)

    def __str__(self):
        return (self.cat_code.cat_name + '-' + self.sub_name)

class expense_details_v3(models.Model):
    cat_code = models.ForeignKey(cat_master_v3, null = True, on_delete = models.DO_NOTHING)
    sub_code = models.ForeignKey(sub_cat_v3, null = True, on_delete = models.DO_NOTHING)
    amount = models.DecimalField(max_digits= 6, decimal_places= 2, null = False)
    remarks = models.CharField(max_length= 200, null = True, blank = True)
    date_created = models.DateField(auto_created= True, null = True, blank = True)
    c_user = models.CharField(max_length=20, null = True, blank = True)
    date_modified = models.DateField(auto_created= True, null = True, blank = True)
    m_user = models.CharField(max_length=20, blank = True, null = True)

    def __str__(self):
        return (self.cat_code.cat_name + '-' + self.sub_code.sub_name + '-' + self.amount)