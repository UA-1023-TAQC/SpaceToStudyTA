import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/p')
LESSONS_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button[1]/div')
QUIZZES_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button[2]/div')
ATTACHMENTS_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button[3]/div')
NEW_LESSON_BTN = (By.XPATH, '//a[contains(text(), "New lesson")]')
SEARCH_LESSONS_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div/div/input')

TABLE_LESSON_TITLES_ROW = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div/table/thead/tr/')
TITLE_COLUMN = (By.XPATH, f'{TABLE_LESSON_TITLES_ROW}/th[1]/span')
ATTACHMENTS_COLUMN = (By.XPATH, f'{TABLE_LESSON_TITLES_ROW}/th[2]/span')
LAST_UPDATES_LESSONS_COLUMN = (By.XPATH, f'{TABLE_LESSON_TITLES_ROW}/th[3]/span')
ACTIONS_LESSONS_COLUMN = (By.XPATH, f'{TABLE_LESSON_TITLES_ROW}/th[4]/span')

TABLE_QUIZZES_TITLES_ROW = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[1]/table/thead/tr')
QUIZ_TITLE_COLUMN = (By.XPATH, f'{TABLE_QUIZZES_TITLES_ROW}/th[1]/span')
QUESTIONS_COLUMN = (By.XPATH, f'{TABLE_QUIZZES_TITLES_ROW}/th[2]/span')
LAST_UPDATE_QUIZZES_COLUMN = (By.XPATH, f'{TABLE_QUIZZES_TITLES_ROW}/th[3]/span')
ACTIONS_QUIZZES_COLUMN = (By.XPATH, f'{TABLE_QUIZZES_TITLES_ROW}/th[4]/span')

TABLE_ATTACHMENTS_TITLES_ROW = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/table/thead/tr')
SEARCH_ATTACHMENTS_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div/div/input')
ADD_ATTACHMENT_BTN = (By.XPATH, '//button[contains(text(), "Add Attachment")]')
FILE_COLUMN = (By.XPATH, f'{TABLE_ATTACHMENTS_TITLES_ROW}/th[1]/span')
SIZE_COLUMN = (By.XPATH, f'{TABLE_ATTACHMENTS_TITLES_ROW}/th[2]/span')
LAST_UPDATE_ATTACHMENTS_COLUMN = (By.XPATH, f'{TABLE_ATTACHMENTS_TITLES_ROW}/th[3]/span')
ACTIONS_ATTACHMENTS_COLUMN = (By.XPATH, f'{TABLE_ATTACHMENTS_TITLES_ROW}/th[4]/span')

ROW_WITH_NO_MATCHES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]')

ROWS_PATH = "//tbody[@class='MuiTableBody-root']//tr"


class MyResourcesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get page title")
    def get_page_title(self) -> str:
        return self.driver.find_element(*PAGE_TITLE).text

    @allure.step("Get lessons button")
    def get_lessons_btn(self) -> WebElement:
        return self.driver.find_element(*LESSONS_BTN)

    @allure.step("get text lessons button")
    def get_lessons_btn_text(self) -> str:
        return self.driver.find_element(*LESSONS_BTN).text

    @allure.step("Click lessons button")
    def click_lessons_btn(self):
        self.get_lessons_btn().click()

    @allure.step("Get quizzes button")
    def get_quizzes_btn(self) -> WebElement:
        return self.driver.find_element(*QUIZZES_BTN)

    @allure.step("Get text quizzes button")
    def get_quizzes_btn_text(self) -> str:
        return self.driver.find_element(*QUIZZES_BTN).text

    @allure.step("Click quizzes button")
    def click_quizzes_btn(self):
        self.get_quizzes_btn().click()

    @allure.step("Get attachments button")
    def get_attachments_btn(self) -> WebElement:
        return self.driver.find_element(*ATTACHMENTS_BTN)

    @allure.step("Get text attachments button")
    def get_attachments_btn_text(self) -> str:
        return self.driver.find_element(*ATTACHMENTS_BTN).text

    @allure.step("Click attachments button")
    def click_attachments_btn(self):
        self.get_attachments_btn().click()

    @allure.step("Get new lesson button")
    def get_new_lesson_btn(self) -> WebElement:
        return self.driver.find_element(*NEW_LESSON_BTN)

    @allure.step("Get text new lesson button")
    def get_new_lesson_btn_text(self) -> str:
        return self.driver.find_element(*NEW_LESSON_BTN).text

    @allure.step("Click new lesson button")
    def click_new_lesson_btn(self):
        self.get_new_lesson_btn().click()

    @allure.step("Get search lessons input")
    def get_search_lessons_input(self) -> WebElement:
        return self.driver.find_element(*SEARCH_LESSONS_INPUT)

    @allure.step("Set search lessons input")
    def set_search_lessons_input(self, text):
        self.get_search_lessons_input().send_keys(text)

    @allure.step("Get text search lessons input")
    def get_search_lessons_input_text(self) -> str:
        return self.driver.find_element(*SEARCH_LESSONS_INPUT).text

    @allure.step("Get search lessons titles row")
    def get_table_lessons_titles_row(self) -> WebElement:
        return self.driver.find_element(*TABLE_LESSON_TITLES_ROW)

    @allure.step("Get title column")
    def get_title_column(self) -> WebElement:
        return self.driver.find_element(*TITLE_COLUMN)

    @allure.step("Click title column")
    def click_title_column(self):
        self.get_title_column().click()

    @allure.step("Get attachments column")
    def get_attachments_column(self) -> WebElement:
        return self.driver.find_element(*ATTACHMENTS_COLUMN)

    @allure.step("Get last updates lessons column")
    def get_last_updates_lessons_column(self) -> WebElement:
        return self.driver.find_element(*LAST_UPDATES_LESSONS_COLUMN)

    @allure.step("Click last updates lessons column")
    def click_last_updates_lessons_column(self):
        self.get_last_updates_lessons_column().click()

    @allure.step("Get actions lessons column")
    def get_actions_lessons_column(self) -> WebElement:
        return self.driver.find_element(*ACTIONS_LESSONS_COLUMN)

    @allure.step("Get quizzes titles row")
    def get_quizzes_titles_row(self) -> WebElement:
        return self.driver.find_element(*TABLE_QUIZZES_TITLES_ROW)

    @allure.step("Get quiz title column")
    def get_quiz_title_column(self) -> WebElement:
        return self.driver.find_element(*QUIZ_TITLE_COLUMN)

    @allure.step("Get text quiz title column")
    def get_quiz_title_column_text(self) -> str:
        return self.get_quiz_title_column().text

    @allure.step("Get questions column")
    def get_questions_column(self) -> WebElement:
        return self.driver.find_element(*QUESTIONS_COLUMN)

    @allure.step("Get text questions column")
    def get_questions_column_text(self) -> str:
        return self.get_questions_column().text

    @allure.step("Get last update quizzes column")
    def get_last_update_quizzes_column(self) -> WebElement:
        return self.driver.find_element(*LAST_UPDATE_QUIZZES_COLUMN)

    @allure.step("Get text last update quizzes column")
    def get_last_update_quizzes_column_text(self) -> str:
        return self.get_last_update_quizzes_column().text

    @allure.step("Get actions quizzes column")
    def get_actions_quizzes_column(self) -> WebElement:
        return self.driver.find_element(*ACTIONS_QUIZZES_COLUMN)

    @allure.step("Get text actions quizzes column")
    def get_actions_quizzes_column_text(self) -> str:
        return self.get_actions_quizzes_column().text

    @allure.step("Get attachments titles row")
    def get_attachments_titles_row(self) -> WebElement:
        return self.driver.find_element(*TABLE_ATTACHMENTS_TITLES_ROW)

    @allure.step("Get \"add attachment button\"")
    def get_add_attachment_btn(self) -> WebElement:
        return self.driver.find_element(*ADD_ATTACHMENT_BTN)

    @allure.step("Click \"add attachment button\"")
    def click_add_attachment_btn(self):
        self.get_add_attachment_btn().click()

    @allure.step("Get file column")
    def get_file_column(self) -> WebElement:
        return self.driver.find_element(*FILE_COLUMN)

    @allure.step("Get text file column")
    def get_file_column_text(self) -> str:
        return self.get_file_column().text

    @allure.step("Click file column")
    def click_file_column(self):
        self.get_file_column().click()

    @allure.step("Get size column")
    def get_size_column(self) -> WebElement:
        return self.driver.find_element(*SIZE_COLUMN)

    @allure.step("Get text size column")
    def get_size_column_text(self) -> str:
        return self.get_size_column().text

    @allure.step("Click size column")
    def click_size_column(self):
        self.get_size_column().click()

    @allure.step("Get last update attachments column")
    def get_last_update_attachments_column(self) -> WebElement:
        return self.driver.find_element(*LAST_UPDATE_ATTACHMENTS_COLUMN)

    @allure.step("Get text last update attachments column")
    def get_last_update_attachments_column_text(self) -> str:
        return self.get_last_update_attachments_column().text

    @allure.step("Click last update attachments column")
    def click_last_update_attachments_column(self):
        self.get_last_update_attachments_column().click()

    @allure.step("Get actions attachments column")
    def get_actions_attachments_column(self) -> WebElement:
        return self.driver.find_element(*ACTIONS_ATTACHMENTS_COLUMN)

    @allure.step("Get row with no matches")
    def get_row_with_no_matches(self) -> WebElement:
        return self.driver.find_element(*ROW_WITH_NO_MATCHES)

    @allure.step("Get text row with no matches")
    def get_row_with_no_matches_text(self) -> str:
        return self.get_row_with_no_matches().text

    @allure.step("Get list of rows lessons")
    def get_list_of_rows_lessons(self) -> list:
        return self.driver.find_elements(By.XPATH, ROWS_PATH)
