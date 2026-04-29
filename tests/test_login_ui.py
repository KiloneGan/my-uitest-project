import os
from playwright.sync_api import Page, expect


def test_login_success(page: Page, base_url: str) -> None:
    """
    登录成功用例（可通过环境变量覆盖定位器和断言目标）：
    - LOGIN_USERNAME_SELECTOR
    - LOGIN_PASSWORD_SELECTOR
    - LOGIN_SUBMIT_SELECTOR
    - LOGIN_SUCCESS_SELECTOR
    - LOGIN_SUCCESS_TEXT
    - LOGIN_USERNAME
    - LOGIN_PASSWORD
    """
    username_selector = os.getenv("LOGIN_USERNAME_SELECTOR", "input[name='username']")
    password_selector = os.getenv("LOGIN_PASSWORD_SELECTOR", "input[type='password']")
    submit_selector = os.getenv("LOGIN_SUBMIT_SELECTOR", "button[type='submit']")
    success_selector = os.getenv("LOGIN_SUCCESS_SELECTOR", ".main-container, .layout, #app")
    success_text = os.getenv("LOGIN_SUCCESS_TEXT", "")

    username = os.getenv("LOGIN_USERNAME", "your_username")
    password = os.getenv("LOGIN_PASSWORD", "your_password")

    page.goto(base_url)
    page.fill(username_selector, username)
    page.fill(password_selector, password)
    page.click(submit_selector)

    if success_text:
        expect(page.get_by_text(success_text)).to_be_visible()
    else:
        expect(page.locator(success_selector).first).to_be_visible()


def test_login_failed_with_wrong_password(page: Page, base_url: str) -> None:
    """
    登录失败用例，默认断言出现“错误提示元素”。
    可通过以下环境变量覆盖：
    - LOGIN_USERNAME_SELECTOR
    - LOGIN_PASSWORD_SELECTOR
    - LOGIN_SUBMIT_SELECTOR
    - LOGIN_ERROR_SELECTOR
    - LOGIN_USERNAME
    """
    username_selector = os.getenv("LOGIN_USERNAME_SELECTOR", "input[name='username']")
    password_selector = os.getenv("LOGIN_PASSWORD_SELECTOR", "input[type='password']")
    submit_selector = os.getenv("LOGIN_SUBMIT_SELECTOR", "button[type='submit']")
    error_selector = os.getenv(
        "LOGIN_ERROR_SELECTOR",
        ".el-message--error, .ant-message-error, .error, [role='alert']",
    )

    username = os.getenv("LOGIN_USERNAME", "your_username")

    page.goto(base_url)
    page.fill(username_selector, username)
    page.fill(password_selector, "wrong_password_123")
    page.click(submit_selector)
    expect(page.locator(error_selector).first).to_be_visible()
