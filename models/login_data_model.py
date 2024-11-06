class LoginDataModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_login_data(cls, variables, is_valid):
        user_type = 'standard' if is_valid else 'locked_out'

        return cls(
            variables['users'][user_type]['username'],
            variables['users'][user_type]['password']
        )