import pandas as pd
class Quandl_API_KEY:
    @staticmethod
    def get_quandl_api_key():
        data = pd.read_csv('settings/quandl_credentials.csv')
        if data.at[data.first_valid_index(), 'api_key'] is None:
            raise Exception('Api key is empty or invalid.')
        return data.at[data.first_valid_index(), 'api_key']


class Gfeed_URI_API_KEY:
    @staticmethod
    def get_gfeed_uri_api_key():
        data = pd.read_csv('settings/gfeed_credentials.csv')
        if data.at[data.first_valid_index(), 'gfeed_ws_endpoint'] is None:
            raise Exception('Api key is empty or invalid.')
        if data.at[data.first_valid_index(), 'gfeed_api_key'] is None:
            raise Exception('Api key is empty or invalid.')
        return [data.at[data.first_valid_index(), 'gfeed_ws_endpoint'], data.at[data.first_valid_index(), 'gfeed_api_key']]

class KITE_API_KEY_ACCESS_TOKEN:
    @staticmethod
    def get_kite_credentials():
        data = pd.read_csv('settings/kite_credentials.csv')
        if data.at[data.first_valid_index(), 'api_key'] is None:
            raise Exception('Api key is empty or invalid.')
        if data.at[data.first_valid_index(), 'access_token'] is None:
            raise Exception('Api key is empty or invalid.')
        return [data.at[data.first_valid_index(), 'api_key'], data.at[data.first_valid_index(), 'access_token']]