class ConfirmationPage:
    def __init__(self, page):
        self.page = page
        self.confirmation_msg = page.locator('.complete-header')

    def get_confirmation_msg(self):
        return self.confirmation_msg.inner_text()