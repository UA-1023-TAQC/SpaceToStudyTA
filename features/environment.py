from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from tests.utils.value_provider import ValueProvider

IMPLICITLY_WAIT = 5


@fixture
def setup_teardown(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(IMPLICITLY_WAIT)
    context.driver.maximize_window()
    context.driver.get(ValueProvider.get_base_url())
    yield context
    context.driver.quit()

# def before_all(context):
#     use_fixture(setup_teardown, context)
#     # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.

def before_feature(context, feature):
    # model.init(environment='test')
    use_fixture(setup_teardown, context)
