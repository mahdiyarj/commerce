from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from .models import Invoice, InvoiceItem, Product, Transaction


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "price",
        ]


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title"]


class InvoiceItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, invoice_item: InvoiceItem):
        return invoice_item.quantity * invoice_item.unit_price

    class Meta:
        model = InvoiceItem
        fields = ["id", "product", "quantity", "unit_price", "total_price"]


class AddInvoiceItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("No product with the given ID was found.")
        return value

    def save(self, **kwargs):
        invoice_id = self.context["invoice_id"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]

        try:
            invoice_item = InvoiceItem.objects.get(
                invoice_id=invoice_id, product_id=product_id
            )
            invoice_item.quantity += quantity
            invoice_item.save()
            self.instance = invoice_item
        except InvoiceItem.DoesNotExist:
            self.instance = InvoiceItem.objects.create(
                invoice_id=invoice_id, **self.validated_data
            )

        return self.instance

    class Meta:
        model = InvoiceItem
        fields = [
            "id",
            "product_id",
            "unit_price",
            "quantity",
        ]  # TODO Default value for unit_price from product


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, invoice):
        return sum([item.quantity * item.unit_price for item in invoice.items.all()])

    class Meta:
        model = Invoice
        fields = ["id", "user", "created_at", "items", "total_price"]


class CreateInvoiceSerializer(serializers.Serializer):
    def save(self, **kwargs):
        invoice = Invoice.objects.create(user_id=self.context["user_id"])

        return invoice


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
            "invoice",
            "created_at",
            "amount",
        ]
