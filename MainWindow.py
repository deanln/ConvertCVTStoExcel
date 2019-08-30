from PyQt4 import QtGui, QtCore
import convertToExcel, os, sys
import extractCanMessages
import GlobalVariables


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


dataTemplate = resource_path('dataTemplate.xlsx')
safranLogo = resource_path('safranlogo.png')
safranIco = resource_path('safranico.ico')

class MainGUI(QtGui.QMainWindow):
    def __init__(self):
        '''Initializes the main GUI for the entire software'''
        super(QtGui.QMainWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('safranico.ico'))
        self.setWindowTitle('CVTS CAN-NVM Data Parser ver1.0')
        self.setFixedSize(650,200)

        self.picture_label = QtGui.QLabel()  # Construct Logo/Title banner label for software
        self.picture_label.setAlignment(QtCore.Qt.AlignRight)
        self.picture_label.setPixmap(QtGui.QPixmap(safranLogo))

        self.leftColumn = QtGui.QVBoxLayout()  # Construct Left Layout
        self.rightColumn = QtGui.QVBoxLayout()  # Construct Right Layout
        self.frameBox = QtGui.QHBoxLayout()  # Construct Frame Layout
        self.outerFrameBox = QtGui.QVBoxLayout()  # Construct Outer Frame Layout

        self.frame1 = QtGui.QFrame()  # Construct Left Frame
        size_policy_left = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                             QtGui.QSizePolicy.Preferred)
        size_policy_left.setHorizontalStretch(3)
        self.frame1.setLayout(self.leftColumn)
        self.frame1.setSizePolicy(size_policy_left)

        self.frame2 = QtGui.QFrame()  # Construct Right Frame
        size_policy_right = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                              QtGui.QSizePolicy.Preferred)
        size_policy_right.setHorizontalStretch(5)
        self.frame2.setLayout(self.rightColumn)
        self.frame2.setSizePolicy(size_policy_right)

        self.outerframe = QtGui.QFrame()
        self.outerframe.setLayout(self.frameBox)

        self.statusbar = QtGui.QStatusBar()

        self.centralWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.outerFrameBox)
        self.outerFrameBox.setContentsMargins(0, 0, 0, 0)

        self.title_label = QtGui.QLabel("CVTS CAN-NVM Data Parser")
        self.fontSize = QtGui.QFont('Arial', 15, QtGui.QFont.Bold)
        self.title_label.setFont(self.fontSize)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        self.instruction_label = QtGui.QLabel("This application converts CVTS Flight Logs and parses CM_003\n"
                                              "CM_004, CM_007 messages from a valid CVTS flight log file into\n"
                                              "*.xlsx file (using CVTS CAN-NVM Data Parser V3.0 template)\n"
                                              "\nTo start conversion, press 'Convert'.")
        self.instruction_label.setAlignment(QtCore.Qt.AlignVCenter)

        self.convert_button = QtGui.QPushButton("Convert")
        self.convert_button.setStatusTip("Start conversion of CVTS flight log (*.txt to *.xlsx)")
        self.convert_button.clicked.connect(self.convertfile)

        self.frameBox.addWidget(self.frame1)
        self.frameBox.addWidget(self.frame2)

        self.outerFrameBox.addWidget(self.outerframe)
        self.outerFrameBox.addWidget(self.horizontalLine())

        self.leftColumn.addWidget(self.picture_label)
        self.leftColumn.addWidget(self.title_label)
        self.rightColumn.addWidget(self.instruction_label)
        self.rightColumn.addWidget(self.convert_button)

        self.menubar = QtGui.QMenuBar()
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fileMenu = self.menubar.addMenu('&Help')
        self.about_action = QtGui.QAction("&About", self)
        self.about_action.setStatusTip("Developer Contact Information")
        self.about_action.triggered.connect(self.aboutDialog)
        self.fileMenu.addAction(self.about_action)

        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

    def convertfile(self):
        try:
            filetoparse = QtGui.QFileDialog.getOpenFileName(None, 'Select Flight Log (*.txt)', '/', '*.txt')
            fileName = extractCanMessages.createDataList(filetoparse)
            convertToExcel.convertToExcel(dataTemplate, fileName)
            self.statusbar.showMessage('Converted successfully!')
        except IOError:
            self.statusbar.showMessage('No file found.')


    def aboutDialog(self):
        """When user presses the 'About' button, this function is executed. Creates an about dialog."""
        layout = QtGui.QVBoxLayout()
        aboutDialog = QtGui.QDialog()
        aboutDialog.setWindowTitle("Software Details")
        aboutDialog.setWindowIcon(QtGui.QIcon(safranIco))
        aboutDialog.setFixedSize(390, 280)
        layout.setContentsMargins(0, 0, 0, 15)

        boldFont = QtGui.QFont("Arial", 11, QtGui.QFont.Bold)
        ipFont = QtGui.QFont("Arial", 6, QtGui.QFont.Light)

        picture_label = QtGui.QLabel()  # Construct Logo/Title banner label for software
        picture_label.setAlignment(QtCore.Qt.AlignCenter)
        picture_label.setPixmap(QtGui.QPixmap(safranLogo))

        contact = "Developer Contact Information:"
        contact_info = "{}".format(GlobalVariables.CONTACT_INFO)
        name = "{}".format(GlobalVariables.SOFTWARE_NAME)
        version = "Version: {} (built on {})".format(GlobalVariables.SOFTWARE_VERSION, GlobalVariables.VERSION_DATE)
        pn = "Part Number: {}".format(GlobalVariables.SOFTWARE_PN)

        contact_label = QtGui.QLabel(contact)
        contact_label.setAlignment(QtCore.Qt.AlignCenter)
        contact_info_label = QtGui.QLabel(contact_info)
        contact_info_label.setAlignment(QtCore.Qt.AlignCenter)
        version_label = QtGui.QLabel(version)
        version_label.setAlignment(QtCore.Qt.AlignCenter)
        name_label = QtGui.QLabel(name)
        name_label.setFont(boldFont)
        name_label.setAlignment(QtCore.Qt.AlignCenter)
        pn_label = QtGui.QLabel(pn)
        pn_label.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(picture_label)
        layout.addWidget(self.horizontalLine())
        layout.addWidget(name_label)
        layout.addWidget(pn_label)
        layout.addWidget(version_label)
        layout.addWidget(self.horizontalLine())
        layout.addWidget(contact_label)
        layout.addWidget(contact_info_label)
        aboutDialog.setLayout(layout)
        aboutDialog.exec_()


    def horizontalLine(self):
        hline = QtGui.QFrame()
        hline.setFrameShape(QtGui.QFrame.HLine)
        hline.setFrameShadow(QtGui.QFrame.Sunken)
        return hline

if __name__ == '__main__':
    """Main program loop. Constructs background thread, creates main GUI object, and executes the program."""
    import sys
    app = QtGui.QApplication(sys.argv)

    w = MainGUI()
    w.show()
    sys.exit(app.exec_())