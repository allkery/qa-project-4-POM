from playwright.sync_api import Page

class BasePage:

    LOGO_ID = "#entry_217821"
    SEARCH_ID = "#search"
    CART_CLASS = ".cart"
    FEATURED_ID = "#entry_218399"


    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://ecommerce-playground.lambdatest.io"


    def navigate_to(self, path="/"):
        """открыть главную страницу"""

        self.page.goto(self.base_url + path)
        self.page.wait_for_load_state("networkidle")


    def get_current_url(self):
        """получить текущий URL"""

        return self.page.url


    def is_logo_visible(self):
        """проверить видимость логотипа"""

        return self.page.is_visible(self.LOGO_ID)


    def is_search_visible(self):
        """проверить видимость поля для поиска"""

        return self.page.is_visible(self.SEARCH_ID)
    

    def is_cart_visible(self):
        """проверить видимость корзины"""

        return self.page.is_visible(self.CART_CLASS)
    

    def is_featured_visible(self):
        """проверить видимость рекомендуемых товаров"""

        return self.page.is_visible(self.FEATURED_ID)
    