import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
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


if __name__ == '__main__':
    unittest.main(verbosity=2)
