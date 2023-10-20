import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from SpaceToStudy.ui.pages.base_component import BaseComponent

PERSON_ICON = (By.XPATH, './div/div[1]/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, './div/div[1]/div[1]/div/a/p')
ADD_TO_BOOKMARKS_BTN = (By.XPATH, './div/div[1]/button')
LANGUAGES = (By.XPATH, './div/div[1]/div[1]/div/div/p')
OFFER_TITLE = (By.XPATH, './div/div[1]/p')
SUBJECT_LABEL = (By.XPATH, './div/div[1]/div[2]/div[2]/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './div/div[1]/div[2]/div[2]/div[2]/span/p')

PRICE_VALUE = (By.XPATH, './div/div[2]/div[1]/div[1]/p')
PRICE_PERIOD = (By.XPATH, './div/div[2]/div[1]/div[1]/span')

STAR_ICON = (By.XPATH, './/*[@data-testid="star-icon"]')
RATING_VALUE = (By.XPATH, './/*[@data-testid="number-box"]/p')

REVIEWS_LINE = (By.XPATH, './div/div[2]/div[1]/div[2]/p')

VIEW_DETAILS_BTN = (By.XPATH, '//a[contains(text(), "View details")]')
SEND_MESSAGE_BTN = (By.XPATH, '//button[contains(text(), "Send message")]')


class GridCardComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get person's icon")
    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    @allure.step("Click on the person's icon")
    def click_person_icon(self):
        self.get_person_icon().click()

    @allure.step("Get person's name")
    def get_person_name(self):
        return self.node.find_element(*PERSON_NAME)

    def get_person_name_text(self) -> str:
        WebDriverWait(self.node, 10).until(EC.visibility_of_element_located(PERSON_NAME))
        return self.node.find_element(*PERSON_NAME).text

    @allure.step("Click on person's name")
    def click_person_name(self):
        self.get_person_name().click()

    @allure.step("Get add to bookmarks button")
    def get_add_to_bookmarks_btn(self):
        return self.node.find_element(*ADD_TO_BOOKMARKS_BTN)

    @allure.step("Click on the add to bookmarks button")
    def click_add_to_bookmarks_btn(self):
        self.get_add_to_bookmarks_btn().click()
        return self

    @allure.step("Get languages as a webElement")
    def get_languages_webelement(self) -> WebElement:
        return self.node.find_element(*LANGUAGES)

    @allure.step("Get languages as a text")
    def get_languages(self) -> str:
        return self.node.find_element(*LANGUAGES).text

    @allure.step("Get offer title as a text")
    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    @allure.step("Get subject label as a webElement")
    def get_subject_label_webelement(self) -> WebElement:
        return self.node.find_element(*SUBJECT_LABEL)

    @allure.step("Get subject label as a text")
    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    @allure.step("Get level label as a webElement")
    def get_level_label_webelement(self) -> WebElement:
        return self.node.find_element(*LEVEL_LABEL)

    @allure.step("Get level label as a text")
    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    @allure.step("Get price value as webElement")
    def get_price_value_webelement(self) -> WebElement:
        return self.node.find_element(*PRICE_VALUE)

    @allure.step("Get price value")
    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text

    @allure.step("Get period for price as a text")
    def get_period_for_price(self) -> str:
        return self.node.find_element(*PRICE_PERIOD).text

    @allure.step("Get star icon")
    def get_star_icon(self) -> WebElement:
        return self.node.find_element(*STAR_ICON)

    @allure.step("Get rating value as a webElement")
    def get_rating_webelement(self) -> WebElement:
        return self.node.find_element(*RATING_VALUE)

    @allure.step("Get rating value as a text")
    def get_rating_value(self) -> str:
        return self.node.find_element(*RATING_VALUE).text

    @allure.step("Get reviews as a webElement")
    def get_reviews_webelement(self) -> WebElement:
        return self.node.find_element(*REVIEWS_LINE)

    @allure.step("Get reviews line as a text")
    def get_reviews_line(self) -> str:
        return self.node.find_element(*REVIEWS_LINE).text

    @allure.step("Get view details button")
    def get_view_details_btn(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN)

    @allure.step("Click on the view details button")
    def click_view_details_btn(self):
        from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
        self.get_view_details_btn().click()
        return OfferDetailsPage(self.node)

    @allure.step("Get send message button")
    def get_send_message_btn(self) -> WebElement:
        return self.node.find_element(*SEND_MESSAGE_BTN)

    @allure.step("Click on the send message button")
    def click_send_message_btn(self):
        self.get_send_message_btn().click()
