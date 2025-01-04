# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableView, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1628, 871)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_table = QWidget(self.centralwidget)
        self.widget_table.setObjectName(u"widget_table")
        self.verticalLayout = QVBoxLayout(self.widget_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_table)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_table)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_10 = QRadioButton(self.widget_2)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout.addWidget(self.radioButton_10, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.widget_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 0, 6, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 0, 9, 1, 1)

        self.radioButton_9 = QRadioButton(self.widget_2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout.addWidget(self.radioButton_9, 0, 2, 1, 1)

        self.radioButton_7 = QRadioButton(self.widget_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 0, 4, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 0, 5, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 0, 7, 1, 1)

        self.radioButton_8 = QRadioButton(self.widget_2)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 0, 3, 1, 1)

        self.radioButton_4 = QRadioButton(self.widget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 0, 8, 1, 1)

        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.widget_2)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout.addWidget(self.radioButton_11, 1, 2, 1, 1)

        self.radioButton_12 = QRadioButton(self.widget_2)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout.addWidget(self.radioButton_12, 1, 3, 1, 1)

        self.radioButton_13 = QRadioButton(self.widget_2)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout.addWidget(self.radioButton_13, 1, 4, 1, 1)

        self.radioButton_14 = QRadioButton(self.widget_2)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout.addWidget(self.radioButton_14, 1, 5, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.tbvFunds = QTableView(self.widget_table)
        self.tbvFunds.setObjectName(u"tbvFunds")

        self.verticalLayout.addWidget(self.tbvFunds)


        self.horizontalLayout_2.addWidget(self.widget_table)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(200, 0))
        self.widget_4.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.widget_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout_2.addWidget(self.widget_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1628, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5411\u7b5b\u9009\u8bcd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u7b5b\u9009\u8bcd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u8fd1\u4e00\u5468", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8fd12\u5e74", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7acb\u6765", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u6708", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u8fd16\u6708", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u5e74", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u5e74", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u6708", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u5e74\u6765", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u91d1\u7c7b\u578b", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u7533\u8d2d\u72b6\u6001", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\u8d4e\u56de\u72b6\u6001", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f00\u653e\u65e5", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7d2f\u8ba1\u9650\u5b9a\u91d1\u989d", None))
    # retranslateUi

