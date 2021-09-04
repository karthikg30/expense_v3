from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import * 
from django.db.models import Sum
import psycopg2 as sql
from .models import *

# login and logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decoraters import userauthentic_register_login

# Create your views here.

#login Page goes here 
@userauthentic_register_login
def loginpage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username,password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or password')
    
    else:
        return render (request, 'expense/loginpage.html')

#logut pages goes here 
def logoutpage(request):
    logout(request)
    return redirect ('loginpage')


#Home page
@login_required (login_url= 'loginpage')
def home(request):
    category = CategoryForm()
    sub_cat = SubCatForm()
    expform = ExpenseForm()


    if request.method == "POST":
        form_save = CategoryForm(request.POST)
        sub_form_save = SubCatForm(request.POST)
        expform = ExpenseForm(request.POST)

        if form_save.is_valid():
            form_save.save()
            return redirect ('homepage')
        
        if sub_form_save.is_valid():
            sub_form_save.save()
            return redirect ('homepage')
        
        if expform.is_valid():
            expform.save()
            return redirect ('homepage')

    context = {'form': category, 'form2':sub_cat, 'form3': expform}
    return render(request, 'expense/data_load.html', context)


@login_required (login_url= 'loginpage')
def dashboard(request):
    #totalexp = expense_details_v3.objects.values('cat_code').annotate(Sum('amount'))
    
    cat_form = cat_master_v3.objects.all
    sub_cat_form = sub_cat_v3.objects.all

    conn = sql.connect(host="localhost",database="postgres",user="postgres", password="CG-vak123")
    cur = conn.cursor()
    total_saving = cur.execute("SELECT public.fn_total_savings()")
    context = {"saving":total_saving}
    cur.close()
    conn.commit()
    
    return render (request, 'expense/dashboard.html', {'cat_form':cat_form,"sub_cat_form":sub_cat_form })

@login_required (login_url= 'loginpage')
def load_data(request):

    cat_form = cat_master_v3.objects.all
    sub_cat_form = sub_cat_v3.objects.all

    #context = {'cat_form':cat_form,"sub_cat_form":sub_cat_form }

    if request.method == 'POST':
        val1 = request.POST['date_in']
        val2 = request.POST['amount']
        val3 = request.POST['income']

        conn = sql.connect(host="localhost",database="postgres",user="postgres", password="CG-vak123")
        cur = conn.cursor()
        cur.execute('call sp_insert_credit_details (%s, %s,%s);',(val1, val2, val3))

        cur.close()
        conn.commit()
        conn.close()

    return render (request, 'expense/dashboard.html', {'cat_form':cat_form,"sub_cat_form":sub_cat_form })


@login_required (login_url= 'loginpage')
def exp_load_data(request):

    cat_form = cat_master_v3.objects.all
    sub_cat_form = sub_cat_v3.objects.all

    #context = {'cat_form':cat_form,"sub_cat_form":sub_cat_form }

    if request.method == 'POST':
        val1 = request.POST["date_in"]
        val2 = request.POST["cat_code"]
        val3 = request.POST["sub_cat"]
        val4 = request.POST["amount"]
        val5 = request.POST["remarks"]

        conn = sql.connect(host="localhost",database="postgres",user="postgres", password="CG-vak123")
        cur = conn.cursor()
        
        cur.execute('call sp_insert_data_expense_me (%s, %s, %s, %s, %s);',(val1, val2, val3, val4, val5))
        
        cur.close()
        conn.commit()
        conn.close()

    return render (request, 'expense/dashboard.html', {'cat_form':cat_form,"sub_cat_form":sub_cat_form })


@login_required (login_url='loginpage')
def consolidate (request):

    cat_form = cat_master_v3.objects.all
    sub_cat_form = sub_cat_v3.objects.all
    
    if request.method == 'POST':
        consol_date = request.POST["process_date"]
        
        query = 'call public.sp_total_savings (\'{}\');'.format(consol_date)
        
        conn = sql.connect(host="localhost",database="postgres",user="postgres", password="CG-vak123")
        cur = conn.cursor()
        
        #cur.execute('call sp_total_savings (%s);',(consol_date))
        cur.execute(query)
        
        cur.close()
        conn.commit()   
        conn.close()

    return render (request, 'expense/dashboard.html', {'cat_form':cat_form,"sub_cat_form":sub_cat_form })



@login_required (login_url= 'loginpage')
def viewpage(request):
    category = cat_master_v3.objects.all()
    sub_cat = sub_cat_v3.objects.all()

    
    
    context = {'cat':category, 'sub':sub_cat}
    return render (request, 'expense/viewpage.html', context)

@login_required (login_url= 'loginpage')
def expense_page(request):
    exp_details = expense_details_v3.objects.all().order_by('id')
    context = {'exp':exp_details}
    return render (request, 'expense/Expense_details.html', context)

@login_required (login_url= 'loginpage')
def editdate (request,pk):

    exp_details = expense_details_v3.objects.get(id = pk)
    context = {'exp':exp_details}

    return (request, 'expense/Expense_details.html', context)

'''
def sub_cat(request):

    subcat_ip = SubCatForm()
    if request.method == "POST":
        subcat_form = SubCatForm(request.POST)

        if subcat_form.is_valid():
            subcat_form.save()
            return redirect ('sub_cat')
    
    context = {'form': subcat_ip}

    return render (request, 'expense/sub_cat.html', context)
    '''

@login_required (login_url= 'loginpage')
def js(request):
    return render (request, 'expense/js.html')