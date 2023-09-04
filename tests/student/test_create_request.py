import unittest

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.offers_request_modal.offers_request_modal import OffersRequestModal, FirstBlock, SecondBlock, \
    ThirdBlock
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class CreateRequestTestCase(BaseTestRunner):

    def test_offer_details(self):
        (HeaderUnauthorizedComponent(self.driver).click_login_btn()
            .set_email(ValueProvider.get_student_email())
            .set_password(ValueProvider.get_student_password())
            .click_login_button())
        (HeaderAuthorizedComponent(self.driver)
            .get_navigate_links()[0]
            .click())
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create request')]").click()
        first_block = FirstBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[1]"))
        first_block.get_category_input().set_select("Music")
        first_block.get_subject_input().set_select("Guitar")
        first_block.get_checkbox_beginner().set_check()
        second_block = SecondBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]"))
        second_block.get_title_input().set_text("I'd like to become a guitar coach")
        second_block.get_describe_input().set_text("Prefer focus on standard")
        second_block.get_language_input().set_select("Ukrainian")
        second_block.get_price_input().set_text("700")
        third_block = ThirdBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[3]"))
        third_block.get_question_input().set_text("What staff do I need?")
        third_block.set_answer_input_text("You need a guitar")
        OffersRequestModal(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form")).click_add_to_draft_btn()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
