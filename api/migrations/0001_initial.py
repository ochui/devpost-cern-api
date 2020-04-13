# Generated by Django 3.0.5 on 2020-04-13 12:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceManger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('resource_type', models.CharField(choices=[('Seller', 'Seller'), ('pharmacist', 'Pharmacist')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=100)),
                ('resource_type', models.CharField(choices=[('PHARMACY', 'Pharmacy'), ('STORE', 'Store'), ('MARKET', 'Market')], default='STORE', max_length=15)),
                ('resource_status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=15)),
                ('resource_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ResourceManger')),
            ],
            options={
                'verbose_name': 'Resource Center',
                'verbose_name_plural': 'Resource Centers',
            },
        ),
    ]