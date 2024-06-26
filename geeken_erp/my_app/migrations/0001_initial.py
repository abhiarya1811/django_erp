# Generated by Django 5.0.2 on 2024-04-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_password', models.CharField(max_length=45, null=True)),
                ('admin_name', models.CharField(max_length=45, null=True)),
                ('admin_number', models.CharField(max_length=45, null=True)),
                ('admincol', models.CharField(max_length=45, null=True)),
                ('admin_email_id', models.CharField(max_length=45, null=True)),
                ('admin_type', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReturns',
            fields=[
                ('return_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_return', models.CharField(max_length=45, null=True)),
                ('time_of_return', models.CharField(max_length=45, null=True)),
                ('product_return', models.CharField(max_length=45, null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('return_status', models.CharField(max_length=45, null=True)),
                ('additional_amount_paid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('return_completion_date', models.DateField(null=True)),
                ('return_completion_time', models.CharField(max_length=45, null=True)),
                ('customer_details', models.TextField(null=True)),
                ('return_initiation_date', models.DateField(null=True)),
                ('return_initiation_time', models.CharField(max_length=45, null=True)),
                ('reason_of_return', models.CharField(max_length=45, null=True)),
                ('return_product_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('sl_no', models.IntegerField(primary_key=True, serialize=False)),
                ('month', models.IntegerField(null=True)),
                ('from_stocks', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('miscellaneous', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_earning', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('exchange_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_exchange', models.DateField(null=True)),
                ('time_of_exchange', models.CharField(max_length=45, null=True)),
                ('product_exchanged', models.CharField(max_length=45, null=True)),
                ('product_required', models.CharField(max_length=45, null=True)),
                ('exchange_status', models.CharField(max_length=45, null=True)),
                ('additional_amount_paid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('exchange_completion_time', models.CharField(max_length=45, null=True)),
                ('exchange_completion_date', models.DateField(null=True)),
                ('exchange_initiation_date', models.DateField(null=True)),
                ('exchange_initiation_time', models.CharField(max_length=45, null=True)),
                ('customer_details', models.TextField(null=True)),
                ('exchange_product_id', models.IntegerField(null=True)),
                ('requested_product_id', models.IntegerField(null=True)),
                ('exchange_product_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('requested_product_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('reason_of_exchange', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('exp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('month', models.IntegerField(null=True)),
                ('staff_salaries_given', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('spent_on_stock', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('spent_on_transportation', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('spent_on_labour', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_exp_by_month', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('customer_address', models.CharField(max_length=255, null=True)),
                ('customer_mob_num', models.CharField(max_length=15, null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('product_name', models.TextField(null=True)),
                ('order_received_on', models.DateField(null=True)),
                ('order_delivery_date', models.DateField(null=True)),
                ('payment_method', models.CharField(max_length=100, null=True)),
                ('payment_status', models.CharField(max_length=100, null=True)),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('advance_payment', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('remaining_payment', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('retun_policy', models.CharField(max_length=50, null=True)),
                ('retun_policy_time_period', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_type', models.CharField(max_length=100, null=True)),
                ('product_subtype', models.CharField(max_length=100, null=True)),
                ('product_category', models.CharField(max_length=45, null=True)),
                ('measurements', models.CharField(max_length=100, null=True)),
                ('quality', models.CharField(max_length=100, null=True)),
                ('product_company', models.CharField(max_length=100, null=True)),
                ('gst_per_item', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('cp_per_item', models.IntegerField(null=True)),
                ('sp_per_item', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(null=True)),
                ('stock_arrival', models.DateField(null=True)),
                ('stock_status', models.CharField(max_length=100, null=True)),
                ('product_company', models.CharField(max_length=100, null=True)),
                ('stock_quantity_bought', models.IntegerField(null=True)),
                ('stock_quantity_available', models.IntegerField(null=True)),
                ('total_stock_quantity', models.IntegerField(null=True)),
                ('cost_per_item', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('available_stock_cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('bought_stock_cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('stock_cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('stock_gst', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('sl_no', models.IntegerField(null=True)),
                ('supplier_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=60, null=True)),
                ('supplier_address', models.TextField(null=True)),
                ('contact_number', models.IntegerField(null=True)),
                ('company_name_details', models.TextField(null=True)),
                ('product_supplies', models.TextField(null=True)),
                ('product_supplied_till_date', models.IntegerField(null=True)),
                ('dealing_since', models.DateTimeField(null=True)),
                ('deals_completed', models.IntegerField(null=True)),
                ('deals_ongoing', models.IntegerField(null=True)),
                ('deals_completion_time_date', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionCustomer',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_transaction', models.DateField(null=True)),
                ('amount_paid_customer', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('stock_sold_details', models.TextField(null=True)),
                ('status_of_transaction', models.CharField(max_length=45, null=True)),
                ('time_of_transaction', models.CharField(max_length=45, null=True)),
                ('order_received_date', models.DateField(null=True)),
                ('order_received_time', models.CharField(max_length=45, null=True)),
                ('date_of_dispatch', models.DateField(null=True)),
                ('time_of_dispatch', models.CharField(max_length=45, null=True)),
                ('order_details_customer', models.CharField(max_length=200, null=True)),
                ('customer_details', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsWholesaler',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_transaction', models.DateField(null=True)),
                ('time_of_transaction', models.CharField(max_length=45, null=True)),
                ('amount_paid_wholesaler', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('stock_details_sold', models.TextField(null=True)),
                ('transaction_status', models.CharField(max_length=45, null=True)),
                ('stock_details_bought', models.TextField(null=True)),
                ('transaction_status_bought', models.CharField(max_length=45, null=True)),
                ('tansaction_time_bought', models.CharField(max_length=45, null=True)),
                ('transaction_date_bought', models.DateField(null=True)),
                ('purchased_from_franchise', models.TextField(null=True)),
            ],
        ),
    ]
