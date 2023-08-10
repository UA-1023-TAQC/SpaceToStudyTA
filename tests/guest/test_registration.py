from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.home_page.home_page import HomePage
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal


class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://s2s-front-stage.azurewebsites.net/')

    def test_page_title(self):
        self.browser.get('https://s2s-front-stage.azurewebsites.net/')
        self.assertIn('Space2Study', self.browser.title)

    def test_open_sign_up_as_a_student_modal(self):
        login_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div/button[3]')
        login_btn.click()
        join_us_for_free_link = self.browser.find_element(By.XPATH,
                                                          '/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/div[3]/a')
        join_us_for_free_link.click()
        become_a_student = self.browser.find_element(By.XPATH, '//*[@id="what-сan-you-do"]/div[2]/div[1]/button')
        become_a_student.click()
        sign_up_as_a_student_modal = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div')
        self.assertTrue(sign_up_as_a_student_modal.is_enabled())
        self.assertIn('Sign up as a student', sign_up_as_a_student_modal.text)

    def test_open_login_modal(self):
        login_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div/button[3]')
        login_btn.click()
        time.sleep(2)
        login_modal = LoginModal(self.browser)
        email = login_modal.get_email_input()
        email.set_text("test+1@test.com")
        self.assertEquals(email.get_label_text(), "Email *")
        # self.assertEquals(email.get_error_message(), "Email should be of the following format: “local-part@domain.com")

    def test_homepage_categories(self):
        email, password = "login", "pass"
        login_button = self.browser.find_element(By.XPATH, "/html/body/div/div/header/div/div/button[3]")
        login_button.click()
        sleep(2)
        input_email = self.browser.find_element(By.XPATH,
                                                "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]/div/input")
        input_email.send_keys(email)
        input_password = self.browser.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/input")
        input_password.send_keys(password)
        login_button_step2 = self.browser.find_element(By.XPATH,
                                                       "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
        login_button_step2.click()
        sleep(2)

        # self.browser.get('https://s2s-front-stage.azurewebsites.net/tutor')
        first_category_name = HomePage(self.browser).get_categories()[0].get_name()
        self.assertEquals(first_category_name, "Music")



if __name__ == '__main__':
    unittest.main(verbosity=2)
