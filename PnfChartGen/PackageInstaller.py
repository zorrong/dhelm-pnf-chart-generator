# -*- coding: utf-8 -*-
"""
    **PackageInstaller.py**
    -----------------------
    - Copyright (c) 2019, KNC Solutions Private Limited.
    - License: 'Apache License, Version 2.0'.
    - version: 1.0.0

    This script is designed to install required Python packages if they are not already installed.
"""

import subprocess
import sys

try:
    import pandas as pd  # Importing pandas library
except ImportError:
    print('Pandas is not installed, installing it now')
    subprocess.call(['pip', 'install', 'pandas'])  # Installing pandas if not found


class install_packages:
    @staticmethod
    def install():
        """
        This method checks for required packages and installs them if not found.
        """
        df = pd.read_csv('package_status.csv')  # Reading package_status.csv file
        print("Please Wait...")

        if df.at[df.first_valid_index(), 'a'] == 1:
            return

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        package_list = ['pandas',
                        'XlsxWriter',
                        'pytz',
                        'tzlocal',
                        'DhelmGfeedClient',
                        'Quandl',
                        'kiteconnect'
                        ]

        for item in package_list:
            if item not in installed_packages:
                print(item)
                subprocess.call(['pip', 'install', 'DateTime'])  # Installing the missing package

        success = True
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        for item in package_list:
            if item not in installed_packages:
                success = False

        if success:
            df.loc[df.first_valid_index(), 'a'] = 1
            df.to_csv('package_status.csv', encoding='utf-8', index=False)
