# import sys
# from PyQt5 import QtWidgets
# import src.gui.window as window
#
#
# class ExampleApp(QtWidgets.QMainWindow, window.Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#         self.pushButton.clicked.connect(self.submit_message)
#
#     def submit_message(self):
#         self.plainTextEdit.appendPlainText(
#             self.lineEdit.text()
#         )
#
#         self.lineEdit.clear()
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window = ExampleApp()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()