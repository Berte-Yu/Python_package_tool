# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uart_data_handler_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        #MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        #MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_display.setGeometry(QtCore.QRect(10, 140, 581, 151))
        self.textBrowser_display.setObjectName("textBrowser_display")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_CMD = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_CMD.setObjectName("lineEdit_CMD")
        self.gridLayout.addWidget(self.lineEdit_CMD, 0, 1, 1, 1)
        self.pushButton_Left = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Left.setObjectName("pushButton_Left")
        self.gridLayout.addWidget(self.pushButton_Left, 0, 2, 1, 1)
        self.pushButton_Right = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Right.setObjectName("pushButton_Right")
        self.gridLayout.addWidget(self.pushButton_Right, 0, 3, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_del = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.gridLayout.addWidget(self.pushButton_del, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 2, 4, 1, 1)
        self.lineEdit_para_type = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_para_type.setObjectName("lineEdit_para_type")
        self.gridLayout.addWidget(self.lineEdit_para_type, 1, 1, 1, 3)
        self.lineEdit_Para_data = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Para_data.setObjectName("lineEdit_Para_data")
        self.gridLayout.addWidget(self.lineEdit_Para_data, 2, 1, 1, 3)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据包组合工具"))
        self.label.setText(_translate("MainWindow", "命令字节"))
        self.pushButton_Left.setText(_translate("MainWindow", "前进"))
        self.pushButton_Right.setText(_translate("MainWindow", "后退"))
        self.pushButton_add.setText(_translate("MainWindow", "添加"))
        self.label_3.setText(_translate("MainWindow", "参数类型"))
        self.pushButton_del.setText(_translate("MainWindow", "删除"))
        self.label_2.setText(_translate("MainWindow", "参数数据"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))

