from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    browser_name = "chromium"
    headless_mode = False

    if browser_name == "firefox":
        browser_type = context.playwright.firefox
    elif browser_name in ["webkit", "safari"]:
        browser_type = context.playwright.webkit
    else:
        browser_type = context.playwright.chromium

    context.browser = browser_type.launch(headless=headless_mode)
    context.page = context.browser.new_page()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
