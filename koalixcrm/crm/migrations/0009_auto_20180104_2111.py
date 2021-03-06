# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20180104_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='defaultcurrency',
            new_name='default_currency',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='defaultcustomer',
            new_name='default_customer',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='defaultSupplier',
            new_name='default_supplier',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='derivatedFromQuote',
            new_name='derived_from_quote',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='payableuntil',
            new_name='payable_until',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='paymentBankReference',
            new_name='payment_bank_reference',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='lastCalculatedPrice',
            new_name='last_calculated_price',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='lastCalculatedTax',
            new_name='last_calculated_tax',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='lastPricingDate',
            new_name='last_pricing_date',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='overwriteProductPrice',
            new_name='overwrite_product_price',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='positionNumber',
            new_name='position_number',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='sentOn',
            new_name='sent_on',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='accoutingProductCategorie',
            new_name='accounting_product_categorie',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='defaultunit',
            new_name='default_unit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productNumber',
            new_name='product_number',
        ),
        migrations.RenameField(
            model_name='purchaseconfirmation',
            old_name='validuntil',
            new_name='valid_until',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='externalReference',
            new_name='external_reference',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='lastCalculatedPrice',
            new_name='last_calculated_price',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='lastCalculatedTax',
            new_name='last_calculated_tax',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='lastPricingDate',
            new_name='last_pricing_date',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='validuntil',
            new_name='valid_until',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='externalReference',
            new_name='external_reference',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='lastCalculatedPrice',
            new_name='last_calculated_price',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='lastCalculatedTax',
            new_name='last_calculated_tax',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='salescontract',
            old_name='lastPricingDate',
            new_name='last_pricing_date',
        ),
    ]
