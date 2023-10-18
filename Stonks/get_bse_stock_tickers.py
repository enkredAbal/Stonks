# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 04:36:09 2023

@author: woa8uh
"""

import pandas as pd
import requests
import datetime


url = "https://api.bseindia.com/BseIndiaAPI/api/ListofScripData/w"

params = {
    "Group": "",
    "Scripcode": "",
    "industry": "",
    "segment": "Equity",
    "status": "Active"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.bseindia.com/markets/equity/EQReports/MarketWatch.aspx"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()
df = pd.DataFrame(data)

file_name = "equity_active_data_" + str(datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")) + ".csv"
# Write the DataFrame to a CSV file
df.to_csv(file_name, index=False)