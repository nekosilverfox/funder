# This Python file uses the following encoding: utf-8

import pandas as pd
import akshare as ak
from logger import Logger


class Common:
    _all_fund = None
    _log = Logger.get_logger()

    def __init__(self):
        pass

    @classmethod
    def reload_all_fund(cls):
        cls._log.info("获取所有基金列表中...")
        all_fund = ak.fund_name_em()  # 所有基金
        cls._log.info("获取所有基金列表完成")

        cls._log.info("获取所有基金申购状态...")
        fund_purchase_state = ak.fund_purchase_em()  # 基金申购状态
        cls._log.info("获取所有基金申购状态")

        # 合并选择的基金和申购状态
        cls._log.info("合并基金列表及申购状态...")
        merged_df = pd.merge(all_fund, fund_purchase_state,
                             on="基金代码",
                             how="inner",
                             suffixes=("", "_r"))

        # 删除重复列
        cls._log.info("删除重复列...")
        columns_to_drop = [col for col in merged_df.columns if col.endswith("_r")]
        merged_df = merged_df.drop(columns=columns_to_drop)
        cls._all_fund = merged_df.drop(columns=["序号", "拼音全称"])

        cls._log.info("获取所有基金数据完成")
        cls._log.info(cls._all_fund)
        return cls._all_fund

    @classmethod
    def get__all_fund(cls):
        return cls._all_fund
