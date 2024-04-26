from django.urls import path, include
from django.shortcuts import redirect
from .views import main, admin_login, admin_logout, admin_register, product_list, earnings_view, exchange_view, expenditure_view, orders_view, stock_view, suppliers_view, transaction_customer_view, transactions_wholesaler_view, customer_returns_view, user_register, user_login, user_logout

urlpatterns = [
    path('', lambda request: redirect('admin_login'), name='home'),
    path('main/', main, name='main'),
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/register/', admin_register, name='admin_register'),
    path('products/', product_list, name='product_list'),
    path('earnings/', earnings_view, name='earnings'),
    path('exchange/', exchange_view, name='exchange'),
    path('expenditure/', expenditure_view, name='expenditure'),
    path('orders/', orders_view, name='orders'),
    path('stock/', stock_view, name='stock'),
    path('suppliers/', suppliers_view, name='suppliers'),
    path('transaction/customer/', transaction_customer_view, name='transaction_customer'),
    path('transactions/wholesaler/', transactions_wholesaler_view, name='transactions_wholesaler'),
    path('returns/', customer_returns_view, name='customer_returns'),
    path('user/register/', user_register, name='user_register'),
    path('user/login/', user_login, name='user_login'),
    path('user/logout/', user_logout, name='user_logout'),
]
