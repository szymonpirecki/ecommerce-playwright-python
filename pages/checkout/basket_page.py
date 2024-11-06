from pages.checkout.checkout_page import CheckoutPage


class BasketPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator('#checkout')

    def go_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)
