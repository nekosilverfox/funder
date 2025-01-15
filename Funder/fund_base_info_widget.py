import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QFormLayout, QGridLayout, QSizePolicy

"""
    item                                              value
0     基金代码                                             970195
1     基金名称                                   兴证资管金麒麟3个月(FOF)C
2     基金全称                 兴证资管金麒麟3个月持有期混合型基金中基金(FOF)集合资产管理计划
3     成立时间                                         2022-09-05
4     最新规模                                           2072.03万
5     基金公司                                       兴证证券资产管理有限公司
6     基金经理                                                斯苑蓓
7     托管银行                                       中国农业银行股份有限公司
8     基金类型                                           FOF-偏股混合
9     评级机构                                               <NA>
10    基金评级                                               暂无评级
11    投资策略  本集合计划坚持自上而下为主、自下而上为辅，把握“一个中心、四个基本点”，即以大类资产配置为中...
12    投资目标  本集合计划在有效控制组合风险的前提下，通过优选基金积极把握基金市场的投资机会，力求实现集合计...
13  业绩比较基准  中证偏股型基金指数收益率×70%+中债-综合全价（总值）指数收益率×25%+银行活期存款利率...
"""


class FundBaseInfoWidget(QWidget):
    def __init__(self, df: pd.DataFrame, parent=None, logger=None):
        super().__init__(parent)
        self.df = df
        self._log = logger
        self.init_ui()

    # 不知道为什么使用 QFormLayout 会导致文字最后几个文字显示不出来
    # def init_ui(self):
    #     form_layout = QFormLayout()

    #     # 遍历 DataFrame 的每一行，将 item 和 value 添加到 Form Layout 中
    #     for index, row in self.df.iterrows():
    #         item = row['item']
    #         value = row['value']

    #         # 处理缺失值
    #         if pd.isna(value) or pd.isnull(value):
    #             value = "-"

    #         # 太长了，缩短显示
    #         if item == "业绩比较基准":
    #             item = "比较基准"

    #         self._log.info(f"VALUE: {value}")
    #         # 创建 QLabel 并设置内容
    #         lb_item = QLabel(item)
    #         lb_value = QLabel(str(value))
    #         lb_value.setTextInteractionFlags(Qt.TextSelectableByMouse)  # 允许文本选择
    #         lb_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # 设置 QLabel 的大小策略
    #         lb_value.setWordWrap(True)  # 允许自动换行
    #         lb_value.adjustSize()  # 根据内容自动调整大小

    #         # 将标签添加到 Form Layout 中
    #         form_layout.setLabelAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    #         form_layout.addRow(lb_item, lb_value)

    #     # 设置布局
    #     self.setLayout(form_layout)
    #     self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(5)

        for row_index, (index, row) in enumerate(self.df.iterrows()):
            item = row['item']
            value = row['value']

            if pd.isna(value) or pd.isnull(value):
                value = "-"

            if item == "业绩比较基准":
                item = "比较基准"

            lb_item = QLabel(item)
            lb_item.setStyleSheet("font-weight: bold;")
            lb_item.setAlignment(Qt.AlignLeft)

            lb_value = QLabel(value)
            lb_value.setTextInteractionFlags(Qt.TextSelectableByMouse)
            lb_value.setWordWrap(True)
            lb_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

            grid_layout.addWidget(lb_item, row_index, 0, Qt.AlignLeft)
            grid_layout.addWidget(lb_value, row_index, 1)

        self.setLayout(grid_layout)
