from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

BLOCK_NAME = (By.XPATH, "./p")
FOUR_STEPS = (By.XPATH, "./span")

IMAGE_Student = (By.XPATH, "./img")
TITLE_Student = (By.XPATH, "/.p")
DESCRIPTION_Student = (By.XPATH, "./span")


class HowItWorksComponentStudent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._block_name_student = None
        self._four_steps = None
        self._image_student = None
        self._title_student = None
        self._description_student = None

    def get_block_name_student(self) -> str:
        if not self._block_name_student:
            self._block_name_student = self.node.find_element(*BLOCK_NAME)
        return self._block_name_student.text

    def get_four_steps(self) -> str:
        if not self._four_steps:
            self._four_steps = self.node.find_element(*FOUR_STEPS)
        return self._four_steps.text

    def get_image_student(self) -> WebElement:
        if not self._image_student:
            self._image_student = self.node.find_element(*IMAGE_Student)
        return self._image_student

    def get_name_student(self) -> str:
        if not self._title_student:
            self._title_student = self.node.find_element(*TITLE_Student)
        return self._title_student.text

    def get_description_student(self) -> str:
        if not self._description_student:
            self._description_student = self.node.find_element(*DESCRIPTION_Student)
        return self._description_student.text
