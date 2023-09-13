from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.filtering_and_sorting_component import FilteringAndSortingComponent
from SpaceToStudy.ui.pages.explore_offers.grid_card_component import GridCardComponent
from SpaceToStudy.ui.pages.explore_offers.inline_card_component import InlineCardComponent
# from SpaceToStudy.ui.pages.explore_offers.offer_and_request_component import OfferAndRequestComponent
from SpaceToStudy.ui.pages.explore_offers.search_by_tutor_name_component import SearchByTutorNameComponent
from SpaceToStudy.ui.pages.explore_offers.student_private_lesson_component import StudentPrivateLessonComponent
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent

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

    def get_student_for_private_lessons_block(self):
        node = self.driver.find_element(*STUDENT_FOR_PRIVATE_LESSONS_BLOCK)
        if not self._student_for_private_lessons_block:
            self._student_for_private_lessons_block = StudentPrivateLessonComponent(node)
            return self._student_for_private_lessons_block

    def get_title(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    def get_text(self) -> WebElement:
        return self.driver.find_element(*TEXT)

    def get_back_to_all_subject(self) -> WebElement:
        return self.driver.find_element(*BACK_TO_ALL_SUBJECT)

    def get_left_arrow(self) -> WebElement:
        return self.driver.find_element(*LEFT_ARROW)

    def get_search_by_tutor_name_block(self):
        node = self.driver.find_element(*SEARCH_BY_TUTOR_NAME_BLOCK)
        if not self._search_by_tutor_name_block:
            self._search_by_tutor_name_block = SearchByTutorNameComponent(node)
            return self._search_by_tutor_name_block

    def get_filtering_and_sorting_block(self):
        node = self.driver.find_element(*FILTERING_AND_SORTING_BLOCK)
        if not self._filtering_and_sorting_block:
            self._filtering_and_sorting_block = FilteringAndSortingComponent(node)
            return self._filtering_and_sorting_block

    # def get_offer_and_request_block(self) -> tuple[OfferAndRequestComponent]:
    #     if self._offer_and_request_block is None:
    #         navigate_links = self.driver.find_elements(*OFFER_AND_REQUEST_BLOCK)
    #         self._offer_and_request_block = []
    #         for element in navigate_links:
    #             self._offer_and_request_block.append(OfferAndRequestComponent(element))
    #     return self._offer_and_request_block

    def get_popular_categories_cards(self) -> tuple[CategoryComponent]:
        if self._popular_categories_cards is None:
            navigate_links = self.driver.find_elements(*OFFER_AND_REQUEST_BLOCK)
            self._popular_categories_cards = []
            for element in navigate_links:
                self._popular_categories_cards.append(CategoryComponent(element))
        return self._popular_categories_cards

    def get_go_to_categories_btn(self) -> WebElement:
        return self.driver.find_element(*GO_TO_CATEGORIES_BTN)

    def get_scroll_up_btn(self) -> WebElement:
        return self.driver.find_element(*SCROLL_UP_BTN)

    def click_scroll_up_btn(self):
        return self.get_scroll_up_btn().click()

    def click_go_to_categories_btn(self):
        return self.get_go_to_categories_btn().click()

    def click_back_to_all_subject(self):
        return self.get_back_to_all_subject().click()

    def get_list_of_offers_grid_card(self) -> list:
        offers = self.driver.find_elements(*GRID_CARD)
        self._list_of_offers_grid_card = [GridCardComponent(offer) for offer in offers]
        return self._list_of_offers_grid_card

    def get_list_of_offers_inline_card(self) -> list:
        offers = self.driver.find_elements(*INLINE_CARD)
        self._list_of_offers_grid_card = [InlineCardComponent(offer) for offer in offers]
        return self._list_of_offers_inline_card
