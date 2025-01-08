from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("invoices", views.InvoiceViewSet, basename="invoices")
router.register("transactions", views.TransactionViewSet, basename="transactions")

products_router = NestedDefaultRouter(router, "products", lookup="product")
products_router.register("images", views.ProductImageViewSet, basename="product-images")

invoices_router = NestedDefaultRouter(router, "invoices", lookup="invoice")
invoices_router.register("items", views.InvoiceItemViewSet, basename="invoice-items")


urlpatterns = router.urls + invoices_router.urls + products_router.urls
