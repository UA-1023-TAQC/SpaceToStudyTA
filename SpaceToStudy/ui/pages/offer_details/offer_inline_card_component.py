from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.explore_offers.inline_card_component import InlineCardComponent
from SpaceToStudy.ui.pages.offer_details.enroll_offer_modal import EnrollOfferModal

from time import sleep

ENROLL_OFFER_BTN = (By.XPATH, "//button[contains(text(), 'Enroll offer')]")
ENROLL_OFFER_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/form")


class OfferInlineCardComponent(InlineCardComponent):

    def __init__(self, node):
        super().__init__(node)
        self._enroll_offer_btn = None

    def get_enroll_offer_btn(self) -> WebElement:
        return self.node.find_element(*ENROLL_OFFER_BTN)

    def get_enroll_offer_btn_text(self) -> str:
        return self.node.find_element(*ENROLL_OFFER_BTN).text

    def click_enroll_offer_btn(self) -> EnrollOfferModal:
        self.get_enroll_offer_btn().click()
        node = self.node.find_element(*ENROLL_OFFER_MODAL)
        sleep(5)
        return EnrollOfferModal(node)
