from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent

FOOTER_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/footer/div")
PULSATE = (By.XPATH, "//span[@class='MuiTouchRipple-child MuiTouchRipple-childPulsate']")


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
        header_unauthorized_component = HeaderUnauthorizedComponent(self.driver.find_element(By.XPATH, "//header"))
        if header_unauthorized_component.is_login_button_present():
            return header_unauthorized_component
        else:
            return HeaderAuthorizedComponent(self.driver.find_element(By.XPATH, "//header"))

    def go_to_url(self, url):
        self.driver.get(url)

    def hover(self, hover_el):
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_el).perform()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(hover_el))
        return hover_el

    def set_size_window(self, width, height):
        self.driver.set_window_size(width, height)

    def get_tub_animation(self) -> bool:
        try:
            self.driver.find_element(*PULSATE)
            return True
        except NoSuchElementException:
            return False
