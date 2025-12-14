# tests/test_dashboard.py
import time
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestDashboard:

    def test_dashboard_loads_after_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_loaded()

    def test_time_at_work_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_time_at_work_visible()

    def test_my_actions_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_my_actions_visible()

    def test_quick_launch_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_quick_launch_visible()

    def test_buzz_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_buzz_widget_visible()

    def test_leave_today_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_leave_today_widget_visible()

    def test_employee_distribution_charts_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_employee_distribution_charts_visible()

    def test_quick_launch_assign_leave(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_assign_leave()

        assert "/leave/assignLeave" in driver.current_url

    def test_quick_launch_leave_list(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_leave_list()

        assert "/leave/viewLeaveList" in driver.current_url

    def test_quick_launch_apply_leave(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_apply_leave()

        assert "/leave/applyLeave" in driver.current_url


    def test_my_actions_loads_in_dashboard(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_loaded()
        time.sleep(5)

        my_actions = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/p')
        assert my_actions.is_displayed()
        time.sleep(5)

    def test_pending_self(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_pending_review()
        time.sleep(4)
        assert "/performance/searchEvaluatePerformanceReview" in driver.current_url

    def test_review_candidate(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_candidate_interview()
        time.sleep(4)
        assert "/recruitment/viewCandidates?statusId=4" in driver.current_url


