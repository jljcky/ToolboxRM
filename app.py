import sys
from PyQt5 import QtCore, QtGui, QtSvg

from PyQt5.QtWidgets import *
import delete_toolbox

class ToolboxRMWindow(QMainWindow):
    def __init__(self, w: int = 800, h: int = 600):
        super().__init__()
        self.title = "ToolboxRM"
        self.setWindowTitle(self.title)
        self.centerWindow(w, h)
        self.setFixedSize(w, h)
    
    def centerWindow(self, w: int, h: int):
        windowRect = QtCore.QRect(0, 0, w, h)
        centerPoint = QDesktopWidget().availableGeometry().center()

        windowRect.moveCenter(centerPoint)
        self.setGeometry(windowRect)
        self.setWindowIcon(QtGui.QIcon('./assets/ToolboxRMIcon.svg'))

class StartupWindow(ToolboxRMWindow):
    def __init__(self):
        super().__init__(400, 350)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        icon = QLabel(self)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        icon.setPixmap(QtGui.QIcon("./assets/ToolboxRMIcon.svg").pixmap(QtCore.QSize(192,192)))

        brand = QLabel(self)
        brand.setAlignment(QtCore.Qt.AlignCenter)
        brand.setPixmap(QtGui.QIcon("./assets/ToolboxRMLabel.svg").pixmap(QtCore.QSize(256,256)))

        versionNum = QLabel("Version 1.0-alpha2", self)
        versionNum.setAlignment(QtCore.Qt.AlignCenter)
        versionNum.setFont(QtGui.QFont("Arial", 12))

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(icon)
        vbox.addWidget(brand)
        vbox.addWidget(versionNum)
        vbox.addStretch()
        
        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

class WarningWindow(ToolboxRMWindow):
    def __init__(self):
        super().__init__(400, 150)

        warning = QLabel("Proceed?", self)
        warning.setAlignment(QtCore.Qt.AlignCenter)
        warning.setFont(QtGui.QFont("Verdana", 36, QtGui.QFont.Bold))
        
        proceed = QPushButton(self)
        proceed.setText("Proceed")
        proceed.setFont(QtGui.QFont("Arial", 12))

        cancel = QPushButton(self)
        cancel.setText("Cancel")
        cancel.setFont(QtGui.QFont("Arial", 12))

        proceedbox = QHBoxLayout()
        proceedbox.addStretch()
        proceedbox.addWidget(proceed)
        proceedbox.addStretch()
        proceedbox.addWidget(cancel)
        proceedbox.addStretch()

        proceedsection = QWidget()
        proceedsection.setLayout(proceedbox)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(warning)
        vbox.addStretch()
        vbox.addWidget(proceedsection)
        vbox.addStretch()

        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)


class FailWindow(ToolboxRMWindow):
    def __init__(self, message="Looks like something is wrong. Try again."):
        super().__init__()

        icon = QLabel(self)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        icon.setPixmap(QtGui.QIcon("./assets/ToolboxRMIcon.svg").pixmap(QtCore.QSize(192,192)))

        brand = QLabel(self)
        brand.setAlignment(QtCore.Qt.AlignCenter)
        brand.setPixmap(QtGui.QIcon("./assets/ToolboxRMLabel.svg").pixmap(QtCore.QSize(256,256)))

        versionNum = QLabel("Version 1.0-alpha2", self)
        versionNum.setAlignment(QtCore.Qt.AlignCenter)
        versionNum.setFont(QtGui.QFont("Arial", 12))

        complete = QLabel("FAIL!", self)
        complete.setAlignment(QtCore.Qt.AlignCenter)
        complete.setFont(QtGui.QFont("Verdana", 72, QtGui.QFont.Bold))
        complete.setStyleSheet("QLabel { color : #dd0000}")

        finishingMsg = QLabel(message, self)
        finishingMsg.setAlignment(QtCore.Qt.AlignCenter)
        finishingMsg.setFont(QtGui.QFont("Arial", 16))

        vbox = QVBoxLayout()
        vbox.addWidget(icon)
        vbox.addWidget(brand)
        vbox.addWidget(versionNum)
        vbox.addStretch()
        vbox.addWidget(complete)
        vbox.addStretch()
        vbox.addWidget(finishingMsg)
        vbox.addStretch()

        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

class CompleteWindow(ToolboxRMWindow):
    def __init__(self):
        super().__init__()

        icon = QLabel(self)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        icon.setPixmap(QtGui.QIcon("./assets/ToolboxRMIcon.svg").pixmap(QtCore.QSize(192,192)))

        brand = QLabel(self)
        brand.setAlignment(QtCore.Qt.AlignCenter)
        brand.setPixmap(QtGui.QIcon("./assets/ToolboxRMLabel.svg").pixmap(QtCore.QSize(256,256)))

        versionNum = QLabel("Version 1.0-alpha2", self)
        versionNum.setAlignment(QtCore.Qt.AlignCenter)
        versionNum.setFont(QtGui.QFont("Arial", 12))

        complete = QLabel("COMPLETE!", self)
        complete.setAlignment(QtCore.Qt.AlignCenter)
        complete.setFont(QtGui.QFont("Verdana", 72, QtGui.QFont.Bold))
        complete.setStyleSheet("QLabel { color : #dd0000}")

        finishingMsg = QLabel("Looks like it's done. Mission accomplished.", self)
        finishingMsg.setAlignment(QtCore.Qt.AlignCenter)
        finishingMsg.setFont(QtGui.QFont("Arial", 16))

        vbox = QVBoxLayout()
        vbox.addWidget(icon)
        vbox.addWidget(brand)
        vbox.addWidget(versionNum)
        vbox.addStretch()
        vbox.addWidget(complete)
        vbox.addStretch()
        vbox.addWidget(finishingMsg)
        vbox.addStretch()

        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

class MainWindow(ToolboxRMWindow):
    def __init__(self):
        super().__init__()

        icon = QLabel(self)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        icon.setPixmap(QtGui.QIcon("./assets/ToolboxRMIcon.svg").pixmap(QtCore.QSize(192,192)))

        brand = QLabel(self)
        brand.setAlignment(QtCore.Qt.AlignCenter)
        brand.setPixmap(QtGui.QIcon("./assets/ToolboxRMLabel.svg").pixmap(QtCore.QSize(256,256)))

        versionNum = QLabel("Version 1.0-alpha2", self)
        versionNum.setAlignment(QtCore.Qt.AlignCenter)
        versionNum.setFont(QtGui.QFont("Arial", 12))

        vbox = QVBoxLayout()
        vbox.addWidget(icon)
        vbox.addWidget(brand)
        vbox.addWidget(versionNum)
        vbox.addStretch()

        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

if __name__ == "__main__":
    app = QApplication([])
    start = StartupWindow()
    start.show()

    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(2000, loop.quit)
    loop.exec_()

    try:
        delete_toolbox.removeToolboxPlugins()
        delete_toolbox.removeToolboxIcons()
        result = CompleteWindow()
    except delete_toolbox.RobloxStudioNotFoundError:
        result = FailWindow("Can't find Roblox Studio.\nReinstall Roblox Studio and try again.")
    except delete_toolbox.RobloxStudioRibbonNotFoundError:
        result = FailWindow("Can't find RobloxStudioRibbon.xml in Roblox Studio.\nReinstall Roblox Studio and try again")

    start.hide()
    result.show()
    
    sys.exit(app.exec())