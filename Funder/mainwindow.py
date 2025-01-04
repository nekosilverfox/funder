# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from logger import Logger
Logger.init_logger()  # 初始化 Logger

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView
from ui_form import Ui_MainWindow

from fund_getter_thread import FundGetterThread
from dataframe_model import DataFrameModel


class MainWindow(QMainWindow):
    _fund = None
    _log = Logger.get_logger()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 向状态栏添加控件
        self.statusBar().showMessage("窗体初始化成功")

        # 创建子线程
        self.thread = FundGetterThread()
        self.thread.progress_signal.connect(self.update_status_msg)  # 连接进度信号到更新状态方法
        self.thread.result_signal.connect(self.receive_fund_data)  # 连接结果信号到结果处理方法
        self.thread.error_signal.connect(self.handle_error)  # 连接错误信号到错误处理方法

        # 获取基金数据
        QTimer.singleShot(1000, self.reload_fund)  # 延迟 n 秒后执行 reload_fund 方法


    def update_status_msg(cls, message):
        """更新状态栏状态"""
        cls.statusBar().showMessage(message)

    def receive_fund_data(cls, data):
        """处理任务结果"""
        cls._fund = data
        cls.statusBar().showMessage("成功获取基金数据")
        cls._log.info(cls._fund)
        cls.ui.tbvFunds.setModel(DataFrameModel(cls._fund))  # 创建 DataFrameModel 并绑定到 QTableView
        cls.set_tb_header_style()  # 设置表样式

    def handle_error(cls, error_message):
        """处理错误"""
        cls.statusBar().showMessage(error_message)

    def reload_fund(cls):
        """启动子线程去获取基金数据"""
        cls.statusBar().showMessage("开始获取基金数据基...")
        cls._log.info("开始获取基金数据")
        cls.thread.start()  # 启动子线程

    def set_tb_header_style(cls):
        """设置表头样式，必须在数据添加之后调用，否则会因为越界导致崩溃"""
        cls._log.info("设置表样式")
        tb_header = cls.ui.tbvFunds.horizontalHeader()
        tb_header.setSectionResizeMode(QHeaderView.Stretch)  # 自动拉伸

        tb_header.setSectionResizeMode(0, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(0, 70)  # 固定宽度

        tb_header.setSectionResizeMode(3, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(3, 110)  # 固定宽度

        tb_header.setSectionResizeMode(4, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(4, 80)  # 固定宽度

        tb_header.setSectionResizeMode(5, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(5, 80)  # 固定宽度

        tb_header.setSectionResizeMode(6, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(6, 85)  # 固定宽度

        tb_header.setSectionResizeMode(7, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(7, 90)  # 固定宽度

        tb_header.setSectionResizeMode(8, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(8, 120)  # 固定宽度

        tb_header.setSectionResizeMode(9, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(9, 50)  # 固定宽度
        # tb_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 根据内容调整列宽
        # tb_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 根据内容调整列宽
        # tb_header.setSectionResizeMode(4, QHeaderView.ResizeToContents)  # 根据内容调整列宽
        cls._log.info("设置表样式完成")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    Logger.get_logger().info("程序初始化...")

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
