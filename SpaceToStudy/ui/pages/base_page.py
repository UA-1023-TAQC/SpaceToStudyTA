from selenium.webdriver.common.by import By

FOOTER_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/footer/div")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.footer_block = None

    def get_footer_block(self):
        if not self.footer_block:
            self.footer_block = self.driver.find_element(*FOOTER_BLOCK)
        return self.footer_block
