from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent

STAR = (By.CSS_SELECTOR, "*[data-testid^='Star']")

ACTIVE_STAR_TEST_ID = "StarIcon"
INACTIVE_STAR_TEST_ID = "StarSharpIcon"

STAR_ATTRIBUTE = "data-testid"


class RatingStars(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.node = node

    def _get_student_comment_stars_rating_counter(self):
        star_elements = self.node.find_elements(*STAR)

        active_count = 0
        inactive_count = 0

        for star in star_elements:
            if star.get_attribute(STAR_ATTRIBUTE) == ACTIVE_STAR_TEST_ID:
                active_count += 1
            elif star.get_attribute(STAR_ATTRIBUTE) == INACTIVE_STAR_TEST_ID:
                inactive_count += 1
            else:
                raise ValueError("Somthing changed in STAR_ATTRIBUTE or value")
        return active_count, inactive_count

    def get_student_comment_stars_active(self) -> int:
        return self._get_student_comment_stars_rating_counter()[0]

    def get_student_comment_stars_inactive(self) -> int:
        return self._get_student_comment_stars_rating_counter()[1]
