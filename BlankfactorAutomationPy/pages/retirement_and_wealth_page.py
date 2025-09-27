from config.constants import EXPECTED_TEXTS
from playwright.sync_api import Page

class RetirementAndWealthPage:
    def __init__(self, page: Page):
        self.page = page
        self.section_machine_learning = page.locator(
            ".card-text", has_text="AI & Machine learning"
        )
        self.last_card = page.locator(".card-text.small").last
        self.button_lets_get_started = page.locator(".hover-color-aqua")

    def scroll_to_powering_innovation_in_retirement_services(self):
        self.section_machine_learning.scroll_into_view_if_needed()
        self.section_machine_learning.hover()
        text_section_machine_learning = self.get_last_card_text()
        self.compare_texts(
            text_section_machine_learning,
            EXPECTED_TEXTS["CARD_AI_MACHINE_LEARNING"]
        )

    def select_option_menu_lets_get_started(self):
        self.button_lets_get_started.hover()
        self.button_lets_get_started.click()

    def get_last_card_text(self) -> str:
        return self.get_text_element(self.last_card)

    def get_text_element(self, locator) -> str:
        raw = locator.inner_text()
        return " ".join(raw.split()).strip()

    def compare_texts(self, actual: str, expected: str):
        normalized_actual = " ".join(actual.split()).strip()
        normalized_expected = " ".join(expected.split()).strip()
        if normalized_actual != normalized_expected:
            raise AssertionError(
                f"Texts do not match!\nExpected: {normalized_expected}\nActual:   {normalized_actual}"
            )
