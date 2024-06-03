# -*- coding: utf-8 -*-
"""
    **Gen_Pnf_With_Zerodha_Kite_Data.py**
    
    - Copyright (c) 2019, KNC Solutions Private Limited.
    - License: 'Apache License, Version 2.0'.
    - version: 1.0.0
"""

import pandas as pd
import datetime
from collections import OrderedDict, Counter
from kiteconnect import KiteConnect
from kiteconnect import exceptions
import requests
from PnfChartGen.Parameters import *
from PnfChartGen.CredentialLoader import KITE_API_KEY_ACCESS_TOKEN
from PnfChartGen.ChartGenerator import ChartGenerator

class Gen_Pnf_With_Zerodha_Kite_Data:
    """
    This class generates point and figure chart after extracting data from zerodha kite historical api.
    """
    def __init__(self):
        # Load Kite Connect credentials
        self.__credentials = KITE_API_KEY_ACCESS_TOKEN.get_kite_credentials()

        # Load configuration from an Excel file
        self.__config = pd.read_excel('settings/dhelm_pnf_chart_gen_settings.xlsx')

        # Initialize Kite Connect client and set access token
        self.__client = KiteConnect(self.__credentials[0])
        self.__client.set_access_token(self.__credentials[1])

        # Set from_date and to_date variables
        self.__from_date = (self.__config.at[self.__config.first_valid_index(), 'from_dt']).strftime("%Y-%m-%d %H:%M:%S")
        self.__to_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Load list of stocks from a CSV file
        self.__list_stocks = pd.read_csv('settings/kite_chart_gen_list.csv')

        # Set box_type variable based on method_percentage configuration
        if self.__config.at[self.__config.first_valid_index(), 'method_percentage']:
            self.__box_type = Types.Method_percentage
        else:
            self.__box_type = Types.Method_value

        # Set calculation_method variable based on method_percentage configuration
        if 'close' in self.__config.at[self.__config.first_valid_index(), 'calculation_method']:
            self.__calculation_method = Types.Method_close
        else:
            self.__calculation_method = Parameters.Types.Method_highlow

        # Set box_size, reversal, and box_percentage variables from configuration
        self.__box_size = (self.__config.at[self.__config.first_valid_index(), 'BOX_SIZE'])
        self.__reversal = (self.__config.at[self.__config.first_valid_index(), 'REVERSAL'])
        self.__box_percentage = (self.__config.at[self.__config.first_valid_index(), 'BOX_PERCENTAGE'])

        # Set folder variable for storing generated charts
        self.__folder = 'charts_kite'

        # Iterate through list of stocks and generate point and figure charts
        for index, row in self.__list_stocks.iterrows():
            self.__data_historical = self.__get_historical_data(row)
            print('Generating point and figure chart for ' + row['tradingsymbol'])
            ChartGenerator.gen_chart(self.__data_historical,
                                     row['tradingsymbol'],
                                     row['exchange'],
                                     self.__box_type,
                                     self.__calculation_method,
                                     self.__reversal,
                                     self.__box_size,
                                     self.__box_percentage,
                                     self.__folder)
            print('DONE..Check for chart in the folder ' + self.__folder + '.')

    def __get_historical_data(self, row):
        # Fetch historical data from Zerodha Kite API
        hist = None
        df = pd.DataFrame()
        try:
            hist = self.__client.historical_data(int(row['instrument_token']), self.__from_date, self.__to_date, 'day', False)
        except (requests.exceptions.ReadTimeout, exceptions.NetworkException):
            pass
        except Exception:
            pass

        # Process fetched data and return a DataFrame
        if hist is not None:
            for entry in hist:
                if 'date' in entry:
                    entry['date'] = str(entry['date'])
            col = Counter()
            for k in list(hist):
                col.update(k)
                df = pd.DataFrame([k.values() for k in hist], columns=col.keys())
        return df
