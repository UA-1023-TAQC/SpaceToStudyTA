from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

NAME_QUESTIONS_BLOCK = (By.XPATH, "./p")
DESCRIPTION_QUESTIONS_BLOCK = (By.XPATH, "./span")
HOW_TO_FIND_A_TUTOR_ITEM_TITLE = (By.XPATH, "./div[1]/div[1]/h6")
HOW_TO_FIND_A_TUTOR_ITEM_DESCRIPTION = (By.XPATH, "./div[2]/div/div/div/div/p")


class QuestionsComponent(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_questions_block = None
        self._description_questions_block = None
        self._description_items = None
        self._title_items = None

    def get_name_questions_block(self) -> str:
        if not self._name_questions_block:
            self._name_questions_block = self.node.find_element(*NAME_QUESTIONS_BLOCK)
        return self._name_questions_block.text

    def get_description_questions_block(self) -> str:
        if not self._description_questions_block:
            self._description_questions_block = self.node.find_element(*DESCRIPTION_QUESTIONS_BLOCK)
        return self._description_questions_block.text

    def get_title_items(self) -> WebElement:
        if not self._title_items:
            self._title_items = self.node.find_element(*HOW_TO_FIND_A_TUTOR_ITEM_TITLE)
        return self._title_items

    def get_text_title_items(self) -> str:
        return self.get_title_items().text

    def click_title_items(self):
        return self.get_title_items().click()

    def get_description_items(self) -> str:
        if not self._description_items:
            self._description_items = self.node.find_element(*HOW_TO_FIND_A_TUTOR_ITEM_DESCRIPTION)
        return self._description_items.text
