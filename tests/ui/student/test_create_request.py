import unittest
from random import randint

import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from SpaceToStudy.ui.pages.my_profile.my_profile_page import MyProfile
from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
from SpaceToStudy.ui.pages.offers_request_modal.offers_request_modal import (OffersRequestModal,
                                                                             FirstBlock,
                                                                             SecondBlock,
                                                                             ThirdBlock)
from tests.ui.test_runners import TestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class CreateStudentRequestTestCase(TestRunnerWithStudent):
    def test_create_request_as_student(self):
        categories_url = "https://s2s-front-stage.azurewebsites.net/categories"
        category = "Music"
        subject = "Guitar"
        title = "Title 1"
        description = "Description Description Description Description Description Description"
        price = "1"
        questions = "Questions 1"
        answer = "Answer 1"

        categories_url = (HomePageStudent(self.driver)
                          .get_header()
                          .get_navigate_links()[0]
                          .click()
                          .parent
                          .current_url)
        self.assertEqual(categories_url, categories_url)
        offers_request_modal = (CategoriesPage(self.driver)
                                .get_student_private_lesson_component()
                                .click_create_request_btn())

        first_block = offers_request_modal.get_first_block()
        category_input = first_block.get_category_input()
        category_input.set_text(category)
        category_input.press_down_button(1).press_enter_button()
        subject_input = first_block.get_subject_input()
        subject_input.set_text(subject)
        subject_input.press_down_button(1).press_enter_button()
        first_block.get_checkbox_beginner().set_check()

        second_block = offers_request_modal.get_second_block()
        second_block.get_title_input().set_text(title)
        second_block.get_describe_input().set_text(description)
        second_block.get_language_input().press_down_button(2).press_enter_button()
        second_block.get_price_input().set_text(price)

        third_block = offers_request_modal.get_third_block()
        third_block.get_question_input().set_text(questions)
        third_block.set_answer_input_text(answer)
        third_block.click_add_question_btn()
        offers_request_modal.click_add_to_draft_btn()

        inline_card_component = OfferDetailsPage(self.driver).get_offer_inline_card_component()
        expected_title = inline_card_component.get_offer_title()
        expected_subject_label = inline_card_component.get_subject_label()
        expected_price_value = inline_card_component.get_price_value()

        self.assertEqual(title, expected_title)
        self.assertEqual(subject.upper(), expected_subject_label)
        self.assertEqual(float(price), expected_price_value)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/99")
    def test_offer_details(self):
        category = "Music"
        subject = "Guitar"
        title = "I'd like to become a guitar coach"
        desc = "Prefer focus on standard"
        language = "Ukrainian"
        price = "700"
        question = "What staff do I need?"
        answer = "You need a guitar"

        (HeaderComponent(self.driver)
         .get_navigate_links()[0]
         .click())
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create request')]").click()
        first_block = FirstBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[1]"))
        first_block.get_category_input().set_text(category)
        first_block.get_category_input().press_down_button(1).press_enter_button()
        first_block.get_subject_input().set_text(subject)
        first_block.get_subject_input().press_down_button(1).press_enter_button()
        first_block.get_checkbox_beginner().set_check()

        second_block = SecondBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]"))
        second_block.get_title_input().set_text(title)
        second_block.get_describe_input().set_text(desc)
        second_block.get_language_input().set_text(language)
        second_block.get_language_input().press_down_button(1).press_enter_button()
        second_block.get_price_input().set_text(price)

        third_block = ThirdBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[3]"))
        third_block.get_question_input().set_text(question)
        third_block.set_answer_input_text(answer)
        (OffersRequestModal(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form"))
         .click_add_to_draft_btn())

        inline_card = OfferDetailsPage(self.driver).get_inline_card_component()
        student_name_expected = (f"{ValueProvider.get_student_first_name()} "
                                 f"{ValueProvider.get_student_last_name()[0]}.")
        student_name_actual = inline_card.get_person_name()
        card_title_actual = inline_card.get_offer_title()
        card_subject_actual = inline_card.get_subject_label()
        card_level_actual = inline_card.get_level_label()
        card_language_actual = inline_card.get_languages()
        card_price_actual = inline_card.get_price_value()
        self.assertEqual(student_name_expected, student_name_actual)
        self.assertEqual(title, card_title_actual)
        self.assertEqual(str.upper(subject), card_subject_actual)
        self.assertEqual(str.upper("Beginner"), card_level_actual)
        self.assertEqual(language, card_language_actual)
        self.assertEqual(float(price), card_price_actual)

        general_info_component = OfferDetailsPage(self.driver).get_general_info_component()
        offer_desc_actual = OfferDetailsPage(self.driver).get_about_offer_desc()
        subject_actual = (general_info_component
                          .get_tutoring_subject_component()
                          .get_value())
        level_actual = (general_info_component
                        .get_preparation_levels_component()
                        .get_values()[0]
                        .get_text())
        language_actual = (general_info_component
                           .get_tutoring_languages_component()
                           .get_values()[0]
                           .get_text())
        price_actual = (general_info_component
                        .get_pricing_component()
                        .get_value())
        self.assertEqual(desc, offer_desc_actual)
        self.assertEqual(subject, subject_actual)
        self.assertEqual("Beginner", level_actual)
        self.assertEqual(language, language_actual)
        self.assertEqual(f"{price} UAH/hour", price_actual)

        question_actual = (OfferDetailsPage(self.driver)
                           .get_frequently_asked_questions_component()
                           .get_questions()[0].get_question_text())
        answer_actual = (OfferDetailsPage(self.driver)
                         .get_frequently_asked_questions_component()
                         .get_questions()[0]
                         .click_question_btn()
                         .get_answer())
        self.assertEqual(question, question_actual)
        self.assertEqual(answer, answer_actual)

    @allure.testcase("https://github.com/ita-social-projects/SpaceToStudy-Client/issues/1029")
    def test_offer_details_in_student_profile(self):
        offers_request_modal = HomePageStudent(self.driver)
        offers_request_modal.get_categories_header_link().click()
        cp = CategoriesPage(self.driver)
        cn = cp.get_categories_names()
        random_category_num = randint(0, len(cn) - 1)
        clicked_category = cn[random_category_num].text.split("\n")[0]
        cn[random_category_num].click()
        subcategories_list = cp.get_cards()
        random_subcategory_num = randint(0, len(subcategories_list) - 1)
        subject = subcategories_list[random_subcategory_num].get_title()
        offers_request_modal = (CategoriesPage(self.driver)
                                .get_student_private_lesson_component()
                                .click_create_request_btn())
        first_block = offers_request_modal.get_first_block()
        category_input = first_block.get_category_input()
        category_input.set_text(clicked_category)
        category_input.press_down_button(1).press_enter_button()
        subject_input = first_block.get_subject_input()

        check_boxes = first_block.get_all_checkboxes()
        random_check_box_num = randint(0, len(check_boxes) - 1)
        level = check_boxes[random_check_box_num].text
        check_boxes[random_check_box_num].click()

        subject_input.set_text(subject)
        subject_input.press_down_button(1).press_enter_button()

        subject_input.press_down_button(1).press_enter_button()
        second_block = offers_request_modal.get_second_block()
        title = "This is a sort of Title"
        description = "This is a kind of Description"
        price = "789"
        second_block.get_title_input().set_text(title)
        second_block.get_describe_input().set_text(description)
        second_block.get_language_input().press_down_button(randint(1, 7)).press_enter_button()
        second_block.get_language_input().press_down_button(randint(1, 7)).press_enter_button()
        expected_languages_elements = second_block.get_all_selected_languages()
        expected_languages = list()
        for lang in expected_languages_elements:
            expected_languages.append(lang.text)
        second_block.get_price_input().set_text(price)
        third_block = offers_request_modal.get_third_block()
        question = "What is the question?"
        answer = "What is the answer? Answer it is."
        third_block.get_question_input().set_text(question)
        third_block.set_answer_input_text(answer)
        third_block.click_add_question_btn()
        offers_request_modal.click_add_to_draft_btn()

        general_info_component = OfferDetailsPage(self.driver).get_general_info_component()
        offer_desc_actual = OfferDetailsPage(self.driver).get_about_offer_desc()
        subject_actual = (general_info_component
                          .get_tutoring_subject_component()
                          .get_value())
        level_actual = (general_info_component
                        .get_preparation_levels_component()
                        .get_values()[0]
                        .get_text())
        price_actual = (general_info_component
                        .get_pricing_component()
                        .get_value())

        inline_card = OfferDetailsPage(self.driver).get_inline_card_component()
        student_name_actual = inline_card.get_person_name()
        self.assertEqual(description, offer_desc_actual)
        self.assertEqual(subject, subject_actual)
        self.assertEqual(level, level_actual)
        languages_actual = list()
        for i in range(0, len(expected_languages)):
            languages_actual.append((general_info_component
                                     .get_tutoring_languages_component()
                                     .get_values()[i]
                                     .get_text()))
        self.assertEqual(expected_languages, languages_actual)
        self.assertEqual(f"{price} UAH/hour", price_actual)
        question_actual = (OfferDetailsPage(self.driver)
                           .get_frequently_asked_questions_component()
                           .get_questions()[0].get_question_text())
        answer_actual = (OfferDetailsPage(self.driver)
                         .get_frequently_asked_questions_component()
                         .get_questions()[0]
                         .click_question_btn().get_answer())
        self.assertEqual(question, question_actual)
        self.assertEqual(answer, answer_actual)

        hps = HomePageStudent(self.driver).click_account_button()
        hps.get_My_profile_button().click()
        mp_name_surname = MyProfile(self.driver).get_name_surname_text().split()

        student_name_expected = (f"{mp_name_surname[0]} "
                                 f"{mp_name_surname[1][:1]}.")

        self.assertEqual(student_name_expected, student_name_actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
