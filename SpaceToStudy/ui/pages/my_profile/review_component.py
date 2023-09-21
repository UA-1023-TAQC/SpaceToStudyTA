import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

USER_NICKNAME_LINK = (By.XPATH, "./div[1]/div/a")
AVATAR = (By.XPATH, ".//*[local-name()='svg']")
USER_NICKNAME = (By.XPATH, "./div[1]/div/a/p")
DATE = (By.XPATH, "./div[1]/div/p")
DIRECTION_AND_LEVEL = (By.XPATH, "./div[2]/p[1]")
STARS_COMPONENT = (By.XPATH, "./div[2]/div")
COMMENT_TEXT = (By.XPATH, "./div[2]/p[2]")


class ReviewComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.node = node

    @allure.step("Get the avatar of commenting user in ReviewComponent on 'My Profile' page")
    def get_comment_user_avatar(self) -> WebElement:
        return self.node.find_element(*AVATAR)

    @allure.step("Click the avatar of commenting user in ReviewComponent on 'My Profile' page")
    def click_comment_user_avatar(self):
        self.get_comment_user_avatar().click()

    @allure.step("Get the nickname text of commenting user in ReviewComponent on 'My Profile' page")
    def get_comment_user_nickname_text(self) -> str:
        return self.node.find_element(*USER_NICKNAME).text

    @allure.step("Click the nickname of commenting user in ReviewComponent on 'My Profile' page")
    def click_comment_user_nickname(self):
        self.node.find_element(*USER_NICKNAME_LINK).click()

    @allure.step("Get the date when the user commented in ReviewComponent on 'My Profile' page")
    def get_comment_user_date_text(self) -> str:
        return self.node.find_element(*DATE).text

    @allure.step("Get the direction and level where the user commented in ReviewComponent on 'My Profile' page")
    def get_comment_direction_and_level_text(self) -> str:
        return self.node.find_element(*DIRECTION_AND_LEVEL).text

    @allure.step("Get the text of user's comment in ReviewComponent on 'My Profile' page")
    def get_comment_text(self) -> str:
        return self.node.find_element(*COMMENT_TEXT).text

    @allure.step("Get the RatingStars component assigned by user who commented in ReviewComponent on 'My Profile' page")
    def get_comment_stars_rating_component(self) -> WebElement:
        return self.node.find_element(*STARS_COMPONENT)
