from pages.base_page import BasePage

class AuthorizationPage(BasePage):

    INPUT_EMAIL_ID = "#input-email"
    INPUT_PASSWORD_ID = "#input-password"
    AUTORIZATION_RESULT_CLASS = ".alert-dismissible"

    def open_profile_page(self):
        """открыть страницу профиля"""

        self.navigate_to("/index.php?route=account/login")


    def email_input_field_is_visible(self) -> bool:
        """проверить отображается ли поле для ввода почты"""

        self.page.wait_for_selector(self.INPUT_EMAIL_ID)
        return self.page.locator(self.INPUT_EMAIL_ID).is_visible()


    def password_input_field_is_visible(self) -> bool:
        """проверить отображается ли поле для ввода пароля"""

        self.page.wait_for_selector(self.INPUT_PASSWORD_ID)
        return self.page.locator(self.INPUT_PASSWORD_ID).is_visible()


    def enter_email(self, email: str ="example@example.com"):
        """ввести почту"""

        self.page.wait_for_selector(self.INPUT_EMAIL_ID)
        self.page.locator(self.INPUT_EMAIL_ID).fill(email)


    def enter_password(self, password: str ='password123'):
        """ввести пароль"""

        self.page.wait_for_selector(self.INPUT_PASSWORD_ID)
        self.page.locator(self.INPUT_PASSWORD_ID).fill(password)


    def confirm_account_details(self):
        """нажать кнопку Login"""

        self.page.get_by_role("button", name="Login").click()


    def authorization_result(self) -> str:
        """получить результат авторизации"""

        return self.page.locator(self.AUTORIZATION_RESULT_CLASS).inner_text()
    
