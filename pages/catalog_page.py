from pages.base_page import BasePage



class CatalogPage(BasePage):

    PAGE_PRODUCT_ID = "#mz-product-grid-image-28-212408"
    PRICE_CLASS = ".price-new"
    PRODUCT_CARD = ".carousel-item"
    PRODUCT_ID = "#entry_216815"

    def open_laptops_and_notebooks(self):
        """Открыть вкладку ноутбуков"""

        self.navigate_to("/index.php?route=product/category&path=18")


    def is_laptops_and_notebooks_visible(self):
        """Проверить наличие товаров на странице"""

        self.page.wait_for_selector(self.PAGE_PRODUCT_ID)
        return self.page.is_visible(self.PAGE_PRODUCT_ID)


    def return_price(self):
        """получить цену товара"""

        self.page.wait_for_selector(self.PRICE_CLASS)
        return self.page.locator(self.PRICE_CLASS).first.inner_text()


    def open_product_page(self):
        """открыть карточку товара"""

        self.page.wait_for_selector(self.PRODUCT_CARD)
        self.page.locator(self.PRODUCT_CARD).first.click()


    def is_product_page_visible(self):
        """проверить отображается ли карточка товара 
        по которой кликнул пользователь"""

        self.page.wait_for_selector(self.PRODUCT_ID)
        return self.page.is_visible(self.PRODUCT_ID)