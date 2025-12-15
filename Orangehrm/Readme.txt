# OrangeHRM Selenium Pytest Suite

End‑to‑end UI tests for the OrangeHRM demo application using Selenium WebDriver and pytest.[web:6]

## Project structure

- `config.py` – base URL configuration for the OrangeHRM demo site.
- `conftest.py` – shared pytest fixtures, including the `driver` fixture that creates and tears down a Chrome WebDriver instance.[web:12]
- `pages/` – Page Object Model classes.
  - `login_page.py` – actions and locators for the login page.
  - `dashboard_page.py` – actions and locators for the dashboard widgets and quick‑launch links.
- `tests/` – test cases.
  - `test_login.py` – login and navigation tests.
  - `test_dashboard.py` – dashboard visibility and navigation tests.

## Requirements

- Python 3.8+
- Google Chrome browser
- Matching ChromeDriver or Selenium Manager support
- Recommended packages:
  - `selenium`
  - `pytest`
  - `pytest-html` (for HTML reports).[web:19]

Install dependencies (example):

