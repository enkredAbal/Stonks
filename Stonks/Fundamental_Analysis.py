# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 04:36:10 2023

@author: woa8uh
"""

# import yfinance as yf

# # Define the stock symbol
# symbol = 'ABB'

# # Retrieve the stock information
# stock = yf.Ticker(symbol)

# # # Retrieve the financial statements
# income_statement = stock.financials.loc['Total Revenue']
# balance_sheet = stock.balance_sheet.loc['Total Current Assets']
# cashflow_statement = stock.cashflow.loc['Total Cash From Operating Activities']

# # Perform financial ratio analysis
# total_assets = balance_sheet['Total Assets']
# total_liabilities = balance_sheet['Total Liab']
# total_equity = balance_sheet['Total Stockholder Equity']
# net_income = income_statement['Net Income']
# operating_cashflow = cashflow_statement['Total Cash From Operating Activities']

# # Compute key financial ratios
# profit_margin = net_income / income_statement['Total Revenue']
# return_on_assets = net_income / total_assets
# return_on_equity = net_income / total_equity
# current_ratio = balance_sheet['Total Current Assets'] / balance_sheet['Total Current Liabilities']
# debt_to_equity = total_liabilities / total_equity
# earnings_per_share = net_income / stock.info['sharesOutstanding']
# pe_ratio = stock.info['regularMarketPrice'] / earnings_per_share
# dividend_yield = stock.info['dividendRate'] / stock.info['regularMarketPrice']

# # Print the financial ratios
# print(f"Profit margin: {profit_margin:.2f}")
# print(f"Return on assets: {return_on_assets:.2f}")
# print(f"Return on equity: {return_on_equity:.2f}")
# print(f"Current ratio: {current_ratio:.2f}")
# print(f"Debt-to-equity ratio: {debt_to_equity:.2f}")
# print(f"Earnings per share: {earnings_per_share:.2f}")
# print(f"P/E ratio: {pe_ratio:.2f}")
# print(f"Dividend yield: {dividend_yield:.2%}")


# import requests

# # Define the stock symbol and API key
# symbol = 'ABB.BO'
# api_key = '3UUMUVROGWXYQZK3'

# # Retrieve the financial statements
# income_statement_url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}&datatype=json&market=INR'
# balance_sheet_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}&datatype=json&market=INR'
# cashflow_statement_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}&datatype=json&market=INR'

# income_statement = requests.get(income_statement_url).json()['annualReports'][0]
# balance_sheet = requests.get(balance_sheet_url).json()['annualReports'][0]
# cashflow_statement = requests.get(cashflow_statement_url).json()['annualReports'][0]

# # Perform financial ratio analysis
# total_assets = float(balance_sheet['totalAssets'])
# total_liabilities = float(balance_sheet['totalLiabilities'])
# total_equity = float(balance_sheet['totalShareholderEquity'])
# net_income = float(income_statement['netIncome'])
# operating_cashflow = float(cashflow_statement['operatingCashflow'])

# # Compute key financial ratios
# profit_margin = net_income / float(income_statement['totalRevenue'])
# return_on_assets = net_income / total_assets
# return_on_equity = net_income / total_equity
# current_ratio = float(balance_sheet['totalCurrentAssets']) / float(balance_sheet['totalCurrentLiabilities'])
# debt_to_equity = total_liabilities / total_equity
# earnings_per_share = float(requests.get(f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={api_key}').json()['annualEarnings'][0]['reportedEPS'])
# pe_ratio = float(requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}').json()['PERatio'])
# dividend_yield = float(requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}').json()['DividendYield'])

# # Print the financial ratios
# print(f"Profit margin: {profit_margin:.2f}")
# print(f"Return on assets: {return_on_assets:.2f}")
# print(f"Return on equity: {return_on_equity:.2f}")
# print(f"Current ratio: {current_ratio:.2f}")
# print(f"Debt-to-equity ratio: {debt_to_equity:.2f}")
# print(f"Earnings per share: {earnings_per_share:.2f}")
# print(f"P/E ratio: {pe_ratio:.2f}")
# print(f"Dividend yield: {dividend_yield:.2%}")

from yahooquery import Ticker
import pandas as pd

df_all_bse_stocks = pd.read_csv("equity_active_data.csv")
stock_tickers = df_all_bse_stocks['scrip_id'] + ".BO"

symbol = stock_tickers[4]

stock = Ticker(symbol, country = 'India')

#Perform quaterly financial fundamental analysis
quaterly = stock.all_financial_data(frequency="q")
quaters = quaterly[quaterly['NetIncome'].notna()]
recent_quater = quaters.iloc[-1] 

#Liquidity Ratios
try:
    current_assets = recent_quater['CurrentAssets']
except:
    current_assets = None
try:      
    current_liabilities = recent_quater['CurrentLiabilities']
except:
    current_liabilities = None
try:      
    inventory = recent_quater['Inventory']
except:
    inventory = None

try:      
    current_ratio = current_assets / current_liabilities
except:
    current_ratio = None
try:      
    quick_ratio = (current_assets - inventory) / current_liabilities 
except:
    quick_ratio = None
 
#Profitability Ratios
try:      
    gross_profit = recent_quater['GrossProfit']
except:
    gross_profit = None
try:      
    revenue = recent_quater['TotalRevenue']
except:
    revenue = None
try:      
    operating_income = recent_quater['OperatingIncome']
except:
    operating_income = None
try:      
    net_income = recent_quater['NetIncome']
except:
    net_income = None

try:      
    gross_profit_margin = (gross_profit / revenue) * 100
except:
    gross_profit_margin = None
try:      
    operating_profit_margin = (operating_income / revenue) * 100
except:
    operating_profit_margin = None
try:      
    net_profit_margin = (net_income / revenue) * 100
except:
    net_profit_margin = None

#Efficiency Ratios
try:      
    cogs = recent_quater['CostOfRevenue']
except:
    cogs = None
try:      
    inventory_values = quaters.Inventory
    average_inventory = sum(inventory_values) / len(inventory_values)
except:
    average_inventory = None
try:      
    accounts_recievable_values = quaters.AccountsReceivable
    average_accounts_recievable =  sum(accounts_recievable_values) / len(accounts_recievable_values)
except:
    average_accounts_recievable = None

try:      
    inventory_turnover = cogs / average_inventory
except:
    inventory_turnover = None
try:      
    recievables_turnover = revenue / average_accounts_recievable 
except:
    recievables_turnover = None

#Perform annualy financial fundamental 
annually = stock.all_financial_data(frequency="a")
years = annually[annually['TotalDebt'].notna()]
recent_year = annually.iloc[-1] 
prev_year = annually.iloc[-2]

#Solvency Ratios
try:      
    total_debt = recent_year['TotalDebt']
except:
    total_debt = None
try:      
    total_equity = recent_year['StockholdersEquity']
except:
    total_equity = None
try:      
    total_assets = recent_year['TotalAssets']
except:
    total_assets = None
try:      
    ebit = recent_year['EBIT']
except:
    ebit = None
try:      
    interest_expense = recent_year['InterestExpense']
except:
    interest_expense = None

try:      
    debt_to_equity_ratio = total_debt / total_equity 
except:
    debt_to_equity_ratio = None
try:      
    debt_ratio = total_debt / total_assets
except:
    debt_ratio = None
try:      
    interest_coverage_ratio = ebit / interest_expense
except:
    interest_coverage_ratio = None

#Return Ratios
try:      
    net_income = recent_year['NetIncome']
except:
    net_income = None
try:      
    average_total_assets = (recent_year['TotalAssets'] + prev_year['TotalAssets']) / 2
except:
    average_total_assets = None
try:      
    average_total_equity = (recent_year['StockholdersEquity'] + prev_year['StockholdersEquity']) / 2
except:
    average_total_equity = None
try:      
    total_investments_recent_year = recent_year['AvailableForSaleSecurities'] + recent_year['CashEquivalents'] + recent_year['CashFinancial'] + recent_year['HeldToMaturitySecurities'] + recent_year['InvestmentinFinancialAssets'] + recent_year['OtherShortTermInvestments']
    total_investments_prev_year = prev_year['AvailableForSaleSecurities'] + prev_year['CashEquivalents'] + prev_year['CashFinancial'] + prev_year['HeldToMaturitySecurities'] + prev_year['InvestmentinFinancialAssets'] + prev_year['OtherShortTermInvestments']
    average_total_investment = (total_investments_recent_year + total_investments_prev_year) / 2
except:
    average_total_investment = None

try:      
    roa = net_income / average_total_assets
except:
    roa = None
try:      
    roe = net_income / average_total_equity
except:
    roe = None
try:      
    roi = net_income / average_total_investment
except:
    roi = None

#EPS
try:      
    eps = recent_year['BasicEPS']
except:
    eps = None
#Growth Rates
try:      
    revenue_growth_rate = (recent_year['TotalRevenue'] - prev_year['TotalRevenue']) / prev_year['TotalRevenue']
except:
    revenue_growth_rate = None
try:      
    earnings_growth_rate = (recent_year['NetIncome'] - prev_year['NetIncome']) / prev_year['NetIncome']
except:
    earnings_growth_rate = None
try:      
    pe_ratio = stock.quotes[symbol]['trailingPE']
except:
    pe_ratio = None
try:      
    dividend_yield = stock.quotes[symbol]['trailingAnnualDividendYield']
except:
    dividend_yield = None    

# Print the financial ratios
print(symbol)
print("FOR THIS QUATER")
print("Liquidity Ratios:")
print(f"Current ratio: {current_ratio}")
print(f"Quick ratio: {quick_ratio}")
print("Profitability Ratios:")
print(f"Gross Profit margin: {gross_profit_margin}")
print(f"Operating Profit margin: {operating_profit_margin}")
print(f"Net Profit margin: {net_profit_margin}")
print("Efficiency Ratios:")
print(f"Inventory Turnover: {inventory_turnover}")
print(f"Recievables Turnover: {recievables_turnover}")
print("FOR THIS YEAR")
print("Solvency Ratios:")
print(f"Debt to Equity Ratio: {debt_to_equity_ratio}")
print(f"Debt Ratio: {debt_ratio}")
print(f"Interest Covereage Ratio: {interest_coverage_ratio}")
print("Return Ratios:")
print(f"Return on assets: {roa}")
print(f"Return on equity: {roe}")
print(f"Return on Investments: {roi}")
print(f"Earnings per share: {eps}")
print("Growth Rates:")
print(f"Revenue growth rate: {revenue_growth_rate}")
print(f"Earnings growth rate: {earnings_growth_rate}")
print(f"P/E ratio: {pe_ratio}")
print(f"Dividend yield: {dividend_yield}")




















































