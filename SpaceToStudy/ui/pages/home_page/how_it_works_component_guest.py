import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

BLOCK_NAME = (By.XPATH, "./p")
CHECKBOX_LEARN_FROM_EXPERTS = (By.XPATH, "./div[1]/h6[1]")
CHECKBOX_SHARE_YOUR_EXPERIENCE = (By.XPATH, "./div[1]/h6[2]")
IMAGE = (By.XPATH, "./div[2]/img[1]")
TITLE = (By.XPATH, "./div[3]/p")
DESCRIPTION = (By.XPATH, "./div[3]/span")


class HowItWorksComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.block_name = None
        self.checkbox_learn_from_experts = None
        self.checkbox_share_your_experience = None
        self.image = None
        self.title = None
        self.description = None

    @allure.step("Get text from the block name")
    def get_block_name(self) -> str:
        if not self.block_name:
            self.block_name = self.node.find_element(*CHECKBOX_LEARN_FROM_EXPERTS)
        return self.block_name.text

    @allure.step("Get the 'Learn from Experts' checkbox")
    def get_checkbox_learn_from_experts(self) -> WebElement:
        if not self.checkbox_learn_from_experts:
            self.checkbox_learn_from_experts = self.node.find_element(*CHECKBOX_LEARN_FROM_EXPERTS)
        return self.checkbox_learn_from_experts

    @allure.step("Get the text of 'Learn from Experts' checkbox")
    def get_text_checkbox_learn_from_experts(self) -> str:
        return self.get_checkbox_learn_from_experts().text

    @allure.step("Get the 'Share Your Experience' checkbox")
    def get_checkbox_share_your_experience(self) -> WebElement:
        if not self.checkbox_share_your_experience:
            self.checkbox_share_your_experience = self.node.find_element(*CHECKBOX_SHARE_YOUR_EXPERIENCE)
        return self.checkbox_share_your_experience

    @allure.step("Get the text of 'Share Your Experience' checkbox")
    def get_text_checkbox_share_your_experience(self) -> str:
        return self.get_checkbox_learn_from_experts().text

    @allure.step("Get the image")
    def get_image(self) -> WebElement:
        if not self.image:
            self.image = self.node.find_element(*IMAGE)
        return self.image

    @allure.step("Get the name")
    def get_name(self) -> str:
        if not self.title:
            self.title = self.node.find_element(*TITLE)
        return self.title.text

    @allure.step("Get the name WebElement")
    def get_name_web_element(self) -> WebElement:
        if not self.title:
            self.title = self.node.find_element(*TITLE)
        return self.title

    @allure.step("Get the description")
    def get_description(self) -> str:
        if not self.description:
            self.description = self.node.find_element(*DESCRIPTION)
        return self.description.text

    @allure.step("Get the description WebElement")
    def get_description_web_element(self) -> WebElement:
        if not self.description:
            self.description = self.node.find_element(*DESCRIPTION)
        return self.description

    @allure.step("Check if 'How It Works' block is displayed")
    def is_displayed_how_it_works_block(self) -> bool:
        return self.node.is_displayed()

    @allure.step("Get web element")
    def get_web_element(self) -> WebElement:
        return self.node
