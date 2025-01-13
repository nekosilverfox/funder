# This Python file uses the following encoding: utf-8


from PySide6.QtCore import QDateTime, QThread, Signal
import akshare as ak
import pandas as pd


class FundHoldTypeThread(QThread):
    progress_signal = Signal(str)  # 用于传递进度日志
    result_signal = Signal(pd.DataFrame)  # 用于传递任务完成后的结果
    error_signal = Signal(str)  # 用于传递错误信息

    def __init__(self, fund_code: str, logger=None):
        super().__init__()
        self._fund_code = fund_code
        self._log = logger

    def run(self):
        try:
            self.progress_signal.emit(f"获取基金 {self._fund_code} 仓位占比中...")
            data = ak.fund_individual_detail_hold_xq(symbol=self._fund_code, date=QDateTime.currentDateTime().toString("yyyyMMdd"))
            self.progress_signal.emit(f"获取基金 {self._fund_code} 仓位占比完成")

        except Exception as e:
            data = None
            error_message = f"获取基金 {self._fund_code} 仓位占比时发生错误: {str(e)}"
            self.progress_signal.emit(error_message)
            self.error_signal.emit(error_message)  # 发送错误信号

        self.result_signal.emit(data)  # 发送结果到主线程
