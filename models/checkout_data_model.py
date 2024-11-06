class CheckoutDataModel:
    def __init__(self, first_name, last_name, post_code):
        self.first_name = first_name
        self.last_name = last_name
        self.post_code = post_code

    @classmethod
    def get_checkout_data(cls, variables):
        return cls(
            variables['users']['standard']['first_name'],
            variables['users']['standard']['last_name'],
            variables['users']['standard']['post_code']
        )
