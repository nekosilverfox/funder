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
            step = 0
            # 获取所有基金列表
            step += 1
            self.progress_signal.emit(f"「{step}」获取公募基金列表中...")
            all_fund = ak.fund_name_em()
            self.progress_signal.emit("获取公募基金列表完成")

            # 获取基金申购状态
            step += 1
            self.progress_signal.emit(f"「{step}」获取所有公募基金申购状态中...")
            fund_purchase_state = ak.fund_purchase_em()
            fund_purchase_state = fund_purchase_state.drop(columns=["序号", "基金简称", "最新净值/万份收益", "最新净值/万份收益-报告时间"])
            self.progress_signal.emit("获取所有公募基金申购状态完成")

            # 获取开放公募基金涨跌数据
            step += 1
            self.progress_signal.emit(f"「{step}」获取开放公募基金涨跌数据中...")
            fund_rank = ak.fund_open_fund_rank_em()
            fund_rank = fund_rank.drop(columns=["序号", "基金简称", "日期", "累计净值", "自定义", "手续费"])
            self.progress_signal.emit("获取开放公募基金涨跌数据完成")

            # 获取开放公募基金涨跌数据
            step += 1
            self.progress_signal.emit(f"「{step}」获取 QDII 基金数据中...")
            fund_qdii = ak.qdii_e_index_jsl()
            fund_qdii = fund_qdii[["代码", "T-1溢价率"]]
            fund_qdii = fund_qdii.rename(columns={"代码": "基金代码"})
            self.progress_signal.emit("获取 QDII 基金数据完成")

            # 合并基金和申购状态
            step += 1
            self.progress_signal.emit(f"「{step}」合并基金列表及申购状态中...")
            merged_df = pd.merge(all_fund, fund_rank,
                                 on="基金代码",
                                 how="left",
                                 suffixes=("", "_r"))
            merged_df = pd.merge(merged_df, fund_purchase_state,
                                 on="基金代码",
                                 how="left",
                                 suffixes=("", "_r"))
            merged_df = pd.merge(merged_df, fund_qdii,
                                 on="基金代码",
                                 how="left",
                                 suffixes=("", "_r"))

            # 删除重复列
            step += 1
            self.progress_signal.emit(f"「{step}」删除重复列中...")
            columns_to_drop = [col for col in merged_df.columns if col.endswith("_r")]
            merged_df = merged_df.drop(columns=columns_to_drop)

            # 最终的基金数据
            self.progress_signal.emit("整理基金数据...")
            final_df = merged_df.drop(columns=["拼音缩写", "拼音全称", "购买起点"])

            self.progress_signal.emit("获取所有公募基金数据完成")
            self.result_signal.emit(final_df)  # 发送结果到主线程

        except Exception as e:
            error_message = f"获取公募基金数据时发生错误: {str(e)}"
            self.progress_signal.emit(error_message)
            self.error_signal.emit(error_message)  # 发送错误信号
