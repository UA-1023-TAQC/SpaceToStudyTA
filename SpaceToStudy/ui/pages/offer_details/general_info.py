from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.offer_details.info_component_many_values import InfoComponentManyValues
from SpaceToStudy.ui.pages.offer_details.info_component_one_value import InfoComponentOneValue

TITLE = (By.XPATH, "./div/p")
TUTORING_SUBJECT_COMPONENT = (By.XPATH, "./div/div/div[1]/div")
PREPARATION_LEVELS_COMPONENT = (By.XPATH, "./div/div/div[2]/div")
TUTORING_LANGUAGE_COMPONENT = (By.XPATH, "./div/div/div[3]/div")
PRICING_COMPONENT = (By.XPATH, "./div/div/div[4]/div")


class GeneralInfoComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._tutoring_subject_component = None
        self._preparing_levels_component = None
        self._tutoring_language_component = None
        self._pricing_component = None

    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    def get_tutoring_subject_component(self) -> InfoComponentOneValue:
        if not self._tutoring_subject_component:
            node = self.node.find_element(*TUTORING_SUBJECT_COMPONENT)
            self._tutoring_subject_component = InfoComponentOneValue(node)
        return self._tutoring_subject_component

    def get_preparation_levels_component(self) -> InfoComponentManyValues:
        if not self._preparing_levels_component:
            node = self.node.find_element(*PREPARATION_LEVELS_COMPONENT)
            self._preparing_levels_component = InfoComponentManyValues(node)
        return self._preparing_levels_component

    def get_tutoring_languages_component(self) -> InfoComponentManyValues:
        if not self._tutoring_language_component:
            node = self.node.find_element(*TUTORING_LANGUAGE_COMPONENT)
            self._tutoring_language_component = InfoComponentManyValues(node)
        return self._tutoring_language_component

    def get_pricing_component(self) -> InfoComponentOneValue:
        if not self._pricing_component:
            node = self.node.find_element(*PRICING_COMPONENT)
            self._pricing_component = InfoComponentOneValue(node)
        return self._pricing_component
