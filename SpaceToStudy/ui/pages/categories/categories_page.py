import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.categories.tutor_private_lesson_component import TutorPrivateLessonComponent
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage


CATEGORIES_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/p')
CATEGORIES_SUBTEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/span')
SHOW_ALL_OFFERS_BTN = (By.XPATH, '//a[text()="Show all offers"]')
SEARCH_BTN = (By.XPATH, '//button[text()="Search"]')
SEARCH_INPUT = (By.XPATH, '//input[contains(@role, "combobox")]/../..')
SEARCH_FIELD_HELP_TEXT = (By.XPATH, '//*[@id="mui-2488-label"]')
STUDENT_PRIVATE_LESSON_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]")
CARDS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]/div/a")

NO_RESULT_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/p")
CATEGORIES_BLOCK = (By.XPATH, '/html/body/div/div/div[2]/div[2]')
MUSIC_SUBJECTS = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/p')

class CategoriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._cards = None
        self._no_result_title = None
        self._categories_block = None
        self._music_subjects = None

    @allure.step("Get categories title text")
    def get_categories_title(self) -> str:
        return self.driver.find_element(*CATEGORIES_TITLE).text

    @allure.step("Get categories subtitle text")
    def get_categories_subtext(self) -> str:
        return self.driver.find_element(*CATEGORIES_SUBTEXT).text

    @allure.step("Get show all offers button")
    def get_show_all_offers_btn(self) -> WebElement:
        return self.driver.find_element(*SHOW_ALL_OFFERS_BTN)

    @allure.step("Click on the show all offers button")
    def click_show_all_offers_btn(self):
        self.get_show_all_offers_btn().click()
        return ExploreOffersPage(self.driver)

    @allure.step("Get search button")
    def get_search_btn(self) -> WebElement:
        return self.driver.find_element(*SEARCH_BTN)

    @allure.step("Click on the search button")
    def click_search_btn(self):
        self.get_search_btn().click()

    @allure.step("Get search input")
    def get_search_input(self) -> InputDropDownList:
        node = self.driver.find_element(*SEARCH_INPUT)
        return InputDropDownList(node)

    @allure.step("Get search field help text")
    def get_search_field_help_text(self) -> str:
        return self.driver.find_element(*SEARCH_FIELD_HELP_TEXT).text

    @allure.step("Get student private lesson component")
    def get_student_private_lesson_component(self) -> TutorPrivateLessonComponent:
        return TutorPrivateLessonComponent(self.driver.find_element(*STUDENT_PRIVATE_LESSON_COMPONENT))

    @allure.step("Get cards")
    def get_cards(self) -> list:
        from SpaceToStudy.ui.pages.categories.card_component import CardComponent
        if not self._cards:
            card_set = self.driver.find_elements(*CARDS)
            self._cards = [CardComponent(card) for card in card_set]
        return self._cards

    @allure.step("Get no result title")
    def get_no_result_title(self) -> str:
        if not self._no_result_title:
            self._no_result_title = self.driver.find_element(*NO_RESULT_TITLE)
        return self._no_result_title.text

    @allure.step("Get categories block")
    def get_categories_block(self) -> WebElement:
        if not self._categories_block:
            self._categories_block = self.driver.find_element(*CATEGORIES_BLOCK)
        return self._categories_block

    @allure.step("Get music subjects")
    def get_music_subjects(self):
        if self._music_subjects is None:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element(MUSIC_SUBJECTS, 'Music Subjects'))
            self._music_subjects = self.driver.find_element(*MUSIC_SUBJECTS).text
        return self._music_subjects