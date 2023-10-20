from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.filtering_and_sorting_component import FilteringAndSortingComponent
from SpaceToStudy.ui.pages.explore_offers.grid_card_component import GridCardComponent
from SpaceToStudy.ui.pages.explore_offers.inline_card_component import InlineCardComponent
from SpaceToStudy.ui.pages.explore_offers.search_by_tutor_name_component import SearchByTutorNameComponent
from SpaceToStudy.ui.pages.explore_offers.student_private_lesson_component import StudentPrivateLessonComponent

STUDENT_FOR_PRIVATE_LESSONS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]")

TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/p")
TEXT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/span")
BACK_TO_ALL_SUBJECT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/a")
LEFT_ARROW = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/a/svg")

SEARCH_BY_TUTOR_NAME_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div")

FILTERING_AND_SORTING_BLOCK = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[5]")

OFFER_AND_REQUEST_BLOCK = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[6]")

TITLE_POPULAR_CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[7]/div[1]/p")
POPULAR_CATEGORIES_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[7]/div[2]/div")
GO_TO_CATEGORIES_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[7]/div[2]/button")

SCROLL_UP_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[3]/button")
GRID_CARD = (By.XPATH, "//*[@data-testid='OfferContainer']/div[count(div/div)=2]")
INLINE_CARD = (By.XPATH, "//*[@data-testid='OfferContainer']/div[count(div/div)=3]")
NOTIFICATION_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[6]")


class ExploreOffersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._list_of_offers_inline_card = None
        self._list_of_offers_grid_card = None
        self._student_for_private_lessons_block = None
        self._search_by_tutor_name_block = None
        self._filtering_and_sorting_block = None
        # self._offer_and_request_block = None
        self._popular_categories_cards = None
        self._notification_block = None

    @allure.step("Get student for private lessons block")
    def get_student_for_private_lessons_block(self):
        node = self.driver.find_element(*STUDENT_FOR_PRIVATE_LESSONS_BLOCK)
        if not self._student_for_private_lessons_block:
            self._student_for_private_lessons_block = StudentPrivateLessonComponent(node)
            return self._student_for_private_lessons_block

    @allure.step("Get title")
    def get_title(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    @allure.step("Get title text")
    def get_title_text(self):
        return self.get_title().text

    @allure.step("Get subtitle ")
    def get_text(self) -> WebElement:
        return self.driver.find_element(*TEXT)

    @allure.step("Get back to all subject button")
    def get_back_to_all_subject(self) -> WebElement:
        return self.driver.find_element(*BACK_TO_ALL_SUBJECT)

    @allure.step("Get left arrow")
    def get_left_arrow(self) -> WebElement:
        return self.driver.find_element(*LEFT_ARROW)

    @allure.step("Get search by tutor name block")
    def get_search_by_tutor_name_block(self):
        node = self.driver.find_element(*SEARCH_BY_TUTOR_NAME_BLOCK)
        if not self._search_by_tutor_name_block:
            self._search_by_tutor_name_block = SearchByTutorNameComponent(node)
            return self._search_by_tutor_name_block

    @allure.step("Get filtering and sorting block")
    def get_filtering_and_sorting_block(self):
        node = self.driver.find_element(*FILTERING_AND_SORTING_BLOCK)
        if not self._filtering_and_sorting_block:
            self._filtering_and_sorting_block = FilteringAndSortingComponent(node)
            return self._filtering_and_sorting_block

    @allure.step("Get go to categories button")
    def get_go_to_categories_btn(self) -> WebElement:
        return self.driver.find_element(*GO_TO_CATEGORIES_BTN)

    @allure.step("Get scroll up button")
    def get_scroll_up_btn(self) -> WebElement:
        return self.driver.find_element(*SCROLL_UP_BTN)

    @allure.step("Click on the scroll up button")
    def click_scroll_up_btn(self):
        return self.get_scroll_up_btn().click()

    @allure.step("Click on the go to categories button")
    def click_go_to_categories_btn(self):
        return self.get_go_to_categories_btn().click()

    @allure.step("Click on the back to all subjects button")
    def click_back_to_all_subject(self):
        return self.get_back_to_all_subject().click()

    @allure.step("Get list of offers in grid card")
    def get_list_of_offers_grid_card(self) -> List[GridCardComponent]:
        offers = self.driver.find_elements(*GRID_CARD)
        self._list_of_offers_grid_card = [GridCardComponent(offer) for offer in offers]
        return self._list_of_offers_grid_card

    @allure.step("Get list of offers in inline card")
    def get_list_of_offers_inline_card(self) -> List[InlineCardComponent]:
        WebDriverWait(self.driver, 3)
        offers = self.driver.find_elements(*INLINE_CARD)
        self._list_of_offers_inline_card = [InlineCardComponent(offer) for offer in offers]
        return self._list_of_offers_inline_card

    @allure.step("Get notification lock with no results")
    def get_notification_block_with_no_results(self) -> FilteringAndSortingComponent:
        if not self._notification_block:
            _notification_block = self.driver.find_element(*NOTIFICATION_BLOCK)
            self._notification_block = FilteringAndSortingComponent(_notification_block)
        return self._notification_block
