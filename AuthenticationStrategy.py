class AuthenticationStrategy:
    def __init__(self):
        # dummy data
        self.database = {"abc12345": "12345678", "def56789": "abcdefgh"}

    def authenticate(self, username, password):
        raise NotImplementedError()


class LoginAccountStrategy(AuthenticationStrategy):
    def authenticate(self, username, password):
        if not(username in self.database):
            raise ValueError("Username not available!")
        if self.database[username] == password:
            self.registered_user = username
            return True
        return False


class LoginAccountStrategyTwoFactor(AuthenticationStrategy):
    def authenticate(self, username, password):
        if not(username in self.database):
            raise ValueError("Username not available!")
        if self.database[username] == password:
            # Imagine you have received a code by mail. Since this logic is not implemented, any code can be entered here for demonstration purposes.
            security_code = input("Please enter the code you received by mail: ")
            print("You have successfully registered.")
            self.registered_user = username
            return True
        return False
