# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:57:27 2018

@author: xumengting
"""

import tushare as ts
import pandas as pd
import numpy as np

pro = ts.pro_api()

def daily_price_rate(ts_code_list='',
                     trade_date='',
                     price_change_thres=8):
    '''
    :param ts_code_list: default is whole A-shares stock of SH and SZ markets.
    :param trade_date: trade date, default is
    :param price_change_thres: price change threshold, default 8
    :return: ratio (the stock amount of daily price change more than price_thres
            divided by the amount of stocks list)
    '''
    if ts_code_list == '':
        df = pro.query('daily',trade_date=trade_date)
    else:
        if isinstance(ts_code_list,list):
            df = pro.query('daily',trade_date=trade_date).query(
                'ts_code in {ts_code_list}'.format(ts_code_list=ts_code_list))
        else:
            df = pd.DataFrame()
    if df.shape[0]==0:
        return -1
    else:
        df_up =  df.query('pct_change>={price_change_thres}'.format(price_change_thres=price_change_thres))
        return df_up.shape[0]/df.shape[0]

