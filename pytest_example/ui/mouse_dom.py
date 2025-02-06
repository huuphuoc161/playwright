import time

from playwright.sync_api import Page, expect

def test_example_mouse_over(page: Page):
    page.goto("http://www.uitestingplayground.com/mouseover")
    hover_link = page.locator("//a[@title='Click me']")
    hover_link.hover()
    text_warming = page.locator("//a[@class='text-warning']")
    text_warming.click(click_count=4)
    expect(page.locator("//span[@id='clickCount']")).to_have_text("4")

# Non-breaking space
def test_example_non_breaking_space(page: Page):
    page.goto("http://www.uitestingplayground.com/nbsp")
    # page.locator("//button[text()='My Button']").click(timeout=2000)
    page.locator("//button[text()='My\u00A0Button']").click(timeout=2000)


# 15. Overlapped element
def test_example_overlapped_element(page: Page):
    page.goto("http://www.uitestingplayground.com/overlapped")
    name_text_bot = page.get_by_placeholder("Name")
    div = name_text_bot.locator("..")
    div.hover()
    page.mouse.wheel(0,200)
    name_text_bot.click()
    name_text_bot.fill("testExample")
    expect(name_text_bot).to_have_value("testExample")

# 16. Shadow DOM
# http://www.uitestingplayground.com/shadowdom
def test_example_shadown_dom(page: Page):
    page.goto("http://www.uitestingplayground.com/shadowdom")
    page.locator("guid-generator .edit-field").fill("1234567890")
    page.locator("guid-generator .button-generate").click(timeout=3000)
    page.locator("guid-generator .button-copy").click(timeout=3000)
    time.sleep(5)

    page.goto("https://books-pwakit.appspot.com/")
    page.locator("book-app[apptitle='BOOKS'] #input").fill("testExample")
    time.sleep(5)

# iframe example
def test_iframe_example(page: Page):
    # page.goto("https://ui.vision/demo/webtest/frames/")
    # textbox = page.frame_locator("//*[@src='frame_1.html']").locator('//input')
    # textbox.fill("testExample")
    # page.pause()

    page.goto("https://the-internet.herokuapp.com/iframe")
    page.locator("//body[@id='tinymce']").click(timeout=2000)
    email_textbox = page.frame_locator('//*[@id="mce_0_ifr"]').locator('//body')
    email_textbox.click(timeout=1500)
    email_textbox.fill(" testExample", timeout=1500)
    page.pause()
