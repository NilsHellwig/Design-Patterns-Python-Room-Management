class AuthenticationStrategy:
    def __init__(self):
        self.database = {"abc12345": "12345678", "def56789": "abcdefgh"}

    def authenticate(self, username, password):
        raise NotImplementedError()


class RZAccountStrategy(AuthenticationStrategy):
    def authenticate(self, username, password):
        if not(username in self.database):
            raise ValueError("Username not available!")
        if self.database[username] == password:
            return True
        return False


class RZAccountStrategyTwoFactor(AuthenticationStrategy):
    def authenticate(self, username, password):
        if not(username in self.database):
            raise ValueError("Username not available!")
        if self.database[username] == password:
            # Imagine you have received a code by mail. since this logic is not implemented, any code can be entered here for demonstration purposes.
            security_code = input("Bitte geben Sie den Code ein, den Sie per Mail erhalten haben: ")
            print("Sie haben sich erfolgreich registriert.")
            return True
        return False
