from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#/html/body/div/div/div[2]/div[2]/div[4]
#/html/body/div/div/div[2]/div[2]/div[4]

TITLE = (By.XPATH, "./p")
RATING_NUMBER = (By.XPATH, "./div[1]/div[1]/div[1]/h4")
RATING_STARS_CONTAINER = (By.XPATH, "./div[1]/div[1]/div[2]/span")
RATING_REVIEW_COUNTER = (By.XPATH, "./div[1]/div[1]/p")

RATING_PROGRESS_BARS = (By.XPATH, "./div[1]/div[2]")
COMMENTS = (By.XPATH, "./div[2]/div")
MORE_REVIEW_BUTTON = (By.XPATH, "./div[2]/button")

# FULL_STAR_PATH = "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
# EMPTY_STAR_PATH = "M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27z"

active_star_testid = "StarIcon"  
inactive_star_testid = "StarSharpIcon"  


#<svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1vdj6uk" focusable="false" aria-hidden="true" viewBox="0 0 24 24" data-testid="StarIcon"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></svg>
#<svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1j738yg" focusable="false" aria-hidden="true" viewBox="0 0 24 24" data-testid="StarSharpIcon"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27z"></path></svg>

class StudentReviews:
    def __init__(self, node):
        self.node = node

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_rating_number_text(self) -> str:
        return self.node.find_element(*RATING_NUMBER).text

    def get_review_counter_text(self) -> str:
        return self.node.find_element(*RATING_REVIEW_COUNTER).text

    def get_stars_container(self) -> WebElement:
        return self.node.find_element(*RATING_STARS_CONTAINER)

    def get_rating_progress_bars_element(self) -> WebElement:
        return self.node.find_element(*RATING_PROGRESS_BARS)

    def get_rating_progress_bars_list(self) -> List[WebElement]:
        return self.node.find_element(*RATING_PROGRESS_BARS).find_elements(By.XPATH, "./div")

    def get_rating_progress_bar_name_text(self, rating_progress_bar) -> str:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: str
        """
        return rating_progress_bar.find_elements(By.XPATH, ".//p")[0].text

    def get_rating_progress_bar_vote_counter_text(self, rating_progress_bar) -> str:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: str
        """
        return rating_progress_bar.find_elements(By.XPATH, ".//p")[1].text

    def get_rating_progress_bar_completion(self, rating_progress_bar) -> WebElement:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: WebElement
        """
        return rating_progress_bar.find_element(By.XPATH, ".//span")

    def get_students_comments_list(self) -> List[WebElement]:
        return self.node.find_element(*COMMENTS).find_elements(By.XPATH, "./div")

    def get_student_comment_user_avatar(self, students_comment) -> WebElement:
        return students_comment.find_element(By.XPATH, ".//*[local-name()='svg']")

    def click_student_comment_user_avatar(self, students_comment):
        self.get_students_comment_user_avatar(students_comment).click()

    def get_student_comment_user_nickname_text(self, students_comment) -> str:
        return students_comment.find_elements(By.XPATH, ".//p")[0].text

    def student_comment_user_nickname_click(self, students_comment):
        self.get_students_comment_user_nickname(students_comment).click

    def get_student_comment_user_date_text(self, students_comment) -> str:
        return students_comment.find_elements(By.XPATH, ".//p")[1].text

    def get_student_comment_direction_and_level_text(self, students_comment) -> str:
        return students_comment.find_elements(By.XPATH, ".//p")[2].text

    def get_student_comment_text(self, students_comment) -> str:
        return students_comment.find_elements(By.XPATH, ".//p")[3].text

    def get_student_comment_stars_rating_element(self, students_comment) -> WebElement:
        return students_comment.find_element(By.XPATH, ".//span")

    def __get_student_comment_stars_rating_counter(self, students_comment):
        star_elements = self.get_student_comment_stars_rating_element(students_comment).find_elements(By.CSS_SELECTOR, "*[data-testid^='Star']")

        active_count = 0
        inactive_count = 0

        for star in star_elements:
            if star.get_attribute('data-testid') == active_star_testid:
                active_count += 1
            elif star.get_attribute('data-testid') == inactive_star_testid:
                inactive_count += 1
            else:
                raise ValueError("You use an unknown 'path' attribute 'd'")
        return (active_count, inactive_count)


    def get_student_comment_stars_active(self, students_comment) -> int:
        return self.__get_student_comment_stars_rating_counter(students_comment)[0]

    def get_student_comment_stars_inactive(self, students_comment) -> int:
        return self.__get_student_comment_stars_rating_counter(students_comment)[1]

    def get_student_more_review_button(self) -> WebElement:
        return self.node.find_element(*MORE_REVIEW_BUTTON)

    def student_more_review_button_click(self):
        self.get_student_more_review_button().click()



