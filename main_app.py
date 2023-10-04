from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
from downloader import download_file
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInfo, QWebEngineUrlRequestInterceptor
from PyQt5.QtWidgets import QApplication
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # Create a browser widget
        self.browser = QWebEngineView()


        # Create buttons with icons for each website
        self.pmt_button = QPushButton()
        self.pmt_button.setIcon(QIcon("imgs\PMT.png"))  # Set the icon image
        self.pmt_button.setFixedSize(128, 64) 
        self.pmt_button.setIconSize(QSize(128, 64)) 
        self.pmt_button.clicked.connect(lambda: self.load_website("https://www.physicsandmathstutor.com/"))

        self.cie_button = QPushButton()
        
        self.cie_button.setIcon(QIcon("imgs\CIENOTE.png"))
        self.cie_button.setFixedSize(128, 64) 
        self.cie_button.setIconSize(QSize(128, 64)) 
        
        self.cie_button.clicked.connect(lambda: self.load_website("https://pastpapers.papacambridge.com/"))

       
        self.Title = QLabel()
        self.Title.setText("Title")

    
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.pmt_button)
        self.button_layout.addWidget(self.cie_button)
        
    
        self.button = QPushButton("Download Paper")
        self.button.clicked.connect(self.get_file_path)
  
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)

    
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.button)

     
        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    

    
    def get_file_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directory = QFileDialog.getExistingDirectory(self, "Choose Save Directory", options=options)
        if (directory):
            current_url = self.browser.url().toString()
    
            download_file(current_url,directory)
            QMessageBox.information(None, "Success", "File downloaded successfully")

    def load_website(self, url):
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName("All In One Downloader")
window = MyApp()

window.resize(1280,720)
window.show()
app.exec_()
