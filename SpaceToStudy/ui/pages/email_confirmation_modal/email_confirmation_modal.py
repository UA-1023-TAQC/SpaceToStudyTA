from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal

IMAGE = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/img')
MESSAGE = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/div/p')
GO_TO_LOGIN_BUTTON = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button')
LOGIN_MODAL = (By.XPATH, '//div[@data-testid="popupContent"]')


class EmailConfirmationModal(BasePage):
    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    def get_message(self) -> str:
        return self.driver.find_element(*MESSAGE).text

    def get_go_to_login_button(self) -> WebElement:
        return self.driver.find_element(*GO_TO_LOGIN_BUTTON)

    def click_go_to_login_button(self):
        self.get_go_to_login_button().click()
        return LoginModal(self.driver.find_element(*LOGIN_MODAL))
