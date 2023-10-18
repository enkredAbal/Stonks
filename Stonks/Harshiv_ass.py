# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 04:36:09 2023

@author: Ishaan Kohli
"""

import pandas as pd
import requests


years = ['2022', '2021', '2020', '2019', '2018']
df_all_years_statewise = pd.DataFrame()
print("statewise")
for year in years:
    print(year)
    url = "https://pmfby.gov.in/goiConfig/getAdminDashboardStateWiseReport?year="+year+"&seasonCode=&schemeCode=&isCombined="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    
    data1 = data['data']
    
    df = pd.DataFrame(data1)
    df_all_years_statewise = pd.concat([df_all_years_statewise, df], axis= 0)
    name = year+"_statewise.csv"
    # Write the DataFrame to a CSV file
    df.to_csv(name, index=False)

df_all_years_statewise.to_csv("statewise.csv", index=False)    

state_codes = df_all_years_statewise['stateCode'].unique()
season_codes = df_all_years_statewise['season'].unique()
print("districtwise")

df_all_years_districtwise = pd.DataFrame()

for state_code in state_codes:
    print(state_code)
    for year in years:
        for season_code in season_codes:
            url_district = "https://pmfby.gov.in/goiConfig/getAdminDashboardDistrictWiseReport?year="+year+"&seasonCode="+season_code+"&schemeCode=&stateCode="+state_code+"&isCombined="
        
            response = requests.get(url_district, headers=headers)
        
            data = response.json()
        
            data2 = data['data']
        
            df = pd.DataFrame(data2)
            df_all_years_districtwise = pd.concat([df_all_years_districtwise, df], axis= 0)

df_all_years_districtwise.to_csv("districtwise.csv", index=False) 

level_code_params = df_all_years_districtwise['nextLevelParams'].unique()
scheme_codes = df_all_years_statewise['scheme'].unique()
print("levelwise")

df_all_years_levelwise = pd.DataFrame()

for level_code_param in level_code_params:
    print(level_code_param)
    for scheme in scheme_codes:
        substring = "schemeCode="+scheme
        level_code_param = level_code_param.replace("schemeCode=undefined", substring)
        url_level = "https://pmfby.gov.in/goiConfig/getAdminDashboardLevelCoverageReport?"+level_code_param
        response = requests.get(url_level, headers=headers)
        
        data = response.json()
        
        data3 = data['data']
        
        df = pd.DataFrame(data3)
        df_all_years_levelwise = pd.concat([df_all_years_levelwise, df], axis= 0)

df_all_years_levelwise.to_csv("levelwise.csv", index=False) 

level_code_params2 = df_all_years_levelwise['nextLevelParams'].unique()
print("levelwise2")

df_all_years_levelwise2 = pd.DataFrame()

for level_code_param in level_code_params2:
    print(level_code_param)
    for scheme in scheme_codes:
        substring = "schemeCode="+scheme
        level_code_param = level_code_param.replace("schemeCode=undefined", substring)
        url_level = "https://pmfby.gov.in/goiConfig/getAdminDashboardLevelCoverageReport?"+level_code_param
        response = requests.get(url_level, headers=headers)
        
        data = response.json()
        
        data4 = data['data']
        
        df = pd.DataFrame(data4)
        df_all_years_levelwise2 = pd.concat([df_all_years_levelwise2, df], axis= 0)

df_all_years_levelwise2.to_csv("levelwise_level4.csv", index=False) 

level_code_params3 = df_all_years_levelwise2['nextLevelParams'].unique()
print("levelwise3")

df_all_years_levelwise3 = pd.DataFrame()

for level_code_param in level_code_params3:
    print(level_code_param)
    for scheme in scheme_codes:
        substring = "schemeCode="+scheme
        level_code_param = level_code_param.replace("schemeCode=undefined", substring)
        url_level = "https://pmfby.gov.in/goiConfig/getAdminDashboardLevelCoverageReport?"+level_code_param
        response = requests.get(url_level, headers=headers)
        
        data = response.json()
        
        data5 = data['data']
        
        df = pd.DataFrame(data5)
        df_all_years_levelwise3 = pd.concat([df_all_years_levelwise3, df], axis= 0)

df_all_years_levelwise3.to_csv("levelwise_level5.csv", index=False) 

level_code_params4 = df_all_years_levelwise3['nextLevelParams'].unique()
print("levelwise4")

df_all_years_levelwise4 = pd.DataFrame()

for level_code_param in level_code_params4:
    print(level_code_param)
    for scheme in scheme_codes:
        substring = "schemeCode="+scheme
        level_code_param = level_code_param.replace("schemeCode=undefined", substring)
        url_level = "https://pmfby.gov.in/goiConfig/getAdminDashboardLevelCoverageReport?"+level_code_param
        response = requests.get(url_level, headers=headers)
        
        data = response.json()
        
        data6 = data['data']
        
        df = pd.DataFrame(data6)
        df_all_years_levelwise4 = pd.concat([df_all_years_levelwise4, df], axis= 0)

df_all_years_levelwise4.to_csv("levelwise_level6.csv", index=False) 