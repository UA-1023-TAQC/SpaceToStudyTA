import allure
from selenium.webdriver.common.by import By
from SpaceToStudy.ui.pages.base_component import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

QUESTION_BTN = (By.XPATH, "./div")
QUESTION = (By.XPATH, "./div/div/p")
ANSWER = (By.XPATH, "./div[2]//p")

class QuestionComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._question = None
        self._answer = None

    @allure.step("Get question text in 'Frequently asked question' component on offer details page")
    def get_question_text(self) -> str:
        if not self._question:
            self._question = self.node.find_element(*QUESTION)
        return self._question.text

    @allure.step("Click on button to open question in 'Frequently asked question' component on offer details page")
    def click_question_btn(self):
        self.node.find_element(*QUESTION_BTN).click()
        return self

    @allure.step("Get answer text in 'Frequently asked question' component on offer details page")
    def get_answer(self) -> str:
        if not self._answer:
            WebDriverWait(self.node, 10).until(EC.visibility_of_element_located(ANSWER))
            self._answer = self.node.find_element(*ANSWER)
        return self._answer.text