from behave import given, when, then
from config.constants import BASE_URL, EXPECTED_TEXTS
from pages.home_page import HomePage
from pages.retirement_and_wealth_page import RetirementAndWealthPage
from pages.contact_page import ContactPage


@given("user opens the URL")
def step_open_url(context):
    context.page.goto(BASE_URL)


@given("user navigates to Industries and opens the Retirement and Wealth section")
def step_navigate_retirement_section(context):
    context.home_page = HomePage(context.page)
    context.retirement_and_wealth = RetirementAndWealthPage(context.page)
    context.contact_page = ContactPage(context.page)
    context.home_page.accept_policy_if_needed()
    context.home_page.select_option_menu_retirement_and_wealth()
    context.retirement_and_wealth.scroll_to_powering_innovation_in_retirement_services()


@when("user clicks on the Let's get started button")
def step_click_lets_get_started(context):
    context.retirement_and_wealth.select_option_menu_lets_get_started()


@then("user verifies the page URL and the title")
def step_verify_url_and_title(context):
    current_url = context.page.url
    title_page = context.contact_page.get_text_title()

    normalized_title = " ".join(title_page.split()).strip()
    normalized_expected_title = " ".join(EXPECTED_TEXTS["TITLE_CONTACT_PAGE"].split()).strip()

    assert current_url == EXPECTED_TEXTS["TEXT_URL_EXPECTED"], \
        f"Expected URL: {EXPECTED_TEXTS['TEXT_URL_EXPECTED']}, but got: {current_url}"

    assert normalized_title == normalized_expected_title, \
        f"Expected title: {normalized_expected_title}, but got: {normalized_title}"
