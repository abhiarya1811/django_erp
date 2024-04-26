from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, user_email_id, user_name=None, user_password=None, user_phone_number=None,
                    user_address=None, **extra_fields):
        """
        Create and return a regular user with an email, username, password, phone number, address, and registration date.
        """
        if not user_email_id:
            raise ValueError('The Email field must be set')
        user = self.model(
            user_email_id=self.normalize_email(user_email_id),
            user_name=user_name,
            user_phone_number=user_phone_number,
            user_address=user_address,
            **extra_fields
        )
        user.set_password(user_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email_id, user_password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True) # by staff means a normal user do not missunderstood with staff
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_email_id, user_password=user_password, **extra_fields)


class CustomUser(AbstractBaseUser):
    user_full_name = models.CharField(max_length=150, null=True, blank=True)
    user_name = models.CharField(max_length=150, null=True, blank=True)
    user_email_id = models.EmailField(unique=True)
    user_phone_number = models.CharField(max_length=15, null=True, blank=True)
    user_address = models.TextField(null=True, blank=True)
    user_registration_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_email_id'
    REQUIRED_FIELDS = ['user_email_id']

    def __str__(self):
        return self.user_email_id



class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_password = models.CharField(max_length=45, null=True)
    admin_name = models.CharField(max_length=45, null=True)
    admin_number = models.CharField(max_length=45, null=True)
    admin_email_id = models.CharField(max_length=45, null=True)
    admin_type = models.CharField(max_length=45, null=True)

class CustomerReturns(models.Model):
    return_id = models.IntegerField(primary_key=True)
    date_of_return = models.CharField(max_length=45, null=True)
    time_of_return = models.CharField(max_length=45, null=True)
    product_return = models.CharField(max_length=45, null=True)
    product_id = models.IntegerField(null=True)
    return_status = models.CharField(max_length=45, null=True)
    additional_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    return_completion_date = models.DateField(null=True)
    return_completion_time = models.CharField(max_length=45, null=True)
    customer_details = models.TextField(null=True)
    return_initiation_date = models.DateField(null=True)
    return_initiation_time = models.CharField(max_length=45, null=True)
    reason_of_return = models.CharField(max_length=45, null=True)
    return_product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)



class Earnings(models.Model):
    sl_no = models.IntegerField(primary_key=True)
    month = models.IntegerField(null=True)
    from_stocks = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    miscellaneous = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_earning = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Exchange(models.Model):
    exchange_id = models.IntegerField(primary_key=True)
    date_of_exchange = models.DateField(null=True)
    time_of_exchange = models.CharField(max_length=45, null=True)
    product_exchanged = models.CharField(max_length=45, null=True)
    product_required = models.CharField(max_length=45, null=True)
    exchange_status = models.CharField(max_length=45, null=True)
    additional_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    exchange_completion_time = models.CharField(max_length=45, null=True)
    exchange_completion_date = models.DateField(null=True)
    exchange_initiation_date = models.DateField(null=True)
    exchange_initiation_time = models.CharField(max_length=45, null=True)
    customer_details = models.TextField(null=True)
    exchange_product_id = models.IntegerField(null=True)
    requested_product_id = models.IntegerField(null=True)
    exchange_product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    requested_product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    reason_of_exchange = models.CharField(max_length=45, null=True)

class Expenditure(models.Model):
    exp_id = models.IntegerField(primary_key=True)
    month = models.IntegerField(null=True)
    staff_salaries_given = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    spent_on_stock = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    spent_on_transportation = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    spent_on_labour = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_exp_by_month = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100, null=True)
    customer_address = models.CharField(max_length=255, null=True)
    customer_mob_num = models.CharField(max_length=15, null=True)
    product_id = models.IntegerField(null=True)
    product_name = models.TextField(null=True)
    order_received_on = models.DateField(null=True)
    order_delivery_date = models.DateField(null=True)
    payment_method = models.CharField(max_length=100, null=True)
    payment_status = models.CharField(max_length=100, null=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    retun_policy = models.CharField(max_length=50, null=True)
    retun_policy_time_period = models.CharField(max_length=45, null=True)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, null=True)
    product_type = models.CharField(max_length=100, null=True)
    product_subtype = models.CharField(max_length=100, null=True)
    product_category = models.CharField(max_length=45, null=True)
    measurements = models.CharField(max_length=100, null=True)
    quality = models.CharField(max_length=100, null=True)
    product_company = models.CharField(max_length=100, null=True)
    gst_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cp_per_item = models.IntegerField(null=True)
    sp_per_item = models.IntegerField(null=True)



class Stock(models.Model):
    stock_id = models.CharField(max_length=50, primary_key=True)
    product_id = models.IntegerField(null=True)
    stock_arrival = models.DateField(null=True)
    stock_status = models.CharField(max_length=100, null=True)
    product_company = models.CharField(max_length=100, null=True)
    stock_quantity_bought = models.IntegerField(null=True)
    stock_quantity_available = models.IntegerField(null=True)
    total_stock_quantity = models.IntegerField(null=True)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available_stock_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bought_stock_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_gst = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Suppliers(models.Model):
    sl_no = models.IntegerField(null=True)
    supplier_id = models.CharField(max_length=45, primary_key=True)
    supplier_name = models.CharField(max_length=60, null=True)
    supplier_address = models.TextField(null=True)
    contact_number = models.IntegerField(null=True)
    company_name_details = models.TextField(null=True)
    product_supplies = models.TextField(null=True)
    product_supplied_till_date = models.IntegerField(null=True)
    dealing_since = models.DateTimeField(null=True)
    deals_completed = models.IntegerField(null=True)
    deals_ongoing = models.IntegerField(null=True)
    deals_completion_time_date = models.IntegerField(null=True)

class TransactionCustomer(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    date_of_transaction = models.DateField(null=True)
    amount_paid_customer = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_sold_details = models.TextField(null=True)
    status_of_transaction = models.CharField(max_length=45, null=True)
    time_of_transaction = models.CharField(max_length=45, null=True)
    order_received_date = models.DateField(null=True)
    order_received_time = models.CharField(max_length=45, null=True)
    date_of_dispatch = models.DateField(null=True)
    time_of_dispatch = models.CharField(max_length=45, null=True)
    order_details_customer = models.CharField(max_length=200, null=True)
    customer_details = models.CharField(max_length=100, null=True)

class TransactionsWholesaler(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    date_of_transaction = models.DateField(null=True)
    time_of_transaction = models.CharField(max_length=45, null=True)
    amount_paid_wholesaler = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_details_sold = models.TextField(null=True)
    transaction_status = models.CharField(max_length=45, null=True)
    stock_details_bought = models.TextField(null=True)
    transaction_status_bought = models.CharField(max_length=45, null=True)
    tansaction_time_bought = models.CharField(max_length=45, null=True)
    transaction_date_bought = models.DateField(null=True)
    purchased_from_franchise = models.TextField(null=True)


