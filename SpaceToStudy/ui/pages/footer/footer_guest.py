from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage

FOOTER_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/footer/div")


class Footer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.footer_block = None


    def get_footer_block(self):
        if not self.footer_block:
            self.footer_block = self.driver.find_element(*FOOTER_BLOCK)
        return self.footer_block