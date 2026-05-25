from pages.base_page import BasePage

class ProductPage(BasePage):

    PRICE_CLASS = ".price-new"
    PRODUCT_TITLE_ID = "#entry_216816"
    PRODUCT_LINK = "/index.php?route=product/product&product_id=47"
    BTN_CART_ID = "#entry_216842"
    COUNT_CART_CLASS = ".cart-item-total"


    def open_product_card(self):
        """открыть карточку товара"""

        self.navigate_to(self.PRODUCT_LINK)


    def product_name_is_visible(self) -> bool:
        """проверить отображается ли название"""

        self.page.wait_for_selector(self.PRODUCT_TITLE_ID)
        return self.page.locator(self.PRODUCT_TITLE_ID).is_visible()
    

    def product_cost_is_visible(self) -> bool:
        """проверить отображается ли цена"""

        self.page.wait_for_selector(self.PRICE_CLASS)
        return self.page.get_by_role("heading", name="$").is_visible()
    

    def add_to_cart_button_is_visible(self) -> bool:
        """проверить видимость и активность кнопки добавления в корзину"""

        self.page.wait_for_selector(self.BTN_CART_ID)
        visible = self.page.locator(self.BTN_CART_ID).is_visible()
        active = self.page.locator(self.BTN_CART_ID).is_enabled()
        return visible and active
    

    def add_product_to_cart(self):
        """добавить товар в корзину"""

        self.page.wait_for_selector(self.BTN_CART_ID)
        self.page.get_by_role("button", name="Add to Cart").click()


    def return_cart_counter(self) -> str:
        """вернуть количество товаров в корзине"""

        self.page.wait_for_selector(self.COUNT_CART_CLASS)
        return self.page.locator(self.COUNT_CART_CLASS).first.inner_text()

    
