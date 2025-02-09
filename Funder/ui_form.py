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
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

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
        self.leIncludeWords_2 = QLineEdit(self.widget)
        self.leIncludeWords_2.setObjectName(u"leIncludeWords_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leIncludeWords_2.sizePolicy().hasHeightForWidth())
        self.leIncludeWords_2.setSizePolicy(sizePolicy)
        self.leIncludeWords_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.leIncludeWords_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

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
        self.cb3Year = QCheckBox(self.widget_2)
        self.cb3Year.setObjectName(u"cb3Year")

        self.gridLayout.addWidget(self.cb3Year, 1, 7, 1, 1)

        self.cbCanBuy = QCheckBox(self.widget_2)
        self.cbCanBuy.setObjectName(u"cbCanBuy")

        self.gridLayout.addWidget(self.cbCanBuy, 3, 2, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 3, 9, 1, 1)

        self.cb2Year = QCheckBox(self.widget_2)
        self.cb2Year.setObjectName(u"cb2Year")

        self.gridLayout.addWidget(self.cb2Year, 1, 6, 1, 1)

        self.cbCanSale = QCheckBox(self.widget_2)
        self.cbCanSale.setObjectName(u"cbCanSale")

        self.gridLayout.addWidget(self.cbCanSale, 3, 3, 1, 1)

        self.cb1Month = QCheckBox(self.widget_2)
        self.cb1Month.setObjectName(u"cb1Month")

        self.gridLayout.addWidget(self.cb1Month, 1, 2, 1, 1)

        self.cb1Week = QCheckBox(self.widget_2)
        self.cb1Week.setObjectName(u"cb1Week")

        self.gridLayout.addWidget(self.cb1Week, 1, 1, 1, 1)

        self.cbNextOpenDay = QCheckBox(self.widget_2)
        self.cbNextOpenDay.setObjectName(u"cbNextOpenDay")

        self.gridLayout.addWidget(self.cbNextOpenDay, 3, 4, 1, 1)

        self.cbDayQuota = QCheckBox(self.widget_2)
        self.cbDayQuota.setObjectName(u"cbDayQuota")

        self.gridLayout.addWidget(self.cbDayQuota, 3, 5, 1, 1)

        self.cb1Year = QCheckBox(self.widget_2)
        self.cb1Year.setObjectName(u"cb1Year")

        self.gridLayout.addWidget(self.cb1Year, 1, 5, 1, 1)

        self.cbThisYear = QCheckBox(self.widget_2)
        self.cbThisYear.setObjectName(u"cbThisYear")

        self.gridLayout.addWidget(self.cbThisYear, 1, 8, 1, 1)

        self.cbT1Premium = QCheckBox(self.widget_2)
        self.cbT1Premium.setObjectName(u"cbT1Premium")

        self.gridLayout.addWidget(self.cbT1Premium, 3, 6, 1, 1)

        self.cb3Month = QCheckBox(self.widget_2)
        self.cb3Month.setObjectName(u"cb3Month")

        self.gridLayout.addWidget(self.cb3Month, 1, 3, 1, 1)

        self.cbFundType = QCheckBox(self.widget_2)
        self.cbFundType.setObjectName(u"cbFundType")

        self.gridLayout.addWidget(self.cbFundType, 3, 1, 1, 1)

        self.cbFromSetup = QCheckBox(self.widget_2)
        self.cbFromSetup.setObjectName(u"cbFromSetup")

        self.gridLayout.addWidget(self.cbFromSetup, 1, 9, 1, 1)

        self.cb6Month = QCheckBox(self.widget_2)
        self.cb6Month.setObjectName(u"cb6Month")

        self.gridLayout.addWidget(self.cb6Month, 1, 4, 1, 1)


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
        self.wFundBaseInfo.setMinimumSize(QSize(0, 50))
        self.verticalLayout_4 = QVBoxLayout(self.wFundBaseInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.wFundBaseInfo)

        self.widget_8 = QWidget(self.sawFundInfo)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_9.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.barRisk = QProgressBar(self.widget_7)
        self.barRisk.setObjectName(u"barRisk")
        sizePolicy.setHeightForWidth(self.barRisk.sizePolicy().hasHeightForWidth())
        self.barRisk.setSizePolicy(sizePolicy)
        self.barRisk.setMaximum(0)
        self.barRisk.setValue(0)

        self.horizontalLayout_3.addWidget(self.barRisk)


        self.verticalLayout_9.addWidget(self.widget_7)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.tbvRisk = QTableView(self.sawFundInfo)
        self.tbvRisk.setObjectName(u"tbvRisk")

        self.verticalLayout_3.addWidget(self.tbvRisk)

        self.widget_4 = QWidget(self.sawFundInfo)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.barBuySaleRole = QProgressBar(self.widget_9)
        self.barBuySaleRole.setObjectName(u"barBuySaleRole")
        sizePolicy.setHeightForWidth(self.barBuySaleRole.sizePolicy().hasHeightForWidth())
        self.barBuySaleRole.setSizePolicy(sizePolicy)
        self.barBuySaleRole.setMaximum(0)
        self.barBuySaleRole.setValue(0)

        self.horizontalLayout_4.addWidget(self.barBuySaleRole)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.tbvBuySaleRole = QTableView(self.widget_4)
        self.tbvBuySaleRole.setObjectName(u"tbvBuySaleRole")

        self.verticalLayout_6.addWidget(self.tbvBuySaleRole)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.sawFundInfo)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.barHoldType = QProgressBar(self.widget_10)
        self.barHoldType.setObjectName(u"barHoldType")
        sizePolicy.setHeightForWidth(self.barHoldType.sizePolicy().hasHeightForWidth())
        self.barHoldType.setSizePolicy(sizePolicy)
        self.barHoldType.setMaximum(0)
        self.barHoldType.setValue(0)

        self.horizontalLayout_5.addWidget(self.barHoldType)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.tbvHoldType = QTableView(self.widget_3)
        self.tbvHoldType.setObjectName(u"tbvHoldType")

        self.verticalLayout_5.addWidget(self.tbvHoldType)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.sawFundInfo)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.lbReportTime = QLabel(self.widget_12)
        self.lbReportTime.setObjectName(u"lbReportTime")
        self.lbReportTime.setFont(font4)

        self.horizontalLayout_7.addWidget(self.lbReportTime)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.barHoldDetail = QProgressBar(self.widget_12)
        self.barHoldDetail.setObjectName(u"barHoldDetail")
        sizePolicy.setHeightForWidth(self.barHoldDetail.sizePolicy().hasHeightForWidth())
        self.barHoldDetail.setSizePolicy(sizePolicy)
        self.barHoldDetail.setMaximum(0)
        self.barHoldDetail.setValue(0)

        self.horizontalLayout_7.addWidget(self.barHoldDetail)


        self.verticalLayout_7.addWidget(self.widget_12)

        self.tbvHoldDetail = QTableView(self.widget_5)
        self.tbvHoldDetail.setObjectName(u"tbvHoldDetail")

        self.verticalLayout_7.addWidget(self.tbvHoldDetail)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.sawFundInfo)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.barProfit = QProgressBar(self.widget_11)
        self.barProfit.setObjectName(u"barProfit")
        sizePolicy.setHeightForWidth(self.barProfit.sizePolicy().hasHeightForWidth())
        self.barProfit.setSizePolicy(sizePolicy)
        self.barProfit.setMaximum(0)
        self.barProfit.setValue(0)

        self.horizontalLayout_6.addWidget(self.barProfit)


        self.verticalLayout_8.addWidget(self.widget_11)

        self.tbvProfit = QTableView(self.widget_6)
        self.tbvProfit.setObjectName(u"tbvProfit")

        self.verticalLayout_8.addWidget(self.tbvProfit)


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
        self.cb3Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u5e74 (%)", None))
        self.cbCanBuy.setText(QCoreApplication.translate("MainWindow", u"\u7533\u8d2d\u72b6\u6001", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5171 N \u6761\u6570\u636e", None))
        self.cb2Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd12\u5e74 (%)", None))
        self.cbCanSale.setText(QCoreApplication.translate("MainWindow", u"\u8d4e\u56de\u72b6\u6001", None))
        self.cb1Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u6708 (%)", None))
        self.cb1Week.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u5468 (%)", None))
        self.cbNextOpenDay.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f00\u653e\u65e5", None))
        self.cbDayQuota.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7d2f\u8ba1\u9650\u5b9a\u91d1\u989d", None))
        self.cb1Year.setText(QCoreApplication.translate("MainWindow", u"\u8fd11\u5e74 (%)", None))
        self.cbThisYear.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u5e74\u6765 (%)", None))
        self.cbT1Premium.setText(QCoreApplication.translate("MainWindow", u"T-1\u6ea2\u4ef7\u7387", None))
        self.cb3Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd13\u6708 (%)", None))
        self.cbFundType.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u91d1\u7c7b\u578b", None))
        self.cbFromSetup.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7acb\u6765 (%)", None))
        self.cb6Month.setText(QCoreApplication.translate("MainWindow", u"\u8fd16\u6708 (%)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u9669", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4e70\u5165/\u5356\u51fa\u89c4\u5219", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6301\u4ed3\u7c7b\u578b\u5360\u6bd4", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6301\u4ed3\u80a1\u7968\u5360\u6bd4", None))
        self.lbReportTime.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u76c8\u5229\u6982\u7387", None))
    # retranslateUi

