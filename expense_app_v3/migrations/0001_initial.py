# Generated by Django 3.1.7 on 2021-04-21 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_master_v3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('cat_name', models.CharField(max_length=50)),
                ('cby', models.CharField(blank=True, default='app_user', max_length=25, null=True)),
                ('mby', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_cat_v3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('sub_name', models.CharField(max_length=50)),
                ('cby', models.CharField(blank=True, default='app_user', max_length=25, null=True)),
                ('mby', models.CharField(blank=True, max_length=25, null=True)),
                ('cat_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_app_v3.cat_master_v3')),
            ],
        ),
        migrations.CreateModel(
            name='expense_details_v3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateField(auto_created=True, blank=True, null=True)),
                ('date_created', models.DateField(auto_created=True, blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('c_user', models.CharField(blank=True, max_length=20, null=True)),
                ('m_user', models.CharField(blank=True, max_length=20, null=True)),
                ('cat_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expense_app_v3.cat_master_v3')),
                ('sub_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expense_app_v3.sub_cat_v3')),
            ],
        ),
    ]
