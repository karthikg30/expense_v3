# Generated by Django 3.1.7 on 2021-04-21 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0003_auto_20210422_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense_details',
            name='cat_code',
        ),
        migrations.RemoveField(
            model_name='expense_details',
            name='sub_code',
        ),
        migrations.RemoveField(
            model_name='sub_cat',
            name='cat_code',
        ),
        migrations.DeleteModel(
            name='cat_master',
        ),
        migrations.DeleteModel(
            name='expense_details',
        ),
        migrations.DeleteModel(
            name='sub_cat',
        ),
    ]
