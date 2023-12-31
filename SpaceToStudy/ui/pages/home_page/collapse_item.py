import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE_COLLAPSE_ITEM = (By.XPATH, "./div[1]/div/h6")
DESCRIPTION_COLLAPSE_ITEM = (By.XPATH, ".//p")
TAB_ELEMENT = (By.XPATH, "./div[1]")


class CollapseItem(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    @allure.step("Get title element")
    def get_title(self) -> WebElement:
        return self.node.find_element(*TITLE_COLLAPSE_ITEM)

    @allure.step("Get title text")
    def get_title_text(self) -> str:
        return self.get_title().text

    @allure.step("Get description element")
    def get_description(self) -> WebElement:
        wait = WebDriverWait(self.node, 10)
        description = wait.until(EC.visibility_of_element_located(DESCRIPTION_COLLAPSE_ITEM))
        return description

    @allure.step("Get description text")
    def get_description_text(self) -> str:
        return self.get_description().text

    @allure.step("Get color of title")
    def get_color_of_title(self):
        return self.node.find_element(*TITLE_COLLAPSE_ITEM).value_of_css_property("color")

    @allure.step("Get value of css description")
    def get_description_value_of_css(self, value):
        return self.node.find_element(*DESCRIPTION_COLLAPSE_ITEM).value_of_css_property(value)

    @allure.step("Check if element is expanded")
    def is_expanded(self) -> bool:
        aria_expanded = self.node.find_element(By.XPATH, ".//div[@aria-expanded]").get_attribute("aria-expanded")
        return aria_expanded == "true"

    @allure.step("Click element")
    def click(self):
        self.node.click()

    @allure.step("Get background el with tab")
    def get_background_el_with_tab(self) -> WebElement:
        return self.node.find_element(*TAB_ELEMENT)
