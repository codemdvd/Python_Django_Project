# Generated by Django 4.0.5 on 2022-12-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('car_vin_code', models.CharField(max_length=30)),
                ('car_brand', models.CharField(max_length=20)),
                ('engine_type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryClassifier',
            fields=[
                ('delivery_code', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('delivery_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'delivery_classifier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HelloTask',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('task_id', models.IntegerField()),
                ('task_name', models.CharField(max_length=30)),
                ('creation_date', models.DateField()),
                ('period_of_execution', models.CharField(max_length=20)),
                ('contact_person_id', models.IntegerField()),
                ('executor_id', models.IntegerField()),
                ('contract_number', models.IntegerField()),
                ('task_status', models.CharField(max_length=30)),
                ('author_id', models.IntegerField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'hello_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sending_date', models.DateField()),
                ('recieving_date', models.DateField(blank=True, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'income',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStausClassifier',
            fields=[
                ('ord_status_code', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('ord_stat_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'order_staus_classifier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderTable',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('payment_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('sets_left', models.SmallIntegerField()),
                ('detail_number', models.CharField(max_length=30)),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('product_price', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoleClassifier',
            fields=[
                ('role_code', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'role_classifier',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='ContactPerson',
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.DeleteModel(
            name='ContractEquipment',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='PositionDictionary',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
        migrations.CreateModel(
            name='IncomeProduct',
            fields=[
                ('amount', models.SmallIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='hello.product')),
            ],
            options={
                'db_table': 'income_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='hello.ordertable')),
                ('amount', models.SmallIntegerField(blank=True, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
            ],
            options={
                'db_table': 'order_product',
                'managed': False,
            },
        ),
    ]
