Project structure
pages/

login_page.py – Page Object for the login screen (open page, submit credentials, error banner helper).

dashboard.py – Page Object for the Dashboard (widgets, charts, quick launch, Buzz, punch in, etc.).

test/

test_login.py – Login tests (valid/invalid credentials, link navigation).

test_dashboard.py – Dashboard tests (widgets visibility, navigation, charts, Buzz, punch in, configuration modal).

config/

config.py – Global settings such as BASE_URL.

reports/

assets/ – Static files (if needed for reports).

*.html – Pytest HTML reports generated per run.

conftest.py – Shared Pytest fixtures and hooks (WebDriver setup/teardown, HTML reporting, screenshots on failure).​

Prerequisites
Python 3.8+ installed.

Google Chrome installed.

ChromeDriver compatible with your Chrome version and on your PATH (or configured via webdriver-manager / local path).​

Recommended: create and activate a virtual environment for the project.

Install dependencies (example):

bash
pip install -r requirements.txt
Typical requirements.txt:

text
selenium
pytest
pytest-html
Running the tests
From the project root (where conftest.py lives), run:

bash
pytest
Pytest will:

Start a fresh Chrome browser for each test using the driver fixture (maximized with implicit waits).

Generate an HTML report under reports/ with a timestamped filename like orangehrm_report_YYYYMMDD_HHMMSS.html and embed screenshots for failed tests via pytest-html extras.​

To run only login or dashboard tests:

bash
pytest test/test_login.py
pytest test/test_dashboard.py
Use -k to filter by test name pattern:

bash
pytest -k "punch_in or invalid_credentials"
Test coverage
Current high‑level coverage:

Login page

Page load and presence of username, password, and login button.

Multiple invalid credential combinations (empty fields, wrong user, wrong password) and verification of the error banner.

External “OrangeHRM, Inc” link navigation to the marketing site.

Dashboard

Successful login leads to /dashboard and “Dashboard” header is visible.

Visibility of all main widgets: Time at Work, My Actions, Quick Launch, Buzz Latest Posts, Employees on Leave Today, Employee Distribution by Sub Unit/Location.

Quick Launch actions navigate to their respective URLs (Assign Leave, Leave List, Apply Leave, My Leave, Timesheets, My Timesheet).

My Actions items navigate to Performance Review and Candidates pages.

Buzz widget and example post visibility.

Pie chart legend toggling for Sub Unit and Location charts (all slices hidden after toggling).

Employees on Leave configuration gear icon and configuration modal.

Punch In button navigating to /attendance/punchIn.

How to extend
Add new pages to pages/ as Page Objects, following the existing LoginPage and Dashboard patterns.

Create corresponding tests in test/ that use the shared driver fixture and methods from your Page Objects.

Update config.Config with additional settings (e.g., alternative base URLs, credentials, timeouts) as the framework grows.​

newly added file called helper

