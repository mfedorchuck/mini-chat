from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver

import sys
from PyQt5 import QtWidgets
from src.design import window


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.protocol = self

    def lineReceived(self, line):
        message = line.decode()
        self.factory.window.plainTextEdit.appendPlainText(message)


class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol = Client

    def __init__(self, app_window):
        self.window = app_window


class ChatWindow(QtWidgets.QMainWindow, window.Ui_MainWindow):
    protocol: Client
    reactor = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self):
        self.pushButton.clicked.connect(self.send_message)

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)

    def send_message(self):
        message = self.lineEdit.text()

        self.protocol.sendLine(message.encode())
        self.lineEdit.setText("")

app = QtWidgets.QApplication(sys.argv)

import qt5reactor

window = ChatWindow
window.show()

qt5reactor.install()

from twisted.internet import reactor
reactor.connectTCP(
    "localhost",
    7410,
    Connector(window)
)

window.reactor = reactor
reactor.run()
