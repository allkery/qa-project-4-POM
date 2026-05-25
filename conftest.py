import pytest

@pytest.fixture
def base_page(page):
    from pages.base_page import BasePage
    return BasePage(page)


@pytest.fixture
def home(base_page):
    base_page.navigate_to()
    return base_page


@pytest.fixture
def search(page):
    from pages.search_page import SearchPage
    return SearchPage(page)


@pytest.fixture
def catalog(page):
    from pages.catalog_page import CatalogPage
    return CatalogPage(page)


@pytest.fixture
def authorization(page):
    from pages.authorization_page import AuthorizationPage
    return AuthorizationPage(page)


@pytest.fixture
def product(page):
    from pages.product_page import ProductPage
    return ProductPage(page)


@pytest.fixture
def cart(page):
    from pages.cart_page import CartPage
    return CartPage(page)