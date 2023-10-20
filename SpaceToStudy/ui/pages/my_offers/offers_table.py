import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, "./td[1]")
SUBJECT = (By.XPATH, "./td[2]/div/div[1]/span/p")
SKILL_LEVEL = (By.XPATH, "./td[2]/div/div[2]/span/p")
PRICE = (By.XPATH, "./td[3]")
LAST_UPDATE = (By.XPATH, "./td[4]")
STATUS = (By.XPATH, "./td[5]/div/span/p/span[2]")


class OfferElements(BaseComponent):
    @allure.step("Get an Offer title for offer in the offers table on the My offers page")
    def get_offer_title(self) -> str:
        return self.node.find_element(*TITLE).text

    @allure.step("Get a Subject name for offer in the offers table on the My offers page")
    def get_offer_category_name(self) -> str:
        return self.node.find_element(*SUBJECT).text

    @allure.step("Get a Level of the skill for offer in the offers table on the My offers page")
    def get_offer_subject_name(self) -> str:
        return self.node.find_element(*SKILL_LEVEL).text

    @allure.step("Get an offer Price in the offers table on the My offers page")
    def get_offer_price(self) -> str:
        return self.node.find_element(*PRICE).text

    @allure.step("Get an offer Last update date in the offers table on the My offers page")
    def get_offer_last_update(self) -> str:
        return self.node.find_element(*LAST_UPDATE).text

    @allure.step("Get an offer Status in the offers table on the My offers page")
    def get_offer_status(self) -> str:
        return self.node.find_element(*STATUS).text
