import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.explore_offers.student_private_lesson_component import StudentPrivateLessonComponent
from SpaceToStudy.ui.pages.offers_request_modal.offers_request_modal import OffersRequestModal

CREATE_REQUEST_MODAL = (By.XPATH, "/html/body/div[2]/div[3]")


class TutorPrivateLessonComponent(StudentPrivateLessonComponent):

    def __init__(self, node):
        super().__init__(node)

    @allure.step("Click on the create request button")
    def click_create_request_btn(self) -> OffersRequestModal:
        self.get_create_request_btn().click()
        return OffersRequestModal(self.node.find_element(*CREATE_REQUEST_MODAL))
