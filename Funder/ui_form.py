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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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

        self.leIncludeWords = QLineEdit(self.widget)
        self.leIncludeWords.setObjectName(u"leIncludeWords")

        self.horizontalLayout.addWidget(self.leIncludeWords)

        self.btnCleanIncludeWords = QPushButton(self.widget)
        self.btnCleanIncludeWords.setObjectName(u"btnCleanIncludeWords")

        self.horizontalLayout.addWidget(self.btnCleanIncludeWords)

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

        self.leExcludeWords = QLineEdit(self.widget)
        self.leExcludeWords.setObjectName(u"leExcludeWords")

        self.horizontalLayout.addWidget(self.leExcludeWords)

        self.btnCleanExcludeWords = QPushButton(self.widget)
        self.btnCleanExcludeWords.setObjectName(u"btnCleanExcludeWords")

        self.horizontalLayout.addWidget(self.btnCleanExcludeWords)


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

        self.cbT1Premium = QCheckBox(self.widget_2)
        self.cbT1Premium.setObjectName(u"cbT1Premium")

        self.gridLayout.addWidget(self.cbT1Premium, 2, 6, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.tbvFunds = QTableView(self.widget_table)
        self.tbvFunds.setObjectName(u"tbvFunds")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setUnderline(False)
        self.tbvFunds.setFont(font3)
        self.tbvFunds.setStyleSheet(u"")
        self.tbvFunds.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbvFunds.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tbvFunds)


        self.horizontalLayout_2.addWidget(self.widget_table)

        self.mwFundDetail = QWidget(self.centralwidget)
        self.mwFundDetail.setObjectName(u"mwFundDetail")
        self.mwFundDetail.setMinimumSize(QSize(250, 0))
        self.mwFundDetail.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.mwFundDetail)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saFundDetail = QScrollArea(self.mwFundDetail)
        self.saFundDetail.setObjectName(u"saFundDetail")
        self.saFundDetail.setWidgetResizable(True)
        self.saFundDetail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.sawFundInfo = QWidget()
        self.sawFundInfo.setObjectName(u"sawFundInfo")
        self.sawFundInfo.setGeometry(QRect(0, 0, 348, 794))
        self.verticalLayout_3 = QVBoxLayout(self.sawFundInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wFundBaseInfo = QWidget(self.sawFundInfo)
        self.wFundBaseInfo.setObjectName(u"wFundBaseInfo")
        self.verticalLayout_4 = QVBoxLayout(self.wFundBaseInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.wFundBaseInfo)

        self.widget_8 = QWidget(self.sawFundInfo)
        self.widget_8.setObjectName(u"widget_8")
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 58, 16))

        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_4 = QWidget(self.sawFundInfo)
        self.widget_4.setObjectName(u"widget_4")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 0, 58, 16))
        self.tableWidget_3 = QTableWidget(self.widget_4)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 20, 261, 151))

        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.sawFundInfo)
        self.widget_3.setObjectName(u"widget_3")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 0, 58, 16))
        self.tableWidget_4 = QTableWidget(self.widget_3)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(10, 20, 261, 151))

        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.sawFundInfo)
        self.widget_5.setObjectName(u"widget_5")
        self.tableWidget_2 = QTableWidget(self.widget_5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 20, 261, 151))
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 58, 16))

        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.sawFundInfo)
        self.widget_6.setObjectName(u"widget_6")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 58, 16))
        self.tableWidget = QTableWidget(self.widget_6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 30, 261, 151))

        self.verticalLayout_3.addWidget(self.widget_6)

        self.saFundDetail.setWidget(self.sawFundInfo)

        self.verticalLayout_2.addWidget(self.saFundDetail)


        self.horizontalLayout_2.addWidget(self.mwFundDetail)

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
        self.btnCleanIncludeWords.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u7b5b\u9009\u8bcd", None))
        self.btnCleanExcludeWords.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
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
        self.cbT1Premium.setText(QCoreApplication.translate("MainWindow", u"T-1\u6ea2\u4ef7\u7387", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u9669", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4e70\u5165/\u5356\u51fa\u89c4\u5219", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6301\u4ed3\u7c7b\u578b\u5360\u6bd4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6301\u4ed3\u80a1\u7968\u5360\u6bd4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76c8\u5229\u6982\u7387", None))
    # retranslateUi

