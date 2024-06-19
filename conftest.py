from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser(request):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        yield driver
        driver.quit()