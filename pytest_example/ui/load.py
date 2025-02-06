from playwright.sync_api import Page, expect

# load delay until element is ready
def test_load_delay_example(page: Page):
    page.goto("https://katalon.com/katalon-platform")
    page.locator("//button[@id='onetrust-accept-btn-handler']").click()
    onboarding_hub_link = page.get_by_role("link", name = "Onboarding Hub")
    onboarding_hub_link.scroll_into_view_if_needed(timeout=5000)
    onboarding_hub_link.click()

    social_google = page.locator("//*[@id='social-google']")
    expect(social_google).to_be_visible(timeout=5000)
    social_google.click()

# wait for ajax data or data from backend

def test_wait_ajax_data_example(page: Page):
    page.goto("http://www.uitestingplayground.com/ajax")
    page.locator("//button[@id='ajaxButton']").click()
    success_message = page.locator("//p[@class='bg-success']")
    success_message.wait_for()
    expect(success_message).to_be_visible()

# Element change after an event

def test_element_change_after_event(page: Page):
    page.goto("http://www.uitestingplayground.com/click")
    bad_button = page.locator("//button[@id='badButton']")
    expect(bad_button).to_have_class("btn btn-primary")
    bad_button.click()
    expect(bad_button).to_have_class("btn btn-success")

    page.goto("http://www.uitestingplayground.com/textinput")
    page.locator("//input").fill("exanple")
    primary_btn = page.locator("button.btn-primary")
    expect(primary_btn).to_have_text("Button Change it's Name Based on Input Value")
    primary_btn.click()
    expect(primary_btn).to_have_text("exanple")