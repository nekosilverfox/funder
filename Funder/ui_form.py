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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1628, 871)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
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
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line)

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
        self.cb1Week = QCheckBox(self.widget_2)
        self.cb1Week.setObjectName(u"cb1Week")

        self.gridLayout.addWidget(self.cb1Week, 1, 1, 1, 1)

        self.cb6Month = QCheckBox(self.widget_2)
        self.cb6Month.setObjectName(u"cb6Month")

        self.gridLayout.addWidget(self.cb6Month, 1, 4, 1, 1)

        self.cb1Year = QCheckBox(self.widget_2)
        self.cb1Year.setObjectName(u"cb1Year")

        self.gridLayout.addWidget(self.cb1Year, 1, 5, 1, 1)

        self.cb2Year = QCheckBox(self.widget_2)
        self.cb2Year.setObjectName(u"cb2Year")

        self.gridLayout.addWidget(self.cb2Year, 1, 6, 1, 1)

        self.cbThisYear = QCheckBox(self.widget_2)
        self.cbThisYear.setObjectName(u"cbThisYear")

        self.gridLayout.addWidget(self.cbThisYear, 1, 8, 1, 1)

        self.cbFromSetup = QCheckBox(self.widget_2)
        self.cbFromSetup.setObjectName(u"cbFromSetup")

        self.gridLayout.addWidget(self.cbFromSetup, 1, 9, 1, 1)

        self.cbCanBuy = QCheckBox(self.widget_2)
        self.cbCanBuy.setObjectName(u"cbCanBuy")

        self.gridLayout.addWidget(self.cbCanBuy, 2, 2, 1, 1)

        self.cb3Year = QCheckBox(self.widget_2)
        self.cb3Year.setObjectName(u"cb3Year")

        self.gridLayout.addWidget(self.cb3Year, 1, 7, 1, 1)

        self.cbDayQuota = QCheckBox(self.widget_2)
        self.cbDayQuota.setObjectName(u"cbDayQuota")

        self.gridLayout.addWidget(self.cbDayQuota, 2, 5, 1, 1)

        self.cb3Month = QCheckBox(self.widget_2)
        self.cb3Month.setObjectName(u"cb3Month")

        self.gridLayout.addWidget(self.cb3Month, 1, 3, 1, 1)

        self.cbFundType = QCheckBox(self.widget_2)
        self.cbFundType.setObjectName(u"cbFundType")

        self.gridLayout.addWidget(self.cbFundType, 2, 1, 1, 1)

        self.cbCanSale = QCheckBox(self.widget_2)
        self.cbCanSale.setObjectName(u"cbCanSale")

        self.gridLayout.addWidget(self.cbCanSale, 2, 3, 1, 1)

        self.cbNextOpenDay = QCheckBox(self.widget_2)
        self.cbNextOpenDay.setObjectName(u"cbNextOpenDay")

        self.gridLayout.addWidget(self.cbNextOpenDay, 2, 4, 1, 1)

        self.cb1Month = QCheckBox(self.widget_2)
        self.cb1Month.setObjectName(u"cb1Month")

        self.gridLayout.addWidget(self.cb1Month, 1, 2, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 2, 9, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.tbvFunds = QTableView(self.widget_table)
        self.tbvFunds.setObjectName(u"tbvFunds")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setUnderline(False)
        self.tbvFunds.setFont(font3)
        self.tbvFunds.setStyleSheet(u"")

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6839\u636e\u57fa\u91d1\u540d\u79f0\u8fdb\u884c\u7b5b\u9009\uff08\u7b5b\u9009\u8bcd\u4f7f\u7528\u7a7a\u683c\u8fdb\u884c\u5206\u9694\uff09", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5411\u7b5b\u9009\u8bcd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u7b5b\u9009\u8bcd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.cb1Week.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u5468 (%)", None))
        self.cb6Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd16\u6708 (%)", None))
        self.cb1Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u5e74 (%)", None))
        self.cb2Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd12\u5e74 (%)", None))
        self.cbThisYear.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u5e74\u6765 (%)", None))
        self.cbFromSetup.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7acb\u6765 (%)", None))
        self.cbCanBuy.setText(QCoreApplication.translate("MainWindow", u"\u7533\u8d2d\u72b6\u6001", None))
        self.cb3Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u5e74 (%)", None))
        self.cbDayQuota.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7d2f\u8ba1\u9650\u5b9a\u91d1\u989d", None))
        self.cb3Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u6708 (%)", None))
        self.cbFundType.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u91d1\u7c7b\u578b", None))
        self.cbCanSale.setText(QCoreApplication.translate("MainWindow", u"\u8d4e\u56de\u72b6\u6001", None))
        self.cbNextOpenDay.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f00\u653e\u65e5", None))
        self.cb1Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u6708 (%)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5171 N \u6761\u6570\u636e", None))
    # retranslateUi

