# ========== Главная страница ==========


def test_main_page_loads_and_displays_logo(home):
    """Страница загружается, логотип отображается"""

    assert home.is_logo_visible()


def test_main_page_search_input_is_visible_in_header(home):
    """Поле поиска видно в шапке"""

    assert home.is_search_visible()


def test_main_page_cart_icon_is_visible_in_header(home):
    """Иконка корзины отображается"""

    assert home.is_cart_visible()


def test_main_page_featured_products_are_visible(home):
    """Карточки товаров видны"""

    assert home.is_featured_visible()


# ========== Поиск ==========


def test_search_by_valid_keyword_mac_displays_results(search):
    """Результаты поиска отображаются"""

    search.search("Mac")
    assert search.is_results_visible()
    

def test_search_nonexistent_product_shows_no_results_message(search):
    """Сообщение об отсутствии результатов показывается"""

    search.search("xyzxyzxyz")
    assert search.is_empty_visible()


def test_search_with_empty_query_keeps_page_or_shows_hint(search):
    """Поиск с пустой строкой — открывается страница поиска"""

    search.search("")
    assert "product%2Fsearch&search" in search.get_current_url()


# ========== Каталог и категории ==========


def test_catalog_laptops_category_displays_products(catalog):
    """Товары категории отображаются"""

    catalog.open_laptops_and_notebooks()
    assert catalog.is_laptops_and_notebooks_visible()


def test_catalog_every_product_has_price(catalog):
    """У каждой карточки есть цена"""

    catalog.open_laptops_and_notebooks()
    assert "$" in catalog.return_price()


def test_catalog_clicking_product_card_opens_product_page(catalog):
    """Открывается страница товара после клика по карточке"""

    catalog.open_laptops_and_notebooks()
    catalog.open_product_page()
    assert catalog.is_product_page_visible()


# ========== Страница товара ==========


def test_product_page_title_is_visible(product):
    """Заголовок страницы товара виден"""

    product.open_product_card()
    assert product.product_name_is_visible()


def test_product_page_price_is_visible(product):
    """Цена видна на странице"""

    product.open_product_card()
    assert product.product_cost_is_visible()


def test_product_page_add_to_cart_button_is_enabled(product):
    """Кнопка "Add to Cart" видна и активна"""

    product.open_product_card()
    assert product.add_to_cart_button_is_visible()


def test_product_page_adding_to_cart_updates_header_counter(product):
    """товар добавляется в корзину, счетчик обновляется"""

    product.open_product_card()
    product.add_product_to_cart()
    assert "1" in product.return_cart_counter()


# ========== Корзина ==========


def test_cart_empty_cart_shows_empty_message(cart):
    """Сообщение "Your shopping cart is empty!" 
    показывается когда товаров в корзине нету"""

    cart.open_cart()
    assert cart.check_message()


def test_cart_added_product_is_displayed_in_cart(cart, product):
    """Товар появляется в корзине после добавления"""

    product.open_product_card()
    product.add_product_to_cart()
    cart.open_cart()
    assert "1" in product.return_cart_counter()
    assert cart.is_the_item_in_the_cart()


def test_cart_displays_correct_non_zero_total_price(cart, product):
    """Сумма отображается и не равна $0.00 после добавления товара"""

    product.open_product_card()
    product.add_product_to_cart()
    cart.open_cart()
    assert int(cart.get_total_price()[1:-3]) > 0
    assert cart.cart_sum_is_visible()


def test_cart_removing_product_makes_cart_empty(cart, product, home):
    """Корзина становится пустой после удаления товара"""

    product.open_product_card()
    product.add_product_to_cart()
    home.navigate_to()
    cart.open_cart()
    assert cart.is_the_item_in_the_cart()

    cart.remove_product()
    assert cart.check_message()


# ========== Авторизация ==========


def test_auth_login_page_displays_form(authorization):
    """Форма входа отображается"""

    authorization.open_profile_page()
    assert authorization.password_input_field_is_visible()
    assert authorization.email_input_field_is_visible()


def test_auth_login_with_invalid_password_shows_error_message(authorization):
    """Сообщение об ошибке при входе с неверными данными"""

    authorization.open_profile_page()
    authorization.enter_email()
    authorization.enter_password()
    authorization.confirm_account_details()
    assert "Warning" in authorization.authorization_result()