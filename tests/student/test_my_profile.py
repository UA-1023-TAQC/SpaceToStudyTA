import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.my_profile.my_profile import MyProfile


class MyProfileTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://s2s-front-stage.azurewebsites.net/')

    def login(self, email, password):
        login_button = self.browser.find_element(By.XPATH, "/html/body/div/div/header/div/div/button[3]")
        login_button.click()
        sleep(2)
        input_email = self.browser.find_element(By.XPATH,
                                               "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]/div/input")
        input_email.send_keys(email)
        sleep(1)
        input_password = self.browser.find_element(By.XPATH,
                                               "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/input")
        input_password.send_keys(password)
        sleep(1)
        login_button_step2 =  self.browser.find_element(By.XPATH,
                                               "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
        login_button_step2.click()
        sleep(2)
        self.browser.get('https://s2s-front-stage.azurewebsites.net/my-profile')
        sleep(1)


    def test_name_surname(self):
        self.login("volodumur911@gmail.com", "6QmaEud>G;7L!Ry")
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        name_surname = profile_info.get_name_surname_text()
        self.assertEquals(name_surname, "Tester Toster")

    def test_days_at_space2study_text(self):
        self.login("volodumur911@gmail.com", "6QmaEud>G;7L!Ry")
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(5)
        days_at_space2study_text = profile_info.get_days_in_spase2study_text()
        self.assertEquals("1 day", days_at_space2study_text)