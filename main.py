
from ui_app import Ui_App
from ui_train import Window
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())

