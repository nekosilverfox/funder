# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from logger import Logger

Logger.init_logger()  # 初始化 Logger

import sys
import pandas as pd

from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QProgressBar
from ui_form import Ui_MainWindow

from fund_getter_thread import FundGetterThread
from dataframe_model import DataFrameModel


class MainWindow(QMainWindow):
    _fund = None
    _log = Logger.get_logger()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.loding_bar = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setTitle("公募基金筛选器")

        self.tbvModel = None

        # 向状态栏添加控件
        self.statusBar().showMessage("窗体初始化成功")

        # 创建子线程
        self.thread = FundGetterThread()
        self.thread.progress_signal.connect(self.update_status_msg)  # 连接进度信号到更新状态方法
        self.thread.result_signal.connect(self.receive_fund_data)  # 连接结果信号到结果处理方法
        self.thread.error_signal.connect(self.handle_error)  # 连接错误信号到错误处理方法

        # 获取基金数据
        QTimer.singleShot(1000, self.reload_fund)  # 延迟 n 秒后执行 reload_fund 方法

        self.connect_signal_solt()

    def connect_signal_solt(self):
        """连接信号和槽"""
        self.ui.cb1Week.stateChanged.connect(lambda state: self.set_col_hidden(state, "近1周"))
        self.ui.cb1Month.stateChanged.connect(lambda state: self.set_col_hidden(state, "近1月"))
        self.ui.cb3Month.stateChanged.connect(lambda state: self.set_col_hidden(state, "近3月"))
        self.ui.cb6Month.stateChanged.connect(lambda state: self.set_col_hidden(state, "近6月"))
        self.ui.cb1Year.stateChanged.connect(lambda state: self.set_col_hidden(state, "近1年"))
        self.ui.cb2Year.stateChanged.connect(lambda state: self.set_col_hidden(state, "近2年"))
        self.ui.cb3Year.stateChanged.connect(lambda state: self.set_col_hidden(state, "近3年"))
        self.ui.cbThisYear.stateChanged.connect(lambda state: self.set_col_hidden(state, "今年来"))
        self.ui.cbFromSetup.stateChanged.connect(lambda state: self.set_col_hidden(state, "成立来"))
        self.ui.cbFundType.stateChanged.connect(lambda state: self.set_col_hidden(state, "基金类型"))
        self.ui.cbCanBuy.stateChanged.connect(lambda state: self.set_col_hidden(state, "申购状态"))
        self.ui.cbCanSale.stateChanged.connect(lambda state: self.set_col_hidden(state, "赎回状态"))
        self.ui.cbNextOpenDay.stateChanged.connect(lambda state: self.set_col_hidden(state, "下一开放日"))
        self.ui.cbDayQuota.stateChanged.connect(lambda state: self.set_col_hidden(state, "日累计限定金额"))
        self.ui.cbT1Premium.stateChanged.connect(lambda state: self.set_col_hidden(state, "T-1溢价率"))

        self.ui.leIncludeWords.textChanged.connect(self.filter_by_fund_name)
        self.ui.leExcludeWords.textChanged.connect(self.filter_by_fund_name)

        self.ui.btnCleanIncludeWords.clicked.connect(self.ui.leIncludeWords.clear)
        self.ui.btnCleanExcludeWords.clicked.connect(self.ui.leExcludeWords.clear)

    def update_status_msg(cls, message):
        """更新状态栏状态"""
        cls.statusBar().showMessage(message)

    def receive_fund_data(cls, data):
        """处理任务结果"""
        cls._fund = data
        cls.statusBar().showMessage(f'成功获取公募基金数据 共 {cls._fund.shape[0]} 条数据\t获取时间 {QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")}')
        cls._log.info(cls._fund)
        cls.tbvModel = DataFrameModel(cls._fund)
        cls.ui.tbvFunds.setModel(cls.tbvModel)  # 创建 DataFrameModel 并绑定到 QTableView
        cls.set_tb_header_style()  # 设置表样式
        cls.statusBar().removeWidget(cls.loding_bar)  # 移除进度条

        # 连接复选框对应表列的信号和槽
        cls.ui.cb1Week.setChecked(True)
        cls.ui.cb1Month.setChecked(True)
        cls.ui.cb3Month.setChecked(True)
        cls.ui.cb6Month.setChecked(True)
        cls.ui.cb1Year.setChecked(True)
        cls.ui.cb2Year.setChecked(False)
        cls.set_col_hidden(0, "近2年")
        cls.ui.cb3Year.setChecked(False)
        cls.set_col_hidden(0, "近3年")
        cls.ui.cbThisYear.setChecked(True)
        cls.ui.cbFromSetup.setChecked(True)
        cls.ui.cbFundType.setChecked(True)
        cls.ui.cbCanBuy.setChecked(True)
        cls.ui.cbCanSale.setChecked(False)
        cls.set_col_hidden(0, "赎回状态")
        cls.ui.cbNextOpenDay.setChecked(False)
        cls.set_col_hidden(0, "下一开放日")
        cls.ui.cbDayQuota.setChecked(True)
        cls.ui.cbT1Premium.setChecked(False)
        cls.set_col_hidden(0, "T-1溢价率")

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

    def set_col_hidden(cls, state, col_name):
        """根据复选框状态确认是否隐藏某些行"""
        col_index = cls._fund.columns.get_loc(col_name)
        # cls._log.info(f"ComboBox {col_name} 状态变为 {Qt.CheckState.Checked} 受影响表列下标 {col_index}")
        if state == 2:
            cls._log.info(f"ComboBox {col_name} 状态变为 Checked 受影响表列下标 {col_index}")
            cls.ui.tbvFunds.setColumnHidden(col_index, False)
        elif state == 0:
            cls._log.info(f"ComboBox {col_name} 状态变为 UnChecked 受影响表列下标 {col_index}")
            cls.ui.tbvFunds.setColumnHidden(col_index, True)

    def set_tb_header_style(cls):
        """设置表头样式，必须在数据添加之后调用，否则会因为越界导致崩溃"""
        cls._log.info("设置表样式")
        # cls.ui.tbvFunds.verticalHeader().setVisible(False)  # 取消显示水平表头
        # cls.ui.tbvFunds.verticalHeader().setDefaultSectionSize(30)  # 设置固定行高为 35 像素

        cls.ui.tbvFunds.setSortingEnabled(True)  # 启用排序功能
        tb_header = cls.ui.tbvFunds.horizontalHeader()
        tb_header.setSectionResizeMode(QHeaderView.Stretch)  # 自动拉伸

        tb_header.setSectionResizeMode(0, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(0, 65)  # 固定宽度

        tb_header.setSectionResizeMode(2, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(2, 110)  # 基金类型

        tb_header.setSectionResizeMode(3, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(3, 65)  # 固定宽度

        tb_header.setSectionResizeMode(4, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(4, 60)  # 日增长率

        tb_header.setSectionResizeMode(5, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(5, 60)  # 近1周

        tb_header.setSectionResizeMode(6, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(6, 60)  # 近1月

        tb_header.setSectionResizeMode(7, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(7, 60)  # 近3月

        tb_header.setSectionResizeMode(8, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(8, 60)  # 近6月

        tb_header.setSectionResizeMode(9, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(9, 65)  # 近1年

        tb_header.setSectionResizeMode(10, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(10, 65)  # 近2年

        tb_header.setSectionResizeMode(11, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(11, 65)  # 近3年

        tb_header.setSectionResizeMode(12, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(12, 60)  # 今年来

        tb_header.setSectionResizeMode(13, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(13, 65)  # 成立来

        tb_header.setSectionResizeMode(14, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(14, 70)  # 申购状态

        tb_header.setSectionResizeMode(15, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(15, 70)  # 赎回状态

        tb_header.setSectionResizeMode(16, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(16, 85)  # 下一开放日

        tb_header.setSectionResizeMode(17, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(17, 110)  # 固定宽度

        tb_header.setSectionResizeMode(18, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(18, 50)  # 固定宽度

        tb_header.setSectionResizeMode(19, QHeaderView.Fixed)
        cls.ui.tbvFunds.setColumnWidth(19, 55)  # 固定宽度

        cls._log.info("设置表样式完成")

    def filter_by_fund_name(self):
        """根据正向和反向词过滤基金名称"""
        include_input = self.ui.leIncludeWords.text().strip()
        exclude_input = self.ui.leExcludeWords.text().strip()

        # 将空格替换为 '|', 创建正则表达式的 alternation
        include_words = '|'.join(include_input.split()) if include_input else None
        exclude_words = '|'.join(exclude_input.split()) if exclude_input else None

        self._log.info(f'正向过滤词：{include_words} 反向过滤词：{exclude_words}')

        # 初始化 mask 为全 True
        mask = pd.Series([True] * len(self._fund))

        # 应用包含条件
        if include_words:
            mask &= self._fund["基金简称"].str.contains(include_words, regex=True, na=False)

        # 应用排除条件
        if exclude_words:
            mask &= ~self._fund["基金简称"].str.contains(exclude_words, regex=True, na=False)

        filter_fund = self._fund[mask]
        self.tbvModel.resetDataFrame(pd.DataFrame(filter_fund))


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
