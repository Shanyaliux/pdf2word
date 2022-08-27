import os
import threading
from PyQt5 import QtWidgets, QtCore
from Ui_MainWindow import Ui_MainWindow
from pdf2docx import Converter
from PyQt5.QtWidgets import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


        self.startButton.setEnabled(False)
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setFormat('%v\%m')


        # 绑定点击事件
        self.selectFilesButton.clicked.connect(self.openFilesDialog)
        self.selectOutputButton.clicked.connect(self.openOutputPath)
        self.startButton.clicked.connect(self.startConvert)


    def openFilesDialog(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, "选择PDF文件", r"./", "PDF文件(*.pdf)")
        if len(self.files) != 0:
            self.filesPathEditText.setText("\n".join(self.files))
            self.startButton.setEnabled(True)
            self.outputPath = os.path.dirname(self.files[0])
            self.outputPathEditText.setText(self.outputPath)


    def openOutputPath(self):
        self.outputPath = QFileDialog.getExistingDirectory(self, "选择文件夹", r"./")
        self.outputPathEditText.setText(self.outputPath)


    def startConvert(self):
        self.startButton.setEnabled(False)
        self.selectFilesButton.setEnabled(False)
        self.selectOutputButton.setEnabled(False)
        self.progressBar.setMaximum(len(self.files))
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
        self.pdf2docxThread = Pdf2docxThread()
        self.pdf2docxThread.setFilesAndOutputPath(self.files, self.outputPath)
        self.pdf2docxThread.progressBarValue.connect(self.progressbarSignal2Value)
        self.statusbar.showMessage("开始转换，请稍后……")
        # QMessageBox.information(self,'提示','开始转换，请稍后……', QMessageBox.Yes | QMessageBox.Yes)
        self.pdf2docxThread.start()
        

    def progressbarSignal2Value(self, i):
        self.progressBar.setValue(i)
        if i == len(self.files):
            self.startButton.setEnabled(True)
            self.selectFilesButton.setEnabled(True)
            self.selectOutputButton.setEnabled(True)
            self.statusbar.showMessage("转换完成", 5000)
            self.progressBar.setVisible(False)
            QMessageBox.information(self,'提示','转换完成', QMessageBox.Yes | QMessageBox.Yes)
            
            
    
        
class Pdf2docxThread (QtCore.QThread):   
    progressBarValue = QtCore.pyqtSignal(int)
    def __init__(self):
        super(Pdf2docxThread, self).__init__()
        
    def setFilesAndOutputPath(self, files, outputPath):
        self.files = files
        self.outputPath = outputPath

    def run(self):
        for count, pdf in enumerate(self.files, start=1):
            _, tempfilename = os.path.split(pdf)
            filename, _ = os.path.splitext(tempfilename)
            docxFile = os.path.join(self.outputPath, f'{filename}.docx')
            self.pdf2docx(pdf, docxFile)
            self.progressBarValue.emit(count)
        
    def pdf2docx(self, pdfFile, docxFile):
        # 创建转换实例（对象）
        cv = Converter(pdfFile)
        # 开始转换
        cv.convert(docxFile)
        # 转换完成，释放实例（对象）
        cv.close()





