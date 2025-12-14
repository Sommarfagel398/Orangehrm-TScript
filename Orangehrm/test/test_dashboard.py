# tests/test_dashboard.py
import time
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestDashboard:

    #dashboard confirms after loading
    def test_dashboard_loads_after_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_loaded()
    #testing if all widgets are presented
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

#this part test if the widgets of quick launch works and leads to a right directory or page
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

    #test script for testing My Actions form
    def test_my_actions_loads_in_dashboard(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_my_actions_loaded()
        time.sleep(5)


    def test_pending_self(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_pending_review()
        time.sleep(4)
        assert "/performance/searchEvaluatePerformanceReview" in driver.current_url
        time.sleep(5)

    def test_review_candidate(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_candidate_interview()
        time.sleep(4)
        assert "/recruitment/viewCandidates?statusId=4" in driver.current_url
        time.sleep(5)

    def test_my_buzz_post_dashboard(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_buzz_loaded()
        time.sleep(4)
