from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_MainWindow import Ui_MainWindow
from MainWindow import MainWindow
import sys

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  app.setStyle("Fusion")  # 设置窗口风格
  MainWindow = MainWindow() # 创建窗体对象
  MainWindow.show() # 显示窗体
  sys.exit(app.exec_())
