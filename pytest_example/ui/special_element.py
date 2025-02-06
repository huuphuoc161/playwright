# UI Testing Spacial Case



from playwright.sync_api import Page, expect

# Dynamic ID
def test_dynamic_id_example(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamicid")
    dynamic_id_button = page.get_by_role("button", name="Button with Dynamic ID")
    expect(dynamic_id_button).to_be_visible()
    dynamic_id_button.click()

# Elements have the same attribute class

def test_attribute_class_example(page: Page):
    page.goto("http://www.uitestingplayground.com/classattr")
    # primary_button = page.locator("//button[@class='btn class2 btn-primary btn-test']")
    primary_button = page.locator("button.btn-primary")
    expect(primary_button).to_be_visible()
    primary_button.click()

    page.goto("https://sellercenter.lazada.vn/apps/seller/login")
    # page.locator("//button[@type='submit']").click()
    page.locator("//button[contains(@class, 'next-btn-primary')]")
    # page.locator("button.login-button").click()

# Test example: Element hidden

def test_hiden_layer_example(page: Page):
    page.goto("http://www.uitestingplayground.com/hiddenlayers")
    green_button = page.locator("//button[@id='greenButton']")
    # green_button = page.locator("button.btn-success")
    green_button.click()
    # green_button.click(timeout=1000)
    blue_button = page.locator("//button[@id='blueButton']")
    blue_button.click()
