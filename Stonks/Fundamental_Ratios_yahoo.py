# -*- coding: utf-8 -*-
"""
Created on Mon May  8 03:58:30 2023

@author: woa8uh
"""

from yahooquery import Ticker
import pandas as pd
import datetime
import glob
import os.path

stocks_file_type =  'equity_active_data_*'
stocks_files = glob.glob(stocks_file_type)
stocks_max_file = max(stocks_files, key=os.path.getctime)
df_all_bse_stocks = pd.read_csv(stocks_max_file)
stock_tickers = df_all_bse_stocks['scrip_id'] + ".BO"

# Create a new DataFrame to store the calculated ratios
ratios_df = pd.DataFrame(columns=[
    "Symbol", "Current Ratio", "Quick Ratio", "Gross Profit Margin", "Operating Profit Margin",
    "Net Profit Margin", "Inventory Turnover", "Receivables Turnover", "Debt to Equity Ratio",
    "Debt Ratio", "Interest Coverage Ratio", "Return on Assets", "Return on Equity",
    "Return on Investments", "Earnings per Share", "Revenue Growth Rate",
    "Earnings Growth Rate", "P/E Ratio", "Dividend Yield"
])
for symbol in stock_tickers:
    print(symbol)
    stock = Ticker(symbol, country = 'India')
    
    #Perform quaterly financial fundamental analysis
    quaterly = stock.all_financial_data(frequency="q")
    if('data unavailable' not in quaterly):
        quaters = quaterly[quaterly['TotalAssets'].notna()]
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
            receivables_turnover = revenue / average_accounts_recievable 
        except:
            receivables_turnover = None
    else:
        current_ratio = None
        quick_ratio = None
        gross_profit_margin = None
        operating_profit_margin = None
        net_profit_margin = None
        inventory_turnover = None
        receivables_turnover = None
    
    #Perform annualy financial fundamental 
    annually = stock.all_financial_data(frequency="a")
    if('data unavailable' not in annually): 
        years = annually[annually['TotalAssets'].notna()]
        recent_year = annually.iloc[-1] 
        if(len(years) > 1):
            prev_year = annually.iloc[-2]
        else:
            prev_year = annually.iloc[-1]
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
            earnings_growth_rate = (net_income - prev_year['NetIncome']) / prev_year['NetIncome']
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
    else:
        debt_to_equity_ratio = None
        debt_ratio = None
        interest_coverage_ratio = None
        roa = None
        roe = None
        roi = None
        eps = None
        revenue_growth_rate = None
        earnings_growth_rate = None
        pe_ratio = None
        dividend_yield = None
        
       # Add the calculated ratios to the DataFrame
    ratios_df = ratios_df.append({
        "Symbol": symbol,
        "Current Ratio": current_ratio,
        "Quick Ratio": quick_ratio,
        "Gross Profit Margin": gross_profit_margin,
        "Operating Profit Margin": operating_profit_margin,
        "Net Profit Margin": net_profit_margin,
        "Inventory Turnover": inventory_turnover,
        "Receivables Turnover": receivables_turnover,
        "Debt to Equity Ratio": debt_to_equity_ratio,
        "Debt Ratio": debt_ratio,
        "Interest Coverage Ratio": interest_coverage_ratio,
        "Return on Assets": roa,
        "Return on Equity": roe,
        "Return on Investments": roi,
        "Earnings per Share": eps,
        "Revenue Growth Rate": revenue_growth_rate,
        "Earnings Growth Rate": earnings_growth_rate,
        "P/E Ratio": pe_ratio,
        "Dividend Yield": dividend_yield
    }, ignore_index=True)

file_name = "stock_ratios_" + str(datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")) + ".csv"
# Save the ratios DataFrame to a CSV file
ratios_df.to_csv(file_name, index=False)
