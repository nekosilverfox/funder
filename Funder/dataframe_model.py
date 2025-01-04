import sys
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import QTableView


# 自定义模型，用于将 DataFrame 数据适配到 QTableView
class DataFrameModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        # 返回行数
        return len(self._data)

    def columnCount(self, parent=None):
        # 返回列数
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        """返回单元格的数据和样式"""
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        # 获取单元格数据
        value = self._data.iloc[row, col]

        if role == Qt.DisplayRole:
            # 返回数据作为字符串
            return str(value)

        if role == Qt.ForegroundRole:
            # 设置文字颜色
            if self._data.columns[col] == "手续费" and isinstance(value, (float, int)) and value > 0.15:
                return QBrush(QColor("red"))  # 手续费大于 0.15 的文字为红色
            elif self._data.columns[col] == "手续费" and isinstance(value, (float, int)) and value <= 0.15:
                return QBrush(QColor("green"))  # 手续费小于于 0.15 的文字为绿色

            elif self._data.columns[col] == "申购状态" and value == "开放申购":
                return QBrush(QColor("green"))
            elif self._data.columns[col] == "申购状态" and value == "限大额":
                return QBrush(QColor("yellow"))
            elif self._data.columns[col] == "申购状态" and value == "暂停申购":
                return QBrush(QColor("red"))

            elif self._data.columns[col] == "赎回状态" and value == "开放赎回":
                return QBrush(QColor("green"))
            elif self._data.columns[col] == "赎回状态" and value == "暂停赎回":
                return QBrush(QColor("red"))

            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value >= 10000:
                return QBrush(QColor("green"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 10000 and value >= 1000:
                return QBrush(QColor("yellow"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 1000 and value >= 300:
                return QBrush(QColor("orange"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 300:
                return QBrush(QColor("red"))

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # 提供表头数据
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                # 返回列标签
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                # 返回行索引
                return str(self._data.index[section])
        return None
