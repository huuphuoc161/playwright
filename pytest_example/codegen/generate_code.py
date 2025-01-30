import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://thanhcaviet.net/")
    page.get_by_role("link", name="Jêsus Là Bạn Thật Ôi, Jêsus").click()
    page.get_by_text("+").nth(1).click()
    page.get_by_text("+").nth(1).click()
    page.get_by_text("+").nth(1).click()
    page.get_by_role("button", name="cột").click()
    page.get_by_role("button", name="cột").click()
