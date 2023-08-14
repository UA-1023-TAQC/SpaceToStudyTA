from selenium.webdriver.common.by import By


HOW_TO_FIND_TUTOR_QUESTION = (By.XPATH, "./div[1]/div[1]")
HOW_TO_BOOK_LESSON_QUESTION = (By.XPATH, "./div[2]/div[1]")
RULES_FOR_STUDENTS_QUESTION = (By.XPATH, "./div[3]/div[1]")
PAY_FOR_LESSONS_QUESTION = (By.XPATH, "./div[4]/div[1]")


class AskedQuestions:

    def __init__(self, noda):
        self.noda = noda

    def open_hidden_text_one(self):
        return self.noda.find_element(*HOW_TO_FIND_TUTOR_QUESTION)

    def click_how_find_tutor_icon(self):
        self.open_hidden_text_one().click()

    def open_hidden_text_two(self):
        return self.noda.find_element(*HOW_TO_BOOK_LESSON_QUESTION)

    def click_how_book_lesson_icon(self):
        self.open_hidden_text_two().click()

    def open_hidden_text_three(self):
        return self.noda.find_element(*RULES_FOR_STUDENTS_QUESTION)

    def click_rules_for_students_icon(self):
        self.open_hidden_text_three().click()

    def open_hidden_text_four(self):
        return self.noda.find_element(*PAY_FOR_LESSONS_QUESTION)

    def click_pay_for_lessons_icon(self):
        self.open_hidden_text_four().click()