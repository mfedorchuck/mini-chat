from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver


class Handler(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)
        print("Disconnected")
        for user in self.factory.clients:
            if user is not self:
                user.sendLine(f"User: {self.login} leave chat".encode())

    def connectionMade(self):
        self.login = None
        self.factory.clients.append(self)
        print("Connected")

    def lineReceived(self, line: bytes):
        message = line.decode()

        if self.login:
            message = f"<{self.login}>: {message}"

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(message.encode())

        else:
            if message.startswith("login:"):
                login = message.replace("login:", "")
                self.login = login
                print(f"New user: {login}")
                self.sendLine(f"Welcome {login}!".encode())
                for user in self.factory.clients:
                    if user is not self:
                        user.sendLine(f"New user: {login} joined chat".encode())

            else:
                self.sendLine("Login setup failed 🙁".encode())


class Server(ServerFactory):
    protocol = Handler
    clients: list

    def __init__(self):
        self.clients = []

    def startFactory(self):
        print("Server started....")


reactor.listenTCP(7410, Server())
reactor.run()
