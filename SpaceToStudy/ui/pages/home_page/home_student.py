import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent
from SpaceToStudy.ui.pages.home_page.how_it_works_component_student import HowItWorksComponentStudent
from SpaceToStudy.ui.pages.home_page.questions_component import QuestionsComponent
from SpaceToStudy.ui.pages.home_page.search_tutor_input_component import SearchTutorComponent
from SpaceToStudy.ui.pages.subjects.subjects_page import SubjectsPage

CATEGORY_MUSIC = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[1]")
CATEGORY_COMPUTER = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[2]")
CATEGORY_DESIGN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[3]")
CATEGORY_DANCE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[4]")
CATEGORY_MATH = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[5]")
CATEGORY_LANGUAGES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a[6]")
CATEGORIES_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div")
CATEGORIES_BLOCK_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/p")
CATEGORIES_BLOCK_DESCRIPTION = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/span")
CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
CATEGORIES_MOBILE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div/a")

BUTTON_GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
HEADER_LINK_CATEGORIES = (By.XPATH, "//a[contains(text(), 'Categories')]")
BUTTON_FIND_TUTOR = (By.XPATH, "//a[contains(text(), 'Find tutor')]")
SEARCH_INPUT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div")
HOW_IT_WORKS_BLOCK_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]")
IMG_SEARCH_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/img")
QUESTIONS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]/div[1]")
QUESTIONS_ITEMS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]/div[2]/div")
ACCOUNT_BUTTON = (By.XPATH, "//button[@aria-label='Account']")
MY_PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, 'profile')]")


class HomePageStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._categories = None
        self._button_go_to_categories = None
        self._header_link_categories = None
        self._button_find_tutor = None
        self._questions_block = None
        self._questions_items = None
        self._search_tutor = None
        self._img_search_block = None
        self._how_it_works_block_student = None
        self._categories_block_title = None
        self._categories_block_description = None
        self._categories_block = None
        self._categories_mobile = None
        self._account_button = None
        self._my_profile_button = None

    @allure.step("Get categories")
    def get_categories(self) -> tuple[CategoryComponent]:
        if self._categories is None:
            categories = self.driver.find_elements(*CATEGORIES)
            self._categories = []
            for category in categories:
                self._categories.append(CategoryComponent(category))
        return self._categories

    @allure.step("Get categories mobile version site")
    def get_categories_mobile(self) -> tuple[CategoryComponent]:
        if self._categories_mobile is None:

            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located(CATEGORIES_MOBILE))
            categories_mobile = self.driver.find_elements(*CATEGORIES_MOBILE)
            self._categories_mobile = []
            for category in categories_mobile:
                self._categories_mobile.append(CategoryComponent(category))
        return self._categories_mobile

    @allure.step("Get categories block")
    def get_categories_block(self) -> WebElement:
        if not self._categories_block:
            self._categories_block = self.driver.find_element(*CATEGORIES_BLOCK)
        return self._categories_block

    @allure.step("Get My Profile button")
    def get_My_profile_button(self) -> WebElement:
        if not self._my_profile_button:
            self._my_profile_button = self.driver.find_element(*MY_PROFILE_BUTTON)
        return self._my_profile_button

    @allure.step("Get categories header link")
    def get_categories_header_link(self) -> WebElement:
        if not self._header_link_categories:
            self._header_link_categories = self.driver.find_element(*HEADER_LINK_CATEGORIES)
        return self._header_link_categories

    @allure.step("Get Account button")
    def get_account_button(self) -> WebElement:
        if not self._account_button:
            self._account_button = self.driver.find_element(*ACCOUNT_BUTTON)
        return self._account_button

    @allure.step("Get value css categories block")
    def get_gap_value_css_property_categories_block(self):
        value = self.get_categories_block().value_of_css_property("gap")
        gap = value.replace("px", "")
        gap_int = (int(gap))
        return gap_int

    @allure.step("Get title categories block")
    def get_title_categories_block(self) -> str:
        if not self._categories_block_title:
            self._categories_block_title = self.driver.find_element(*CATEGORIES_BLOCK_TITLE)
        return self._categories_block_title.text

    @allure.step("Get description categories block")
    def get_description_categories_block(self) -> str:
        if not self._categories_block_description:
            self._categories_block_description = self.driver.find_element(*CATEGORIES_BLOCK_DESCRIPTION)
        return self._categories_block_description.text

    @allure.step("Click category element by the {index} index")
    def click_category_el(self, index: int):
        self.get_categories()[index].click()
        return SubjectsPage(self.driver)

    @allure.step("Get search input")
    def get_search_input(self) -> SearchTutorComponent:
        if not self._search_tutor:
            _search_tutor = self.driver.find_element(*SEARCH_INPUT_BLOCK)
            self._search_tutor = SearchTutorComponent(_search_tutor)
        return self._search_tutor

    @allure.step("Get button \"go to categories\"")
    def get_button_go_to_categories(self) -> WebElement:
        if not self._button_go_to_categories:
            self._button_go_to_categories = self.driver.find_element(*BUTTON_GO_TO_CATEGORIES)
        return self._button_go_to_categories

    @allure.step("Get text button \"go to categories\"")
    def get_text_button_go_to_categories(self) -> str:
        return self.get_button_go_to_categories().text

    @allure.step("Click button \"go to categories\"")
    def click_button_go_to_categories(self):
        self.get_button_go_to_categories().click()
        return CategoriesPage(self.driver)

    def get_header_link_categories(self) -> WebElement:
        if not self._header_link_categories:
            self._header_link_categories = self.driver.find_element(*HEADER_LINK_CATEGORIES)
        return self._header_link_categories

    @allure.step("Click header link \"Categories\"")
    def click_header_link_categories(self):
        self.get_header_link_categories().click()
        return CategoriesPage(self.driver)

    @allure.step("Click Account button")
    def click_account_button(self):
        self.get_account_button().click()
        return HomePageStudent(self.driver)

    @allure.step("Get button \"find tutor\"")
    def get_button_find_tutor(self) -> WebElement:
        if not self._button_find_tutor:
            self._button_find_tutor = self.driver.find_element(*BUTTON_FIND_TUTOR)
        return self._button_find_tutor

    @allure.step("Get text button \"find tutor\"")
    def get_text_button_find_tutor(self) -> str:
        return self.get_button_find_tutor().text

    @allure.step("Click button \"find tutor\"")
    def click_button_find_tutor(self) -> ExploreOffersPage:
        self.get_button_find_tutor().click()
        return ExploreOffersPage(self.driver)

    @allure.step("Get questions block")
    def get_questions_block(self) -> QuestionsComponent:
        if not self._questions_block:
            _questions_block = self.driver.find_element(*QUESTIONS_BLOCK)
            self._questions_block = QuestionsComponent(_questions_block)
        return self._questions_block

    @allure.step("Get questions items")
    def get_questions_items(self) -> list[QuestionsComponent]:
        if self._questions_items is None:
            _questions_items = self.driver.find_elements(*QUESTIONS_ITEMS)
            self._questions_items = []
            for questions_item in _questions_items:
                self._questions_items.append(QuestionsComponent(questions_item))
        return self._questions_items

    @allure.step("Get image search block")
    def get_img_search_block(self) -> WebElement:
        if not self._img_search_block:
            self._img_search_block = self.driver.find_element(*IMG_SEARCH_BLOCK)
        return self._img_search_block

    @allure.step("Get how it works block in student page")
    def get_how_it_works_block_student(self) -> HowItWorksComponentStudent:
        if not self._how_it_works_block_student:
            _how_it_works_block_student = self.driver.find_element(*HOW_IT_WORKS_BLOCK_STUDENT)
            self._how_it_works_block_student = HowItWorksComponentStudent(_how_it_works_block_student)
        return self._how_it_works_block_student
