import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.offer_details.frequently_asked_questions import FrequentlyAskedQuestions
from SpaceToStudy.ui.pages.offer_details.general_info import GeneralInfoComponent
from SpaceToStudy.ui.pages.offer_details.offer_inline_card_component import OfferInlineCardComponent

TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div/div/p")
DESC = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div/div/span")
IMG = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/img")
OFFER_INLINE_CARD_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div")
ABOUT_OFFER_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/div/p")
ABOUT_OFFER_DESC = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/div/p")
GENERAL_INFO_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]")
FREQUENTLY_ASKED_QUESTIONS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]")
WHAT_STUDENTS_SAY_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[6]")
INLINE_CARD_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")

SUCCESS_FLASHBOX = (By.XPATH,
                    "//div[@role='alert']//div[contains(text(), 'Request for cooperation sent successfully')]")


class OfferDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._title = None
        self._desc = None
        self._img = None
        self._offer_inline_card_component = None
        self._about_offer_title = None
        self._about_offer_desc = None
        self._general_info_component = None
        self._frequently_asked_questions_component = None
        self._what_students_say_component = None
        self._enroll_offer_btn = None
        self._is_request_sent_successfully = None
        self._inline_card_component = None

    @allure.step("Get title of offer details page")
    def get_title(self) -> str:
        if not self._title:
            self._title = self.driver.find_element(*TITLE)
        return self._title.text

    @allure.step("Get description of offer details page")
    def get_desc(self) -> str:
        if not self._desc:
            self._desc = self.driver.find_element(*DESC)
        return self._desc.text

    @allure.step("Get image of offer details page")
    def get_img(self) -> WebElement:
        if not self._img:
            self._img = self.driver.find_element(*IMG)
        return self._img

    @allure.step("Get offer inline card on offer details page")
    def get_offer_inline_card_component(self) -> OfferInlineCardComponent:
        if not self._offer_inline_card_component:
            node = self.driver.find_element(*OFFER_INLINE_CARD_COMPONENT)
            self._offer_inline_card_component = OfferInlineCardComponent(node)
        return self._offer_inline_card_component

    @allure.step("Get title of 'About offer' component on offer details page")
    def get_about_offer_title(self) -> str:
        if not self._about_offer_title:
            self._about_offer_title = self.driver.find_element(*ABOUT_OFFER_TITLE)
        return self._about_offer_title

    @allure.step("Get description of 'About offer' component on offer details page")
    def get_about_offer_desc(self) -> str:
        if not self._about_offer_desc:
            self._about_offer_desc = self.driver.find_element(*ABOUT_OFFER_DESC)
        return self._about_offer_desc.text

    @allure.step("Get 'General information' component on offer details page")
    def get_general_info_component(self) -> GeneralInfoComponent:
        if not self._general_info_component:
            node = self.driver.find_element(*GENERAL_INFO_COMPONENT)
            self._general_info_component = GeneralInfoComponent(node)
        return self._general_info_component

    @allure.step("Get 'Frequently asked questions' component on offer details page")
    def get_frequently_asked_questions_component(self) -> FrequentlyAskedQuestions:
        if not self._frequently_asked_questions_component:
            node = self.driver.find_element(*FREQUENTLY_ASKED_QUESTIONS)
            self._frequently_asked_questions_component = FrequentlyAskedQuestions(node)
        return self._frequently_asked_questions_component

    @allure.step("Get 'What students say' component on offer details page")
    def get_what_students_say_component(self) -> WebElement:
        if not self._what_students_say_component:
            self._what_students_say_component = self.driver.find_element(*WHAT_STUDENTS_SAY_COMPONENT)
        return self._what_students_say_component

    @allure.step("Get inline card on offer details page")
    def get_inline_card_component(self) -> OfferInlineCardComponent:
        if not self._inline_card_component:
            node = self.driver.find_element(*INLINE_CARD_COMPONENT)
            self._inline_card_component = OfferInlineCardComponent(node)
        return self._inline_card_component

    @allure.step("Check that request was sent successfully on offer details page")
    def is_request_sent_successfully(self) -> bool:
        try:
            (WebDriverWait(self.driver, 10)
             .until(expected_conditions
                    .presence_of_element_located(SUCCESS_FLASHBOX)))
            return True
        except TimeoutException:
            return False
