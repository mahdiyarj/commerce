import pytest
from model_bakery import baker
from rest_framework import status

from sales.models import Product


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post("/sales/products/", product)

    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product):
        authenticate()

        response = create_product({"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_product):
        authenticate(is_staff=True)

        response = create_product({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_product):
        authenticate(is_staff=True)

        response = create_product({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f"/sales/products/{product.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": product.id,
            "title": product.title,
        }
