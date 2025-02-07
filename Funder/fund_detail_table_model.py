import sys
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import QTableView


# 自定义模型，用于将 DataFrame 数据适配到 QTableView
class FundDetailTableModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self._data = data
        self.include_words = []
        self.exclude_words = []
        self.filter_column = -1  # 默认不指定列

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
            # 判断是否为缺失值 (NaN 或 NaT)
            if pd.isna(value) or pd.isnull(value):  # 判断是否是 NaN 或 NaT
                return "-"  # 替换为 "-"

            elif (self._data.columns[col] == "盈利概率"
                  or self._data.columns[col] == "平均收益"
                  or self._data.columns[col] == "年化波动率"
                  or self._data.columns[col] == "仓位占比"
                  or self._data.columns[col] == "占净值比例"):
                return f"{value}%"  # 添加百分号

            elif (self._data.columns[col] == "费用") and value <= 50.0:
                return f"{value}%"  # 添加百分号
            elif (self._data.columns[col] == "费用") and value > 50.0:
                return f"{value}元"  # 添加百分号

            return str(value)  # 返回正常数据

        # Qt.ForegroundRole 的优先级高于样式表
        if role == Qt.ForegroundRole:
            # 设置文字颜色
            if self._data.columns[col] == "平均收益" and isinstance(value, (float, int)) and value <= 0.0:
                return QBrush(QColor("#F03D44"))  # 红色
            elif self._data.columns[col] == "仓位占比" and isinstance(value, (float, int)) and value >= 9.0:
                return QBrush(QColor("blue"))
        return None

    def sort(self, column, order):
        """实现排序功能"""
        if (column < 0) or (column >= self.columnCount()):
            return

        self.layoutAboutToBeChanged.emit()

        column_name = self._data.columns[column]
        ascending = order == Qt.AscendingOrder
        self._data.sort_values(by=column_name, ascending=ascending, inplace=True, kind='mergesort')  # 使用稳定排序
        self._data.reset_index(drop=True, inplace=True)

        self.layoutChanged.emit()
        self._sort_column = column
        self._sort_order = order

    def clear(self):
        """清空模型的数据"""
        self.beginResetModel()  # 通知视图数据即将变化
        self._data = pd.DataFrame()  # 清空数据
        self.endResetModel()  # 通知视图数据变化已完成

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
