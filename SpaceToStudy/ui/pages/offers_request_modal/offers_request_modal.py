from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.pages.base_page import BasePage


FIRST_BLOCK_OF_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]")
NUMBER_OF_BLOCK = (By.XPATH, "//span[contains(@class, 'css-1sckc2u')]")
NAME_OF_BLOCK = (By.XPATH, "//span[contains(@class, 'css-gk4zgh')]")
CATEGORY_INPUT = (By.XPATH, f"{FIRST_BLOCK_OF_MODAL}/div[2]/div[1]/div[1]/div")
SUBJECT_INPUT = (By.XPATH, f"{FIRST_BLOCK_OF_MODAL}/div[2]/div[1]/div[2]/div")
CHECKBOX_LEVELS = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]/div[2]/div[2]/div")
TITLE_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/div[2]/div[1]/div/div")
DESCRIBE_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/div[2]/div[2]/div/div")
MODAL_NAME = (By.XPATH, "//*[contains(@class, 'MuiTypography-body1 css-xszkll')]")
MODAL_DESC = (By.XPATH, "//*/form[contains(@class, 'css-ggry99')]/p[contains(@class, 'css-1cuyrn')]")
CLOSE_BTN = (By.XPATH, "//*/button[contains(@class, 'css-13de6kf')]")
CREATE_OFFER_BTN = (By.XPATH, "//*/button[contains(@class, 'css-mfmxa4')]")
ADD_TO_DRAFT_BTN = (By.XPATH, "//*/button[contains(@class, 'css-4gyf81')]")


class OffersRequestModal(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self.node = None
        self._number_of_block = None
        self._name_of_block = None
        self._title_input = None
        self._describe_input = None

    def get_title_input(self) -> Textarea:
        node = self.driver.find_element(*TITLE_INPUT)
        self._title_input = Textarea(node)
        return self._title_input

    def get_describe_input(self) -> Textarea:
        node = self.driver.find_element(*DESCRIBE_INPUT)
        self._describe_input = Textarea(node)
        return self._describe_input

    def get_modal_name(self) -> str:
        return self.driver.find_element(*MODAL_NAME).text

    def get_modal_desc(self) -> str:
        return self.driver.find_element(*MODAL_DESC).text

    def get_close_btn(self) -> WebElement:
        return self.driver.find_element(*CLOSE_BTN)

    def get_add_to_draft_btn(self) -> WebElement:
        return self.driver.find_element(*ADD_TO_DRAFT_BTN)

    def get_create_offer_btn(self) -> WebElement:
        return self.driver.find_element(*CREATE_OFFER_BTN)

    def click_close_btn(self):
        self.get_close_btn().click()

    def click_add_to_draft_btn(self):
        self.get_add_to_draft_btn().click()

    def click_create_offer_btn(self):
        self.get_create_offer_btn().click()

    def get_number_of_block(self, node):
        if not self._number_of_block:
            self.node = node
            self._number_of_block = self.node.find_element(*NUMBER_OF_BLOCK).text
        return self._number_of_block

    def get_name_of_block(self, node):
        if not self._name_of_block:
            self.node = node
            self._name_of_block = self.node.find_element(*NAME_OF_BLOCK).text
        return self._name_of_block


class FirstBlock(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self._block_name = None
        self._category_input = None
        self._subject_input = None
        self._checkbox_levels = None

    def get_category_input(self) -> Input:
        node = self.driver.find_element(*CATEGORY_INPUT)
        self._category_input = Input(node)
        return self._category_input

    def get_subject_input(self) -> Input:
        node = self.driver.find_element(*SUBJECT_INPUT)
        self._subject_input = Input(node)
        return self._subject_input
