from django.shortcuts import render, redirect
from .models import Earnings, Exchange, Expenditure, Orders, Product,  Stock, Suppliers, TransactionCustomer, TransactionsWholesaler, CustomerReturns
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, CustomUser
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone



def main(request):
    if request.method == 'POST':
        if 'register_admin' in request.POST:
            return redirect('admin_register')
        elif 'admin_login' in request.POST:
            return redirect('admin_login')

    registration_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'main.html', {'registration_form': registration_form, 'login_form': login_form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin/login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')  


def admin_register(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        admin_password = request.POST.get('admin_password')
        admin_name = request.POST.get('admin_name')
        admin_number = request.POST.get('admin_number')
        admin_email_id = request.POST.get('admin_email_id')
        admin_type = request.POST.get('admin_type')
        
        
        admin = Admin(
            admin_id=admin_id,
            admin_password=admin_password,
            admin_name=admin_name,
            admin_number=admin_number,
            admin_email_id=admin_email_id,
            admin_type=admin_type
        )
        
        
        admin.save()
        
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('admin_login')
    
    return render(request, 'admin/register.html')

def earnings_view(request):
    earnings_data = Earnings.objects.all()
    return render(request, 'earnings.html', {'earnings_data': earnings_data})

def exchange_view(request):
    exchange_data = Exchange.objects.all()
    return render(request, 'exchange.html', {'exchange_data': exchange_data})

def expenditure_view(request):
    expenditure_data = Expenditure.objects.all()
    return render(request, 'expenditure.html', {'expenditure_data': expenditure_data})

def orders_view(request):
    orders_data = Orders.objects.all()
    return render(request, 'orders.html', {'orders_data': orders_data})

def product_list(request):
    product_data = Product.objects.all()
    return render(request, 'product_list.html', {'product_data': product_data})

def stock_view(request):
    stock_data = Stock.objects.all()
    return render(request, 'stock.html', {'stock_data': stock_data})

def suppliers_view(request):
    suppliers_data = Suppliers.objects.all()
    return render(request, 'suppliers.html', {'suppliers_data': suppliers_data})

def transaction_customer_view(request):
    transaction_customer_data = TransactionCustomer.objects.all()
    return render(request, 'transaction_customer.html', {'transaction_customer_data': transaction_customer_data})

def transactions_wholesaler_view(request):
    transaction_wholesaler_data = TransactionsWholesaler.objects.all()
    return render(request, 'transaction_wholesaler.html', {'transaction_wholesaler_data': transaction_wholesaler_data})


def customer_returns_view(request):
    customer_returns_data = CustomerReturns.objects.all()
    return render(request, 'return.html', {'customer_return_data': customer_returns_data})


def user_register(request):
    if request.method == 'POST':
        user_full_name = request.POST.get('user_full_name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        user_email_id = request.POST.get('email_id', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        registration_date = request.POST.get('registration_date', '')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('user_register')
            else:
                # this is the default user for django.
                user1 = User.objects.create_user(
                    username=username,
                    password=password,
                    email=user_email_id
                )
                
                # this is the custom user object.
                custom_user = CustomUser.objects.create(
                    user=user1,  # Assuming 'username' is the correct field
                    user_full_name=user_full_name,
                    user_email_id=user_email_id,
                    user_phone_number=phone_number,
                    user_address=address,
                    user_registration_date=timezone.now()
                )
                messages.success(request, 'Account created successfully. You can now login.')
                return redirect('user_login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('user_register')

    return render(request, 'user_register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('user_login')

    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')

