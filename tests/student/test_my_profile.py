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
        self.login("volodumur911@gmail.com", "6QmaEud>G;7L!Ry")

    def login(self, email, password):
        login_button = self.browser.find_element(By.XPATH, "/html/body/div/div/header/div/div/button[3]")
        login_button.click()
        sleep(2)
        input_email = self.browser.find_element(By.XPATH,
                                                "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]/div/input")
        input_email.send_keys(email)
        sleep(2)
        input_password = self.browser.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/input")
        input_password.send_keys(password)
        sleep(2)
        login_button_step2 = self.browser.find_element(By.XPATH,
                                                       "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
        login_button_step2.click()
        sleep(2)
        self.browser.get('https://s2s-front-stage.azurewebsites.net/my-profile')
        sleep(2)

    def test_name_surname(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        name_surname = profile_info.get_name_surname_text()
        self.assertEquals(name_surname, "Tester Toster")

    def test_days_at_space2study_text(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        days_at_space2study_text = profile_info.get_days_in_spase2study_days_numbers_text()
        self.assertEquals("2 days", days_at_space2study_text)

    def test_days_at_space2study_under_text(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        days_at_space2study_text = profile_info.get_days_in_spase2study_text()
        self.assertEquals("AT SPACE2STUDY", days_at_space2study_text)

    def test_language(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        native_language = profile_info.get_native_language_text()
        self.assertEquals("Native:\nUkrainian", native_language)
        # = profile_info.get_native_language_icon()
        #self.assertTrue(native_language_icon.is_displayed())

    def test_rating(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        rating_number = profile_info.get_profile_rating_text()
        self.assertEquals("0", rating_number)
        review_counter = profile_info.get_review_counter_text()
        self.assertEquals = ("0 REVIEWS", review_counter)

    def test_city_country_based(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        city_country_based = profile_info.get_city_country_based()
        self.assertEquals("Based in\nRivne, Ukraine", city_country_based)

    def test_native_language_icon(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        native_language_icon = profile_info.get_native_language_icon()
        self.assertTrue(native_language_icon.is_displayed())

    def test_avatar_is_active(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        avatar = profile_info.get_avatar()
        self.assertTrue(avatar.is_displayed())

    def test_edit_profile_button(self):
        my_profile = MyProfile(self.browser)
        profile_info = my_profile.get_profile_info()
        sleep(1)
        edit_profile_button = profile_info.get_edit_profile_button()
        self.assertTrue(edit_profile_button.is_displayed())
        profile_info.click_edit_profile_button()
        current_url = self.browser.current_url
        self.assertEquals("https://s2s-front-stage.azurewebsites.net/my-profile/edit", current_url)

    def test_completeness_percent(self):
        my_profile = MyProfile(self.browser)
        profile_completeness = my_profile.get_profile_completeness()
        sleep(1)
        completeness_percent_array = profile_completeness.get_completeness_percent_array()
        self.assertEquals(['0%', '20%', '40%', '60%', '80%', '100%'], completeness_percent_array)
        self.assertEquals(6, len(completeness_percent_array))

    def test_profile_completion_steps_containers(self):
        my_profile = MyProfile(self.browser)
        profile_completeness = my_profile.get_profile_completeness()
        sleep(1)
        profile_completeness.click_show_hide_button()
        profile_completion_steps_containers = profile_completeness.get_profile_completion_steps_containers()

    def test_profile_completion_steps_container_2(self):
        my_profile = MyProfile(self.browser)
        profile_completeness = my_profile.get_profile_completeness()
        sleep(1)
        profile_completeness.click_show_hide_button()
        steps_container = profile_completeness.get_profile_completion_steps_containers()[1]
        title = profile_completeness.get_profile_completion_steps_container_title(steps_container)
        icon = profile_completeness.get_profile_completion_steps_container_icon(steps_container)
        description = profile_completeness.get_profile_completion_steps_container_description(steps_container)
        self.assertEquals("Tell us about your professional experience", title)
        self.assertEquals("Fill in your education and qualification details.", description)
        self.assertTrue(icon.is_displayed())

    def test_video_presentation_element(self):
        my_profile = MyProfile(self.browser)
        video_presentation = my_profile.get_video_presentation()
        sleep(1)
        title = video_presentation.get_title_text()
        video = video_presentation.get_video()
        title_bar = video_presentation.get_title_bar()
        self.assertEquals("Video Presentation",title)
        self.assertTrue(video.is_displayed())
        self.assertTrue(title_bar.is_displayed())

    def test_student_review_rating(self):
        my_profile = MyProfile(self.browser)
        student_review = my_profile.get_student_review()
        sleep(1)
        review_counter = student_review.get_review_counter_text()
        rating_number = student_review.get_rating_number_text()
        reflects_the_stars_element = student_review.get_reflects_the_stars_element()
        self.assertEquals("0 reviews", review_counter)
        self.assertEquals("0", rating_number)
        self.assertTrue(reflects_the_stars_element.is_displayed())

    def test_student_review_title(self):
        my_profile = MyProfile(self.browser)
        student_review = my_profile.get_student_review()
        sleep(1)
        title = student_review.get_title_text()
        self.assertEquals("What students say", title)

    def test_student_rating_progress_bars(self):
        my_profile = MyProfile(self.browser)
        student_review = my_profile.get_student_review()
        sleep(1)
        progress_bars_list = student_review.get_rating_progress_bars_list()
        progress_bar = progress_bars_list[0]
        self.assertEquals(5, len(progress_bars_list))
        progress_bar_name = student_review.get_rating_progress_bar_name(progress_bar)
        progress_bar_vote_counter = student_review.get_rating_progress_bar_vote_counter(progress_bar)
        span_element = student_review.get_rating_progress_bar_span_element(progress_bar)
        self.assertEquals("5 stars", progress_bar_name)
        self.assertEquals("3", progress_bar_vote_counter)
        self.assertTrue(span_element.is_displayed())

    def test_student_comments(self):
        my_profile = MyProfile(self.browser)
        student_review = my_profile.get_student_review()
        sleep(1)
        students_comments_list = student_review.get_students_comments_list()
        students_comment = students_comments_list[1]
        avatar = student_review.get_student_comment_user_avatar(students_comment)
        nickname = student_review.get_student_comment_user_nickname_text(students_comment)
        date = student_review.get_student_comment_user_date_text(students_comment)
        comment = student_review.get_student_comment_text(students_comment)
        direction_and_level = student_review.get_student_comment_direc
        tion_and_level_text(students_comment)
        more_review_button = student_review.get_student_more_review_button()
        self.assertTrue(more_review_button.is_displayed())
        self.assertEquals("Tart D.", nickname)
        self.assertEquals("March 2, 2023", date)
        self.assertEquals("Languages - English - Beginner", direction_and_level)
        self.assertEquals("i spent a lot of money, but my english only got worse after lesson", comment)
        self.assertEquals(5, len(students_comments_list))
        self.assertTrue(avatar.is_displayed())

    def test_student_comments_rating_in_stars(self): #dev bug
        my_profile = MyProfile(self.browser)
        student_review = my_profile.get_student_review()
        sleep(1)
        students_comments_list = student_review.get_students_comments_list()
        students_comment = students_comments_list[1]
        stars_rating_full = student_review.get_student_comment_stars_rating_full(students_comment)
        stars_rating_empty = student_review.get_student_comment_stars_rating_empty(students_comment)
        self.assertEquals(3,stars_rating_full)
        self.assertEquals(2,stars_rating_empty)