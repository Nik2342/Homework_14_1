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
def category_electronics():
    return Category("Телефоны", "Все телефоны")


def test_init_category(category_electronics):
    assert category_electronics.name == "Телефоны"
    assert category_electronics.description == "Все телефоны"
    assert len(category_electronics.products) == 0
    assert Category.category_count == 1


def test_add_product_to_category(category_electronics, product_samsung):
    category_electronics.add_product(product_samsung)
    assert len(category_electronics.products) == 1
    assert category_electronics.products[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert Category.product_count == 1


def test_products_in_category(category_electronics):
    product_iphone = Product("iPhone 14 Pro", "128GB, Золотой цвет", 150000.0, 3)
    category_electronics.add_product(product_samsung)
    category_electronics.add_product(product_iphone)
    assert Category.product_count == 3


def test_set_price(product_samsung):
    product_samsung.price = -100
    assert product_samsung.price == 180000.0
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0
