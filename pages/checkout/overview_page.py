from pages.checkout.confirmation_page import ConfirmationPage


class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator('#finish')

    def confirm_purchase(self):
        self.finish_button.click()
        return ConfirmationPage(self.page)
