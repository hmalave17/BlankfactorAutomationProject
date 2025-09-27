from playwright.sync_api import Page
from pages.retirement_and_wealth_page import RetirementAndWealthPage

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.retirement_and_wealth = RetirementAndWealthPage(self.page)
        self.text_title = page.locator(".h1-5")

    def get_text_title(self) -> str:
        return self.retirement_and_wealth.get_text_element(self.text_title)