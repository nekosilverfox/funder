# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from logger import Logger
Logger.init_logger()  # 初始化 Logger

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

from common import Common


class MainWindow(QMainWindow):
    _fund = None
    _log = Logger.get_logger()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 向状态栏添加控件
        self.statusBar().showMessage("窗体初始化成功")

        # 初始化数据源
        self._fund = Common()
        QTimer.singleShot(1000, self.reload_fund)  # 延迟 n 秒后执行 reload_all_fund 方法


    def reload_fund(cls):
        cls.statusBar().showMessage("下载基金数据中...")
        cls._fund.reload_all_fund()
        cls.statusBar().showMessage("下载所有基金数据完成")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    Logger.get_logger().info("程序初始化...")

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
