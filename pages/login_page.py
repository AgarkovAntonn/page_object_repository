from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert ("login" in self.current_url), "Wrong login-page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "There is no LoginForm on page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "There is no RegisterForm on page"