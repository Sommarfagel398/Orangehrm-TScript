import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def orangehrm():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(orangehrm):

    admin = 'Admin'
    password = 'admin123'

    orangehrm.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    orangehrm.find_element(By.NAME, "username").send_keys(admin)
    time.sleep(2)
    orangehrm.find_element(By.NAME, "password").send_keys(password)
    time.sleep(2)
    orangehrm.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    assert "dashboard" in orangehrm.current_url

    time.sleep(1)
    orangehrm.find_element(By.CLASS_NAME, 'oxd-userdropdown-tab').click()
    time.sleep(1)
    orangehrm.find_element(By.XPATH, '//a[text()="Logout"]').click()

def test_incorrect_username(orangehrm):

    admin = 'incorrectUsername'
    password = 'admin123'

    orangehrm.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    orangehrm.find_element(By.NAME, "username").send_keys(admin)
    time.sleep(2)
    orangehrm.find_element(By.NAME, "password").send_keys(password)
    time.sleep(2)
    orangehrm.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    error = WebDriverWait(orangehrm,10).until(
        EC.visibility_of_element_located(
            (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]')
        )
    )
    error.is_displayed()

def test_incorrect_password(orangehrm):

    admin = 'Admin'
    password = 'incorrectPass'

    orangehrm.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    orangehrm.find_element(By.NAME, "username").send_keys(admin)
    time.sleep(2)
    orangehrm.find_element(By.NAME, "password").send_keys(password)
    time.sleep(2)
    orangehrm.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    error = WebDriverWait(orangehrm,10).until(
        EC.visibility_of_element_located(
            (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]')
        )
    )
    error.is_displayed()

def test_reset_pass(orangehrm):
    orangehrm.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    link_text = orangehrm.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
    link_text.click()

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode" in orangehrm.current_url

    try:
        username = orangehrm.find_element(By.NAME,"username")
        username.send_keys('Admin')
        time.sleep(2)
        result = True
    except Exception:
        result = False

    print(result)

    confirmation = WebDriverWait(orangehrm,10).until(
        EC.visibility_of_element_located(
            (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div')
        )
    )
    confirmation.is_displayed()
    time.sleep(2)

def test_link_text(orangehrm):
    orangehrm.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    link = orangehrm.find_element(By.LINK_TEXT,'OrangeHRM, Inc')
    link.click()

    orangehrm.switch_to.window(orangehrm.window_handles[-1])

    assert 'https://www.orangehrm.com/' in orangehrm.current_url