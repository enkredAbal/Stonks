import pandas as pd
import numpy as np
import datetime
import glob
import os.path


# Load the ratios dataframe
ratios_file_type =  'stock_ratios_*'
ratios_files = glob.glob(ratios_file_type)
ratios_max_file = max(ratios_files, key=os.path.getctime)
ratios_df = pd.read_csv(ratios_max_file)


# Load the stock information dataframe
stocks_file_type =  'equity_active_data_*'
stocks_files = glob.glob(stocks_file_type)
stocks_max_file = max(stocks_files, key=os.path.getctime)
stock_info_df = pd.read_csv(stocks_max_file)
stock_info_df['scrip_id'] = stock_info_df['scrip_id'] + ".BO"
# Merge the ratios and stock information dataframes based on the symbol
merged_df = pd.merge(ratios_df, stock_info_df, left_on="Symbol", right_on="scrip_id", how="left")

merged_df = merged_df.replace([np.inf, -np.inf], np.nan)

# Define the desirable direction for each ratio (1 for higher is better, -1 for lower is better)
ratio_direction = {
    "Current Ratio": 1,
    "Quick Ratio": 1,
    "Gross Profit Margin": 1,
    "Operating Profit Margin": 1,
    "Net Profit Margin": 1,
    "Inventory Turnover": -1,
    "Receivables Turnover": -1,
    "Debt to Equity Ratio": -1,
    "Debt Ratio": -1,
    "Interest Coverage Ratio": 1,
    "Return on Assets": 1,
    "Return on Equity": 1,
    "Return on Investments": 1,
    "Earnings per Share": 1,
    "Revenue Growth Rate": 1,
    "Earnings Growth Rate": 1,
    "P/E Ratio": -1,
    "Dividend Yield": 1
}

# Calculate the average ratios per industry, considering the direction of each ratio
average_ratios_per_industry = merged_df.groupby("INDUSTRY").apply(
    lambda x: x.iloc[:, 1:-12].apply(
        lambda y: np.nanmean(y * ratio_direction[y.name]) if np.isfinite(y).any() else np.nan
    )
)

# Calculate the overall average ratios, considering the direction of each ratio
overall_average_ratios = merged_df.iloc[:, 1:-12].apply(
    lambda y: np.nanmean(y * ratio_direction[y.name]) if np.isfinite(y).any() else np.nan
)

merged_df.groupby("INDUSTRY").apply(
    lambda x: x.iloc[:, 1:-12].apply(
        lambda y: print(average_ratios_per_industry[x["INDUSTRY"][y.name]])
    )
)

# Calculate the scores for each stock based on the average ratios per industry
merged_df["Score"] = merged_df.groupby("INDUSTRY").apply(
    lambda x: x.iloc[:, 1:-12].apply(
        lambda y: (y * ratio_direction[y.name] - average_ratios_per_industry[x["INDUSTRY"][y.name]]) / np.nanstd(y * ratio_direction[y.name]) if np.isfinite(y).any() else np.nan
    )
).values.flatten()

# Calculate the cutoff score for selecting the top 30% stocks
cutoff_score = np.nanpercentile(merged_df["Score"], 70)

# Select the top performing 30% stocks based on the scores
top_stocks = merged_df[merged_df["Score"] > cutoff_score]

# Sort the top stocks based on the score in descending order
top_stocks = top_stocks.sort_values(by="Score", ascending=False)


# Save the top performing stocks to a new CSV file
top_stocks.to_csv("top_performing_stocks.csv", index=False)
