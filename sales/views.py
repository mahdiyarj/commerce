from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Invoice, InvoiceItem, Product
from .serializers import (
    AddInvoiceItemSerializer,
    InvoiceItemSerializer,
    InvoiceSerializer,
    ProductSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InvoiceViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
):
    queryset = Invoice.objects.prefetch_related("items__product").all()
    serializer_class = InvoiceSerializer


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
