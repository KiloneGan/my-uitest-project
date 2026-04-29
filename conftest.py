import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "http://www.qzdatasoft.com:8084/gld/")


@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=200)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    page.set_default_timeout(15000)
    yield page
    context.close()
