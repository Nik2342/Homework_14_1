import pytest

from src.sub_main import Category, Product


@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_prod(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


@pytest.fixture
def category_tv():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником",
        ['55" QLED 4K', "Фоновая подсветка", 123000.0, 7],
    )


def test_init_cat(category_tv):
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    assert category_tv.products == ['55" QLED 4K', "Фоновая подсветка", 123000.0, 7]

    assert Category.category_count == 1
    assert Category.product_count == 4
