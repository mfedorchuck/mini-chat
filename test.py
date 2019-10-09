class Client:
    def __init__(self,  age: int, login: str):
        self.age = age
        self.login = login

    def show_info(self):
        return f"login: {self.login}, age: {self.age}"


class SuperClient(Client):
    colour: int = 100

    def show_info(self):
        all_str = super().show_info()
        print(f"{all_str} colour: {self.colour}")
