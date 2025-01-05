# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from logger import Logger
Logger.init_logger()  # 初始化 Logger

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QProgressBar
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
        # self.ui.setTitle("公募基金筛选器")

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
        cls.statusBar().showMessage(f"成功获取公募基金数据 共 {cls._fund.shape[0]} 条数据")
        cls._log.info(cls._fund)
        cls.ui.tbvFunds.setModel(DataFrameModel(cls._fund))  # 创建 DataFrameModel 并绑定到 QTableView
        cls.set_tb_header_style()  # 设置表样式
        cls.statusBar().removeWidget(cls.loding_bar)  # 移除进度条

    def handle_error(cls, error_message):
        """处理错误"""
        cls.statusBar().showMessage(error_message)
        cls.statusBar().removeWidget(cls.loding_bar)  # 移除进度条

    def reload_fund(cls):
        """启动子线程去获取基金数据"""
        # 添加无限循环的进度条到状态栏
        cls.loding_bar = QProgressBar()
        cls.loding_bar.setRange(0, 0)  # 无限循环模式
        cls.loding_bar.setFixedWidth(200)  # 设置进度条宽度
        cls.statusBar().addPermanentWidget(cls.loding_bar)

        cls.statusBar().showMessage("开始获取基金数据...")
        cls._log.info("开始获取基金数据")
        cls.thread.start()  # 启动子线程

    def set_tb_header_style(cls):
        """设置表头样式，必须在数据添加之后调用，否则会因为越界导致崩溃"""
        cls._log.info("设置表样式")
        cls.ui.tbvFunds.verticalHeader().setVisible(False)  # 取消显示水平表头

        tb_header = cls.ui.tbvFunds.horizontalHeader()
        tb_header.setSectionResizeMode(QHeaderView.Stretch)  # 自动拉伸

        tb_header.setSectionResizeMode(0, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(0, 65)  # 固定宽度

        tb_header.setSectionResizeMode(2, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(2, 110)  # 固定宽度

        tb_header.setSectionResizeMode(3, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(3, 65)  # 固定宽度

        tb_header.setSectionResizeMode(4, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(4, 60)  # 日增长率

        tb_header.setSectionResizeMode(5, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(5, 55)  # 近1周

        tb_header.setSectionResizeMode(6, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(6, 55)  # 近1月

        tb_header.setSectionResizeMode(7, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(7, 55)  # 近3月

        tb_header.setSectionResizeMode(8, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(8, 55)  # 近6月

        tb_header.setSectionResizeMode(9, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(9, 63)  # 近1年

        tb_header.setSectionResizeMode(10, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(10, 63)  # 近2年

        tb_header.setSectionResizeMode(11, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(11, 63)  # 近3年

        tb_header.setSectionResizeMode(12, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(12, 60)  # 今年来

        tb_header.setSectionResizeMode(13, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(13, 65)  # 成立来

        tb_header.setSectionResizeMode(14, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(14, 70)  # 固定宽度

        tb_header.setSectionResizeMode(15, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(15, 70)  # 固定宽度

        tb_header.setSectionResizeMode(16, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(16, 85)  # 下一开放日

        tb_header.setSectionResizeMode(17, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(17, 110)  # 固定宽度

        tb_header.setSectionResizeMode(18, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(18, 50)  # 固定宽度

        cls._log.info("设置表样式完成")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置全局样式表
    app.setStyleSheet("""
        /* 设置整个应用程序的背景为黑色，文字为白色 */
        QWidget {
            background-color: #31363E;
            color: #D3DAE7;
        }

        /* 表格整体背景颜色 */
        QTableView {
            background-color: #1B1D1F;
            gridline-color: #242830;
            alternate-background-color: #182D0F;
            selection-background-color: #273B5A;
        }
        QTableView::item:selected {
                color: inherit; /* 选中时字体颜色保持与未选中一致 */
            }
    """)

    Logger.get_logger().info("程序初始化...")

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
