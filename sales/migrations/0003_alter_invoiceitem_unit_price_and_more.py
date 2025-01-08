# Generated by Django 5.1.4 on 2025-01-08 20:20

import django.core.validators
import django.db.models.deletion
import sales.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0002_product_alter_user_email_invoice_invoiceitem_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoiceitem",
            name="unit_price",
            field=models.DecimalField(
                decimal_places=0,
                max_digits=12,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.DecimalField(
                decimal_places=0,
                max_digits=12,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        storage=sales.storage_backends.ProductImageStorage(),
                        upload_to="",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="sales.product",
                    ),
                ),
            ],
        ),
    ]
