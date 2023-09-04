from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent

FOOTER_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/footer/div")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.footer_block = None
        self.header = None

    def get_footer_block(self):
        if not self.footer_block:
            self.footer_block = self.driver.find_element(*FOOTER_BLOCK)
        return self.footer_block

    def get_header(self) -> [HeaderAuthorizedComponent,
                             HeaderUnauthorizedComponent]:
        return HeaderUnauthorizedComponent(self.driver.find_element(By.XPATH, "//header"))

    def go_to_url(self, url):
        self.driver.get(url)
