import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.offer_details.question_component import QuestionComponent

TITLE = (By.XPATH, "./div/p")
QUESTIONS = (By.XPATH, "./div/div/div")


class FrequentlyAskedQuestions(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._questions = None

    @allure.step("Get the title of 'Frequently Asked Questions' component of OfferDetailsPage in tutor's account")
    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    @allure.step("Get the list of questions in 'Frequently Asked Questions' component of OfferDetailsPage \
                in tutor's account")
    def get_questions(self) -> list[QuestionComponent]:
        if not self._questions:
            question_set = self.node.find_elements(*QUESTIONS)
            self._questions = [QuestionComponent(question) for question in question_set]
        return self._questions
