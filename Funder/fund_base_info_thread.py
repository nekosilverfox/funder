# This Python file uses the following encoding: utf-8


from PySide6.QtCore import QThread, Signal
import akshare as ak
import pandas as pd


class FundBaseInfoThread(QThread):
    progress_signal = Signal(str)  # 用于传递进度日志
    result_signal = Signal(pd.DataFrame)  # 用于传递任务完成后的结果
    error_signal = Signal(str)  # 用于传递错误信息

    def __init__(self, fund_code: str, logger=None):
        super().__init__()
        self._fund_code = fund_code
        self._log = logger

    def run(self):
        try:
            self.progress_signal.emit(f"获取基金 {self._fund_code} 基本信息中...")
            data = ak.fund_individual_basic_info_xq(symbol=self._fund_code)
            self.progress_signal.emit(f"获取基金 {self._fund_code} 基本信息完成")
            self.result_signal.emit(data)  # 发送结果到主线程

        except Exception as e:
            error_message = f"获取基金 {self._fund_code} 基本信息时发生错误: {str(e)}"
            self.progress_signal.emit(error_message)
            self.error_signal.emit(error_message)  # 发送错误信号
