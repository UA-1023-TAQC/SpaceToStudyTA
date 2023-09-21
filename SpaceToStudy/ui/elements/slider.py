import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement


@allure.step("Get pixel value of {slider} element")
def convert_range_slider_value_to_pixel_value(target_range_value: int, slider: WebElement,
                                              slider_thumb: WebElement) -> int:
    min_value = int(slider_thumb.get_attribute("min"))
    max_value = int(slider_thumb.get_attribute("max"))
    slider_pixel_width = slider.size['width']
    slider_value_width = max_value - min_value
    convert_to_pixels = slider_pixel_width / slider_value_width
    return convert_to_pixels * (target_range_value - min_value)


class Slider(BaseElement):

    @allure.step("Drag slider to the {target_value} of {slider} element ")
    def drag_slider_to_value(self, target_value: int, slider: WebElement, slider_thumb: WebElement):
        target_position = convert_range_slider_value_to_pixel_value(target_value, slider, slider_thumb)
        slider_width = slider.size['width']
        (ActionChains(self.node)
         .click_and_hold(slider_thumb)
         .move_by_offset(-int(slider_width / 2), 0)  # move to min value
         .move_by_offset(target_position, 0)  # move to target from min
         .release()
         .perform())
        return self

    @allure.step("Drag slider to the left by {values_to_the_left} of {slider} element ")
    def drag_slider_left(self, values_to_the_left: int, slider: WebElement, slider_thumb: WebElement):
        target_value = float(slider_thumb.get_attribute('value')) - values_to_the_left
        self.drag_slider_to_value(int(target_value), slider, slider_thumb)
        return self

    @allure.step("Drag slider to the right by {values_to_the_left} of {slider} element ")
    def drag_slider_right(self, values_to_the_right: int, slider: WebElement, slider_thumb: WebElement):
        target_value = float(slider_thumb.get_attribute('value')) + values_to_the_right
        self.drag_slider_to_value(int(target_value), slider, slider_thumb)
        return self
