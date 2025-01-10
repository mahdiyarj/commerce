from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from .storage_backends import ProductImageStorage
from .validators import validate_image_size


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name", "last_name"]


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=0, validators=[MinValueValidator(1)]
    )
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        storage=ProductImageStorage(),
        upload_to="",
        blank=True,
        null=True,
        validators=[validate_image_size],
    )


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="invoiceitems"
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(
        max_digits=12, decimal_places=0, validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [["invoice", "product"]]


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"  # Initial state
        COMPLETED = "COMPLETED", "Completed"  # Successfully processed
        FAILED = "FAILED", "Failed"  # Transaction failed

    class TransactionMethod(models.TextChoices):
        IPG = "IPG", "Internet Payment Gateway"
        POS = "POS", "Point of Sale"
        CARD = "CARD", "Card to Card"
        CASH = "CASH", "Cash"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(
        max_digits=12, decimal_places=0, validators=[MinValueValidator(1)]
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
    )
    transaction_method = models.CharField(
        max_length=10, choices=TransactionMethod.choices
    )
