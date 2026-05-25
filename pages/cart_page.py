from pages.base_page import BasePage

class CartPage(BasePage):

    MESSAGE_ID = "#content > p:nth-child(3)"
    PRODUCTS_ID = "#checkout-cart"
    CART_URL = "/index.php?route=checkout/cart"

    def open_cart(self):
        """открыть страницу корзины"""

        self.navigate_to(self.CART_URL)


    def check_message(self) -> bool:
        """Сообщение "Your shopping cart is empty!" """

        return self.page.locator(self.MESSAGE_ID).is_visible()


    def is_the_item_in_the_cart(self) -> bool:
        """проверить есть ли что-то в корзине"""

        return self.page.locator(self.PRODUCTS_ID).is_visible()
    

    def cart_sum_is_visible(self) -> bool:
        """проверить что сумма товаров отображается"""

        return self.page.get_by_role("columnheader", name="Total").is_visible()


    def get_total_price(self) -> str:
        """посмотреть итоговую стоимость товаров в корзине"""

        return self.page.locator("#content").get_by_role("strong").filter(has_text="$").first.inner_text()


    def remove_product(self):
        """удалить товар из корзины"""

        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("button", description="Remove", exact=True).click()
        self.page.wait_for_selector(self.MESSAGE_ID)