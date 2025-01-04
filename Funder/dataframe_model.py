import sys
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel
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
        # 提供单元格数据
        if role == Qt.DisplayRole:
            # 获取行和列索引
            row = index.row()
            col = index.column()
            # 返回 DataFrame 中对应的数据
            return str(self._data.iloc[row, col])
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
