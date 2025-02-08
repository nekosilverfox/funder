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
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QProgressBar, QSizePolicy
from ui_form import Ui_MainWindow
from fund_base_info_widget import FundBaseInfoWidget
from dataframe_model import DataFrameModel
from fund_detail_table_model import FundDetailTableModel

from fund_getter_thread import FundGetterThread
from fund_base_info_thread import FundBaseInfoThread
from fund_buy_sale_detail_thread import FundBuySaleDetailThread
from fund_hold_type_thread import FundHoldTypeThread
from fund_hold_detail_thread import FundHoldDetailThread
from fund_profit_probability_thread import FundProfitProbabilityThread
from fund_risk_thread import FundRiskThread

class MainWindow(QMainWindow):
    _fund = None
    _log = Logger.get_logger()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("公募基金筛选器")

        # 添加无限循环的进度条到状态栏
        self.loding_bar = QProgressBar()
        self.loding_bar.setRange(0, 0)  # 无限循环模式
        self.loding_bar.setFixedWidth(200)  # 设置进度条宽度

        self.ui.barRisk.setRange(0, 0)
        self.ui.barBuySaleRole.setRange(0, 0)
        self.ui.barHoldType.setRange(0, 0)
        self.ui.barHoldDetail.setRange(0, 0)
        self.ui.barProfit.setRange(0, 0)

        self.tbvModel = None

        # 隐藏行号
        self.ui.tbvRisk.verticalHeader().hide()
        self.ui.tbvBuySaleRole.verticalHeader().hide()
        self.ui.tbvHoldType.verticalHeader().hide()
        self.ui.tbvHoldDetail.verticalHeader().hide()
        self.ui.tbvProfit.verticalHeader().hide()

        # 设置列宽和行高拉伸策略
        self.ui.tbvRisk.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbvBuySaleRole.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbvHoldType.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbvHoldDetail.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbvProfit.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 隐藏拉杆
        self.ui.tbvRisk.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tbvBuySaleRole.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tbvHoldType.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tbvHoldDetail.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tbvProfit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 设置 QTableView 的大小策略
        self.ui.tbvRisk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.tbvBuySaleRole.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.tbvHoldType.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.tbvHoldDetail.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.tbvProfit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # self.ui.tbvRisk
        # self.ui.tbvBuySaleRole
        # self.ui.tbvHoldType
        # self.ui.tbvHoldDetail
        # self.ui.tbvProfit

        # 向状态栏添加控件
        self.statusBar().showMessage("窗体初始化成功")

        # 创建子线程
        # 获取所有基金列表
        self.thread_all_fund_list = FundGetterThread()
        self.thread_all_fund_list.progress_signal.connect(self.update_status_msg)  # 连接进度信号到更新状态方法
        self.thread_all_fund_list.result_signal.connect(self.receive_fund_data)  # 连接结果信号到结果处理方法
        self.thread_all_fund_list.error_signal.connect(self.handle_error)  # 连接错误信号到错误处理方法

        # 基金基本信息
        self.thread_fund_base_info = FundBaseInfoThread(self._log)
        self.thread_fund_base_info.progress_signal.connect(self.update_status_msg)
        self.thread_fund_base_info.result_signal.connect(self.receive_fund_base_info)
        self.thread_fund_base_info.error_signal.connect(self.handle_error)

        # 买卖信息
        self.thread_buy_sale_detail = FundBuySaleDetailThread(self._log)
        self.thread_buy_sale_detail.progress_signal.connect(self.update_status_msg)
        self.thread_buy_sale_detail.result_signal.connect(self.receive_buy_sale_detail)
        self.thread_buy_sale_detail.error_signal.connect(self.handle_error)

        # 持仓类型信息
        self.thread_fund_hold_type = FundHoldTypeThread(self._log)
        self.thread_fund_hold_type.progress_signal.connect(self.update_status_msg)
        self.thread_fund_hold_type.result_signal.connect(self.receive_fund_hold_type)
        self.thread_fund_hold_type.error_signal.connect(self.handle_error)

        # 持仓细节
        self.thread_fund_hold_detail = FundHoldDetailThread(self._log)
        self.thread_fund_hold_detail.progress_signal.connect(self.update_status_msg)
        self.thread_fund_hold_detail.result_signal.connect(self.receive_fund_hold_detail)
        self.thread_fund_hold_detail.error_signal.connect(self.handle_error)

        # 风险信息（波动回撤等）
        self.thread_fund_risk = FundRiskThread(self._log)
        self.thread_fund_risk.progress_signal.connect(self.update_status_msg)
        self.thread_fund_risk.result_signal.connect(self.receive_fund_risk)
        self.thread_fund_risk.error_signal.connect(self.handle_error)

        # 盈利概率
        self.thread_fund_profit = FundProfitProbabilityThread(self._log)
        self.thread_fund_profit.progress_signal.connect(self.update_status_msg)
        self.thread_fund_profit.result_signal.connect(self.receive_fund_profit)
        self.thread_fund_profit.error_signal.connect(self.handle_error)

        # 获取基金数据
        QTimer.singleShot(500, self.reload_fund)  # 延迟 n 毫秒后执行 reload_fund 方法

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

    def update_status_msg(self, message):
        """更新状态栏状态"""
        self.statusBar().showMessage(message)

    def receive_fund_data(self, data):
        """处理任务结果"""
        self._fund = data
        self.statusBar().showMessage(
            f'成功获取公募基金数据 共 {self._fund.shape[0]} 条数据\t获取时间 {QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")}')
        self._log.info(self._fund)
        self.tbvModel = DataFrameModel(self._fund)
        self.ui.tbvFunds.setModel(self.tbvModel)  # 创建 DataFrameModel 并绑定到 QTableView
        self.ui.tbvFunds.selectionModel().selectionChanged.connect(self.tbvFundsSelectChanged)  # 连接选中行信号

        self.set_tb_header_style()  # 设置表样式
        self.statusBar().removeWidget(self.loding_bar)  # 移除进度条

        # 连接复选框对应表列的信号和槽
        self.ui.cb1Week.setChecked(True)
        self.ui.cb1Month.setChecked(True)
        self.ui.cb3Month.setChecked(True)
        self.ui.cb6Month.setChecked(True)
        self.ui.cb1Year.setChecked(True)
        self.ui.cb2Year.setChecked(False)
        self.set_col_hidden(0, "近2年")
        self.ui.cb3Year.setChecked(False)
        self.set_col_hidden(0, "近3年")
        self.ui.cbThisYear.setChecked(True)
        self.ui.cbFromSetup.setChecked(True)
        self.ui.cbFundType.setChecked(True)
        self.ui.cbCanBuy.setChecked(True)
        self.ui.cbCanSale.setChecked(False)
        self.set_col_hidden(0, "赎回状态")
        self.ui.cbNextOpenDay.setChecked(False)
        self.set_col_hidden(0, "下一开放日")
        self.ui.cbDayQuota.setChecked(True)
        self.ui.cbT1Premium.setChecked(False)
        self.set_col_hidden(0, "T-1溢价率")

    def replace_widget_in_layout(self, target_widget, new_widget):
        layout = self.ui.sawFundInfo.layout()
        for i in range(layout.count()):
            if layout.itemAt(i).widget() == target_widget:
                obj_name = target_widget.objectName()

                layout.removeWidget(target_widget)
                target_widget.setParent(None)
                target_widget.deleteLater()

                new_widget.setObjectName(obj_name)
                layout.insertWidget(i, new_widget)
                break

    def receive_fund_base_info(self, data):
        """接收子线程数据：基金基本信息"""
        self.statusBar().showMessage("成功获取基金基本信息")
        self._log.info(f"成功获取基金基本信息：{data}")

        if data is None:
            return

        new_widget = FundBaseInfoWidget(data, logger=self._log)
        self.replace_widget_in_layout(self.ui.wFundBaseInfo, new_widget)
        self.ui.wFundBaseInfo = new_widget

    def receive_buy_sale_detail(self, data):
        """接收子线程数据：买卖信息"""
        self.statusBar().showMessage("成功获取买卖信息")
        self._log.info(f"成功获取买卖信息：{data}")
        self.ui.barBuySaleRole.hide()

        if data is None:
            return
        tb_model = FundDetailTableModel(data)
        self.ui.tbvBuySaleRole.setModel(tb_model)
        self.adjust_table_height(self.ui.tbvBuySaleRole)

    def receive_fund_hold_type(self, data):
        """接收子线程数据：持仓类型信息"""
        self.statusBar().showMessage("成功获取持仓类型信息")
        self._log.info(f"成功获取持仓类型信息：{data}")
        self.ui.barHoldType.hide()

        if data is None:
            return
        tb_model = FundDetailTableModel(data)
        self.ui.tbvHoldType.setModel(tb_model)
        self.adjust_table_height(self.ui.tbvHoldType)

    def receive_fund_hold_detail(self, data):
        """接收子线程数据：持仓细节"""
        self.statusBar().showMessage("成功获取持仓细节")
        self._log.info(f"成功获取持仓细节：{data}")
        self.ui.barHoldDetail.hide()

        if data is None:
            return
        tb_model = FundDetailTableModel(data)
        self.ui.tbvHoldDetail.setModel(tb_model)
        self.adjust_table_height(self.ui.tbvHoldDetail)

    def receive_fund_risk(self, data):
        """接收子线程数据：风险信息"""
        self.statusBar().showMessage("成功获取风险信息")
        self._log.info(f"成功获取风险信息：{data}")
        self.ui.barRisk.hide()

        if data is None:
            return
        tb_model = FundDetailTableModel(data)
        self.ui.tbvRisk.setModel(tb_model)
        self.adjust_table_height(self.ui.tbvRisk)

    def receive_fund_profit(self, data):
        """接收子线程数据：盈利概率"""
        self.statusBar().showMessage("成功获取盈利概率")
        self._log.info(f"成功获取盈利概率：{data}")
        self.ui.barProfit.hide()

        if data is None:
            return
        tb_model = FundDetailTableModel(data)
        self.ui.tbvProfit.setModel(tb_model)
        self.adjust_table_height(self.ui.tbvProfit)

    def handle_error(self, error_message):
        """处理错误"""
        self.statusBar().showMessage(error_message)
        self.statusBar().removeWidget(self.loding_bar)  # 移除进度条

    def reload_fund(self):
        """启动子线程去获取基金数据"""
        self.statusBar().addPermanentWidget(self.loding_bar)
        self.statusBar().showMessage("开始获取基金数据...")
        self._log.info("开始获取基金数据")
        self.thread_all_fund_list.start()  # 启动子线程

    def set_col_hidden(self, state, col_name):
        """根据复选框状态确认是否隐藏某些行"""
        col_index = self._fund.columns.get_loc(col_name)
        # self._log.info(f"ComboBox {col_name} 状态变为 {Qt.CheckState.Checked} 受影响表列下标 {col_index}")
        if state == 2:
            self._log.info(f"ComboBox {col_name} 状态变为 Checked 受影响表列下标 {col_index}")
            self.ui.tbvFunds.setColumnHidden(col_index, False)
        elif state == 0:
            self._log.info(f"ComboBox {col_name} 状态变为 UnChecked 受影响表列下标 {col_index}")
            self.ui.tbvFunds.setColumnHidden(col_index, True)

    def set_tb_header_style(self):
        """设置表头样式，必须在数据添加之后调用，否则会因为越界导致崩溃"""
        self._log.info("设置表样式")
        # self.ui.tbvFunds.verticalHeader().setVisible(False)  # 取消显示水平表头
        # self.ui.tbvFunds.verticalHeader().setDefaultSectionSize(30)  # 设置固定行高为 35 像素

        self.ui.tbvFunds.setSortingEnabled(True)  # 启用排序功能
        tb_header = self.ui.tbvFunds.horizontalHeader()
        tb_header.setSectionResizeMode(QHeaderView.Stretch)  # 自动拉伸

        tb_header.setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(0, 65)  # 固定宽度

        tb_header.setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(2, 110)  # 基金类型

        tb_header.setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(3, 65)  # 固定宽度

        tb_header.setSectionResizeMode(4, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(4, 60)  # 日增长率

        tb_header.setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(5, 60)  # 近1周

        tb_header.setSectionResizeMode(6, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(6, 60)  # 近1月

        tb_header.setSectionResizeMode(7, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(7, 60)  # 近3月

        tb_header.setSectionResizeMode(8, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(8, 60)  # 近6月

        tb_header.setSectionResizeMode(9, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(9, 65)  # 近1年

        tb_header.setSectionResizeMode(10, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(10, 65)  # 近2年

        tb_header.setSectionResizeMode(11, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(11, 65)  # 近3年

        tb_header.setSectionResizeMode(12, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(12, 60)  # 今年来

        tb_header.setSectionResizeMode(13, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(13, 65)  # 成立来

        tb_header.setSectionResizeMode(14, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(14, 70)  # 申购状态

        tb_header.setSectionResizeMode(15, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(15, 70)  # 赎回状态

        tb_header.setSectionResizeMode(16, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(16, 85)  # 下一开放日

        tb_header.setSectionResizeMode(17, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(17, 110)  # 固定宽度

        tb_header.setSectionResizeMode(18, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(18, 50)  # 固定宽度

        tb_header.setSectionResizeMode(19, QHeaderView.Fixed)
        self.ui.tbvFunds.setColumnWidth(19, 55)  # 固定宽度

        self._log.info("设置表样式完成")

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

    def tbvFundsSelectChanged(self):
        """处理选择变化事件，获取选中行的数据或行索引"""
        # 获取当前选中的行索引（QModelIndex 对象列表）
        indexes = self.ui.tbvFunds.selectionModel().selectedRows()
        if not indexes:
            return

        # 由于选择模式为单选，列表中最多只有一个元素
        model = self.ui.tbvFunds.model()  # 获取模型对象
        current_data = model.getCurrentData()  # 获取当前显示的数据
        index = indexes[0]  # 获取第一个选中的行 PySide6.QtCore.QModelIndex
        row = index.row()  # 获取行号（0-based index）
        row_data = current_data.iloc[row]  # 获取整行数据

        fund_code = row_data["基金代码"]
        self._log.info(f'选中行: {row}  基金代码：{fund_code}  基金简称：{row_data["基金简称"]}')
        self.statusBar().addPermanentWidget(self.loding_bar)

        # 启动子线程获取对应基金的各个信息
        self.thread_fund_base_info.set_fund_code(fund_code)
        self.thread_fund_base_info.start()

        if self.ui.tbvBuySaleRole.model() is not None:
            self.ui.tbvBuySaleRole.model().clear()
            self.adjust_table_height(self.ui.tbvBuySaleRole)
        self.thread_buy_sale_detail.set_fund_code(fund_code)
        self.thread_buy_sale_detail.start()
        self.ui.barBuySaleRole.show()

        if self.ui.tbvHoldType.model() is not None:
            self.ui.tbvHoldType.model().clear()
            self.adjust_table_height(self.ui.tbvHoldType)
        self.thread_fund_hold_type.set_fund_code(fund_code)
        self.thread_fund_hold_type.start()
        self.ui.barHoldType.show()

        if self.ui.tbvHoldDetail.model() is not None:
            self.ui.tbvHoldDetail.model().clear()
            self.adjust_table_height(self.ui.tbvHoldDetail)
        self.thread_fund_hold_detail.set_fund_code(fund_code)
        self.thread_fund_hold_detail.start()
        self.ui.barHoldDetail.show()

        if self.ui.tbvRisk.model() is not None:
            self.ui.tbvRisk.model().clear()
            self.adjust_table_height(self.ui.tbvRisk)
        self.thread_fund_risk.set_fund_code(fund_code)
        self.thread_fund_risk.start()
        self.ui.barRisk.show()

        if self.ui.tbvProfit.model() is not None:
            self.ui.tbvProfit.model().clear()
            self.adjust_table_height(self.ui.tbvProfit)
        self.thread_fund_profit.set_fund_code(fund_code)
        self.thread_fund_profit.start()
        self.ui.barProfit.show()

    def adjust_table_height(self, table_view):
        """根据列的数量更新指定 QTableView 的大小"""
        row_count = table_view.model().rowCount()
        row_height = table_view.rowHeight(0)  # 获取第一行的高度
        total_height = row_height * row_count  # 总高度 = 行高 * 行数

        # 设置 QTableView 的高度
        table_view.setFixedHeight(total_height + table_view.horizontalHeader().height())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置全局样式表
    app.setStyleSheet("""
        /* 设置整个应用程序的背景为黑色，文字为白色 */
        QLabel {
            margin: 0; 
            padding: 0; 
            border: 1px solid red;
        }
            
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
