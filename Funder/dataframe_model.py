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
        self.include_words = []
        self.exclude_words = []
        self.filter_column = -1  # 默认不指定列

    def rowCount(self, parent=None):
        # 返回行数
        return len(self._data)

    def columnCount(self, parent=None):
        # 返回列数
        return len(self._data.columns)

    def getCurrentData(self):  # 新增方法
        return self._data

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
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, float):
                return f"{int(value)}"  # 转换为整数格式
            elif (self._data.columns[col] == "日增长率"
                  or self._data.columns[col] == "近1周"
                  or self._data.columns[col] == "近1月"
                  or self._data.columns[col] == "近3月"
                  or self._data.columns[col] == "近6月"
                  or self._data.columns[col] == "近1年"
                  or self._data.columns[col] == "近2年"
                  or self._data.columns[col] == "近3年"
                  or self._data.columns[col] == "今年来"
                  or self._data.columns[col] == "成立来"):
                return f"{value}%"  # 添加百分号

            return str(value)  # 返回正常数据

        # Qt.ForegroundRole 的优先级高于样式表
        if role == Qt.ForegroundRole:
            # 设置文字颜色
            if self._data.columns[col] == "手续费" and isinstance(value, (float, int)) and value > 0.15:
                return QBrush(QColor("#F03D44"))  # 手续费大于 0.15 的文字为红色
            elif self._data.columns[col] == "手续费" and isinstance(value, (float, int)) and value <= 0.15:
                return QBrush(QColor("#4EBC76"))  # 手续费小于于 0.15 的文字为绿色

            elif self._data.columns[col] == "申购状态" and value == "开放申购":
                return QBrush(QColor("#4EBC76"))
            elif self._data.columns[col] == "申购状态" and value == "限大额":
                return QBrush(QColor("yellow"))
            elif self._data.columns[col] == "申购状态" and value == "暂停申购":
                return QBrush(QColor("#F03D44"))

            elif self._data.columns[col] == "赎回状态" and value == "开放赎回":
                return QBrush(QColor("#4EBC76"))
            elif self._data.columns[col] == "赎回状态" and value == "暂停赎回":
                return QBrush(QColor("#F03D44"))
            elif self._data.columns[col] == "赎回状态" and value == "封闭期":
                return QBrush(QColor("#F03D44"))
            elif self._data.columns[col] == "赎回状态" and value == "场内交易":
                return QBrush(QColor("orange"))

            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value >= 10000:
                return QBrush(QColor("#4EBC76"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 10000 and value >= 1000:
                return QBrush(QColor("yellow"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 1000 and value >= 300:
                return QBrush(QColor("orange"))
            elif self._data.columns[col] == "日累计限定金额" and isinstance(value, (float, int)) and value < 300:
                return QBrush(QColor("#F03D44"))
            elif (self._data.columns[col] == "日增长率"
                  or self._data.columns[col] == "近1周"
                  or self._data.columns[col] == "近1月"
                  or self._data.columns[col] == "近3月"
                  or self._data.columns[col] == "近6月"
                  or self._data.columns[col] == "近1年"
                  or self._data.columns[col] == "近2年"
                  or self._data.columns[col] == "近3年"
                  or self._data.columns[col] == "今年来"
                  or self._data.columns[col] == "成立来"):
                if value > 0 and (not pd.isna(value) or not pd.isnull(value)):
                    return QBrush(QColor("#F03D44"))
                elif value <= 0 and (not pd.isna(value) or not pd.isnull(value)):
                    return QBrush(QColor("#4EBC76"))
            else:
                return QBrush(QColor("#CFD7E0"))  # 默认颜色
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

    def resetDataFrame(self, data: pd.DataFrame):
        """重新设置模型的数据"""
        self.beginResetModel()
        self._data = data.copy()
        self.endResetModel()
