from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Invoice, InvoiceItem, Product, ProductImage, Transaction
from .pagination import DefaultPagination
from .permissions import IsAdminOrReadOnly
from .serializers import (
    AddInvoiceItemSerializer,
    CreateInvoiceSerializer,
    InvoiceItemSerializer,
    InvoiceSerializer,
    ProductImageSerializer,
    ProductSerializer,
    TransactionSerializer,
)


@extend_schema(tags=["Products"])
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related("images").all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "last_update"]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if InvoiceItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an invoice item."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=["Product Images"])
class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs["product_pk"])


@extend_schema(tags=["Invoices"])
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


@extend_schema(tags=["Invoice Items"])
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


@extend_schema(tags=["Transactions"])
class TransactionViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user_id=self.request.user.id)
