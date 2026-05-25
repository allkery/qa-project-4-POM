from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_RESULTS = ".product-thumb"
    MESSAGE_EMPTY_RESULT = "#entry_212469"

    def search(self, item):
        """Ввести запрос и нажать поиск"""

        self.navigate_to()
        self.page.get_by_role("textbox", name="Search For Products").fill(item)
        self.page.get_by_role("button", name="Search").click()

    def is_results_visible(self):
        """Проверить что результаты поиска отображаются"""

        self.page.wait_for_selector(self.SEARCH_RESULTS)
        return self.page.locator(self.SEARCH_RESULTS).count() > 0
    

    def is_empty_visible(self):
        """Сообщение об отсутствии результатов"""
        
        self.page.wait_for_selector(self.MESSAGE_EMPTY_RESULT)
        return self.page.is_visible(self.MESSAGE_EMPTY_RESULT)