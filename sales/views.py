from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Invoice, InvoiceItem, Product, Transaction
from .serializers import (
    AddInvoiceItemSerializer,
    CreateInvoiceSerializer,
    InvoiceItemSerializer,
    InvoiceSerializer,
    ProductSerializer,
    TransactionSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InvoiceViewSet(ModelViewSet):
    http_method_names = ["get", "post", "head", "options"]

    def get_queryset(self):
        return Invoice.objects.prefetch_related("items__product").filter(
            user_id=self.request.user.id
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateInvoiceSerializer
        return InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateInvoiceSerializer(
            data=request.data, context={"user_id": self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        invoice = serializer.save()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)


class InvoiceItemViewSet(ModelViewSet):
    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddInvoiceItemSerializer
        return InvoiceItemSerializer

    def get_serializer_context(self):
        return {"invoice_id": self.kwargs["invoice_pk"]}

    def get_queryset(self):
        return InvoiceItem.objects.filter(
            invoice_id=self.kwargs["invoice_pk"]
        ).select_related("product")


class TransactionViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
