from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_policy_button = page.get_by_text("policy", exact=False)
        self.option_menu_industries = page.locator("#menu-item-4871")
        self.option_submenu_retirement_and_wealth = page.locator('[title="Retirement and wealth"]')

    def accept_policy_if_needed(self):
        policy_found = False
        cookies = self.page.context.cookies()
        policy_cookie = next(
            (cookie for cookie in cookies if "policy" in cookie["name"].lower()), 
            None
        )
        if policy_cookie:
            policy_found = True

        local_policy = self.page.evaluate("localStorage.getItem('policyAccepted')")
        if local_policy:
            policy_found = True

        session_policy = self.page.evaluate("sessionStorage.getItem('policyAccepted')")
        if session_policy:
            policy_found = True

        if policy_found and self.accept_policy_button.count() > 0:
            self.accept_policy_button.click()
            self.page.wait_for_timeout(1000)
        else:
            print("No policy acceptance required")

    def select_option_menu_retirement_and_wealth(self):
        self.option_menu_industries.hover()
        self.option_submenu_retirement_and_wealth.scroll_into_view_if_needed()
        self.option_submenu_retirement_and_wealth.click(force=True)

