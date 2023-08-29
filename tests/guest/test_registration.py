import unittest
from time import sleep

from selenium.webdriver.common.by import By


from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from tests.test_runners import BaseTestRunner


class RegistrationTestCase(BaseTestRunner):


    def test_page_title(self):
        self.driver.get('https://s2s-front-stage.azurewebsites.net/')
        self.assertIn('Space2Study', self.driver.title)

    def test_open_sign_up_as_a_student_modal(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div/button[3]')
        login_btn.click()
        join_us_for_free_link = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/div[3]/a')
        join_us_for_free_link.click()
        become_a_student = self.driver.find_element(By.XPATH, '//*[@id="what-сan-you-do"]/div[2]/div[1]/button')
        become_a_student.click()
        sign_up_as_a_student_modal = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div')
        self.assertTrue(sign_up_as_a_student_modal.is_enabled())
        self.assertIn('Sign up as a student', sign_up_as_a_student_modal.text)

    def test_open_login_modal(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div/button[3]')
        login_btn.click()
        sleep(2)
        login_modal = LoginModal(self.driver)
        email = login_modal.get_email_input()
        email.set_text("test+1@test.com")
        self.assertEquals(email.get_label_text(), "Email *")
        # self.assertEquals(email.get_error_message(), "Email should be of the following format: “local-part@domain.com")

    def test_homepage_categories(self):
        email, password = "login", "pass"
        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/header/div/div/button[3]")
        login_button.click()
        sleep(2)
        input_email = self.driver.find_element(By.XPATH,
                                               "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]/div/input")
        input_email.send_keys(email)
        input_password = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/input")
        input_password.send_keys(password)
        login_button_step2 = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
        login_button_step2.click()
        sleep(2)

        # self.browser.get('https://s2s-front-stage.azurewebsites.net/tutor')
        first_category_name = HomePageStudent(self.driver).get_categories()[0].get_name()
        self.assertEquals(first_category_name, "Music")

    def test_collapse(self):
        home = HomePageGuest(self.driver)
        is_expanded = (home
                       .get_flexible_location()
                       .is_expanded())
        self.assertTrue(is_expanded)
        is_expanded = (home
                       .click_individual_time()
                       .get_individual_time()
                       .is_expanded())
        self.assertTrue(is_expanded)

    def test_registration_tutor_too_long_password(self):
        registration = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_tutor())
        registration.set_first_name("test")
        registration.set_last_name("test")
        registration.set_email("test@gmail.com")
        registration.set_password("11111111111111111111111111q")
        registration.click_sign_up_btn()
        message = (registration.get_password_error_message().get_error_message())
        self.assertEqual(message, "Password cannot be shorter than 8 and longer than 25 characters")


if __name__ == '__main__':
    unittest.main(verbosity=2)
