import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def orangehrm():
    driver = webdriver.Chrome()

    # this automatically logs in instead of applying in each test methods to log in
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    driver.find_element(By.NAME, "username").send_keys('Admin')
    driver.find_element(By.NAME, "password").send_keys('admin123')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    yield driver


def test_display_dashboard(orangehrm):
    wait = WebDriverWait(orangehrm, 10)

    dashboard = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb"))
    )
    assert dashboard.is_displayed()
    print("Dashboard title is visible")


def test_displayed_quicklinks(orangehrm):
    wait = WebDriverWait(orangehrm,10)

    assign_leave = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"oxd-icon"))
    )
    assert assign_leave.is_displayed()
    print("Assign icon id displayed")

    leave_list = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,""))
    )
    assert leave_list.is_displayed()
    print("Leave icon is displayed")

    timesheet = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,""))
    )
    assert timesheet.is_displayed()
    print("Timesheet is displayed")

    apply_leave = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,""))
    )
    assert apply_leave.is_displayed()
    print("it exist")

    my_leave = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, ""))
    )
    assert my_leave.is_displayed()
    print("it exist")

    my_timesheet = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, ""))
    )
    assert my_timesheet.is_displayed()
    print("it exist")

def test_assign_leave(orangehrm):
    wait = WebDriverWait(orangehrm,10)

    assign_leave = orangehrm.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[1]/button')
    assign_leave.click()
    time.sleep(2)

    wait.until(EC.url_contains("leave/assignLeave"))
    assert "leave/assignLeave" in orangehrm.current_url
    print("Successfully navigated to Assign Leave page!")

def test_leave_list(orangehrm):

    leave_list = orangehrm.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/button/svg')
    leave_list.click()
    time.sleep(2)

    WebDriverWait.until(EC.url_contains("/leave/viewLeaveList"))


