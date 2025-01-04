from PySide6.QtCore import QThread, Signal
import akshare as ak
import pandas as pd

class FundGetterThread(QThread):
    progress_signal = Signal(str)  # 用于传递进度日志
    result_signal = Signal(pd.DataFrame)  # 用于传递任务完成后的结果
    error_signal = Signal(str)  # 用于传递错误信息

    def __init__(self):
        super().__init__()
        self._log = None

    def set_logger(self, logger):
        """设置日志记录器"""
        self._log = logger

    def run(self):
        try:
            # 获取所有基金列表
            self.progress_signal.emit("获取所有基金列表中...")
            all_fund = ak.fund_name_em()
            self.progress_signal.emit("获取所有基金列表完成")

            # 获取基金申购状态
            self.progress_signal.emit("获取所有基金申购状态...")
            fund_purchase_state = ak.fund_purchase_em()
            self.progress_signal.emit("获取所有基金申购状态完成")

            # 合并基金和申购状态
            self.progress_signal.emit("合并基金列表及申购状态...")
            merged_df = pd.merge(all_fund, fund_purchase_state,
                                 on="基金代码",
                                 how="inner",
                                 suffixes=("", "_r"))

            # 删除重复列
            self.progress_signal.emit("删除重复列...")
            columns_to_drop = [col for col in merged_df.columns if col.endswith("_r")]
            merged_df = merged_df.drop(columns=columns_to_drop)

            # 最终的基金数据
            self.progress_signal.emit("整理基金数据...")
            final_df = merged_df.drop(columns=["序号", "拼音全称", "购买起点", "最新净值/万份收益-报告时间"])

            self.progress_signal.emit("获取所有基金数据完成")
            self.result_signal.emit(final_df)  # 发送结果到主线程

        except Exception as e:
            error_message = f"获取基金数据时发生错误: {str(e)}"
            self.progress_signal.emit(error_message)
            self.error_signal.emit(error_message)  # 发送错误信号
