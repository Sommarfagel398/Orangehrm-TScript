# pages/dashboard_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    # this is for url dashboard
    URL_PART = "/dashboard"

    # elements in the header
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    # Time at Work widgers inside the form
    TIME_AT_WORK_WIDGET = (By.XPATH, "//p[text()='Time at Work']")
    PUNCH_STATUS = (By.XPATH, "//p[text()='Punched In']")
    TODAY_TIME = (By.XPATH, "//p[text()='Today']")
    THIS_WEEK_TIME = (By.XPATH, "//p[text()='This Week']")

    # Actions widget inside the form
    MY_ACTIONS_WIDGET = (By.XPATH, "//p[text()='My Actions']")
    PENDING_SELF_REVIEW = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/button')
    CANDIDATE_TO_INTERVIEW = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/button')

    # Quick Launch widget inside the form
    QUICK_LAUNCH_WIDGET = (By.XPATH, "//p[text()='Quick Launch']")
    ASSIGN_LEAVE_BTN = (By.XPATH, "//button[contains(@title,'Assign Leave')]")
    LEAVE_LIST_BTN = (By.XPATH, "//button[contains(@title,'Leave List')]")
    TIMESHEETS_BTN = (By.XPATH, "//button[contains(@title,'Timesheets')]")
    APPLY_LEAVE_BTN = (By.XPATH, "//button[contains(@title,'Apply Leave')]")
    MY_LEAVE_BTN = (By.XPATH, "//button[contains(@title,'My Leave')]")
    MY_TIMESHEET_BTN = (By.XPATH, "//button[contains(@title,'My Timesheet')]")

    # Buzz Latest Posts widget inside the container
    BUZZ_WIDGET = (By.XPATH, "//p[text()='Buzz Latest Posts']")
    BUZZ_POST = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]')
    BUZZ_USERS = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/div')

    # Employees on Leave Today widget inside the container
    LEAVE_TODAY_WIDGET = (By.XPATH, "//p[text()='Employees on Leave Today']")
    NO_EMPLOYEES_MESSAGE = (By.XPATH, "//*[text()='No Employees are on Leave Today']")

    # Employee Distribution widgets inside the container
    EMPLOYEE_SUB_UNIT_CHART = (By.XPATH, "//p[text()='Employee Distribution by Sub Unit']")
    EMPLOYEE_LOCATION_CHART = (By.XPATH, "//p[text()='Employee Distribution by Location']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    #This is for confirmation if all widgets and forms in dashboard are displayed
    def is_loaded(self):
        header = self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
        return header.is_displayed() and self.URL_PART in self.driver.current_url

    def is_time_at_work_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.TIME_AT_WORK_WIDGET))
        return element.is_displayed()

    def is_my_actions_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.MY_ACTIONS_WIDGET))
        return element.is_displayed()

    def is_quick_launch_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.QUICK_LAUNCH_WIDGET))
        return element.is_displayed()

    def is_buzz_widget_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.BUZZ_WIDGET))
        return element.is_displayed()

    def is_leave_today_widget_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.LEAVE_TODAY_WIDGET))
        return element.is_displayed()

    def is_employee_distribution_charts_visible(self):
        sub_unit = self.driver.find_element(*self.EMPLOYEE_SUB_UNIT_CHART)
        location = self.driver.find_element(*self.EMPLOYEE_LOCATION_CHART)
        return sub_unit.is_displayed() and location.is_displayed()

    #This is to check if all quick actions are confirmed linked to the page or link

    def click_assign_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.ASSIGN_LEAVE_BTN)).click()

    def click_leave_list(self):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE_LIST_BTN)).click()

    def click_timesheets(self):
        self.wait.until(EC.element_to_be_clickable(self.TIMESHEETS_BTN)).click()

    def click_apply_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_LEAVE_BTN)).click()

    def click_my_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_LEAVE_BTN)).click()

    def click_my_timesheet(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_TIMESHEET_BTN)).click()


    #this part is for My Actions form
    def is_my_actions_loaded(self):
        form = self.wait.until(EC.visibility_of_element_located(self.MY_ACTIONS_WIDGET))
        return form.is_displayed() and self.URL_PART in self.driver.current_url

    def click_pending_review(self):

        self.wait.until(EC.url_contains("/dashboard"))

        element = self.wait.until(
            EC.element_to_be_clickable(self.PENDING_SELF_REVIEW)
        )
        element.click()

    def click_candidate_interview(self):

        self.wait.until(EC.url_contains("/dashboard"))

        element = self.wait.until(
            EC.element_to_be_clickable(self.CANDIDATE_TO_INTERVIEW)
        )
        element.click()

    #This is for the Buzz part
    def is_buzz_loaded(self):
        form = self.wait.until(EC.visibility_of_element_located(self.BUZZ_WIDGET))
        return form.is_displayed() and self.URL_PART in self.driver.current_url

    def buzz_post(self):
        confirmed = self.wait.until(EC.presence_of_element_located(self.BUZZ_POST))
        return confirmed.is_displayed()

    def users(self):
        user_test = self.wait.until(EC.element_to_be_clickable(self.BUZZ_USERS))
        user_test.click()