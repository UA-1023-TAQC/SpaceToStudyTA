from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent

QUESTION_BTN = (By.XPATH, "./div")
QUESTION = (By.XPATH, "./div/div/p")
ANSWER = (By.XPATH, "./div[2]//p")

class QuestionComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._question = None
        self._answer = None

    def get_question_text(self) -> str:
        if not self._question:
            self._question = self.node.find_element(*QUESTION)
        return self._question.text

    def click_question_btn(self):
        self.node.find_element(*QUESTION_BTN).click()
        return self

    def get_answer(self) -> str:
        if not self._answer:
            self._answer = self.node.find_element(*ANSWER)
        return self._answer.text