import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class GmailBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gmail Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Set up the WebView and load Gmail
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://mail.google.com"))

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Full-screen on launch
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = GmailBrowser()
    browser.show()
    sys.exit(app.exec_())
