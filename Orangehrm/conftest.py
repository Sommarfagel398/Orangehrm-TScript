# conftest.py
import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    if not getattr(config.option, "htmlpath", None):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"reports/orangehrm_report_{timestamp}.html"
