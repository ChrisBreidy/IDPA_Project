import sys

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog

#Below array contains the xml docs paths after browsing
xmlDocumentsPaths = []

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self) # Load the .ui file

        self.browseSeq1 = self.findChild(QtWidgets.QPushButton, 'browseSeq1') # Find seq1 button
        self.browseSeq1.clicked.connect(self.browseSequenceOnePressed)

        self.browseSeq2 = self.findChild(QtWidgets.QPushButton, 'browseSeq2')  # Find seq2 button
        self.browseSeq2.clicked.connect(self.browseSequenceTwoPressed)

        self.calculateED = self.findChild(QtWidgets.QPushButton, 'calculateED')  # Find ED button
        self.calculateED.clicked.connect(self.calculateEditDistPressed)

        self.calculateES = self.findChild(QtWidgets.QPushButton, 'calculateES')  # Find ED button
        self.calculateES.clicked.connect(self.calculateEditScriptPressed)

        self.patchSeq1 = self.findChild(QtWidgets.QPushButton, 'patchSeq1')  # Find ED button
        self.patchSeq1.clicked.connect(self.patchSequenceOnePressed)

        self.patchSeq2 = self.findChild(QtWidgets.QPushButton, 'patchSeq2')  # Find ED button
        self.patchSeq2.clicked.connect(self.patchSequenceTwoPressed)

        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setFixedSize(753,648)
        self.show()

    def browseSequenceOnePressed(self):
        # This is executed when the button is pressed
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'C:/Users/Chris/Desktop', "XML Files (*.xml)")
        temp = fname[0]
        xmlDocumentsPaths.append(temp)


    def browseSequenceTwoPressed(self):
        # This is executed when the button is pressed
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'C:/Users/Chris/Desktop', "XML Files (*.xml)")
        temp = fname[0]
        xmlDocumentsPaths.append(temp)


    def calculateEditDistPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')

    def calculateEditScriptPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')

    def patchSequenceOnePressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')

    def patchSequenceTwoPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()