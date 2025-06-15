import csv
import os
import zipfile
from datetime import date

# Create directory for CSV files
os.makedirs("crypto_trading_sheets", exist_ok=True)

# Tab 1: ReadMe_Instructions
with open('crypto_trading_sheets/ReadMe_Instructions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Column A", "Column B"])
    writer.writerow(["Sheet Name:", "Crypto Trading Platform & Infrastructure Guide"])
    writer.writerow(["Purpose:", "Comprehensive guide for professional crypto trading setup and management"])
    writer.writerow(["Instructions:", "1. Navigate Tabs\n2. Review Content\n3. Customize\n4. Ethiopian Context"])
    writer.writerow(["Date Created:", str(date.today())])
    writer.writerow(["Last Updated:", str(date.today())])

# Tab 2: I_Market_Data (simplified example)
with open('crypto_trading_sheets/I_Market_Data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Category", "Best Tools", "Usage", "Checklist", "Templates", "Alerts"])
    writer.writerow([
        "Real-time Market Data", 
        "TradingView, CoinMarketCap", 
        "Pre-trade analysis, In-trade monitoring", 
        "Account setup, Chart customization", 
        "Chart layouts, Indicator presets", 
        "Price alerts, Indicator alerts"
    ])
    writer.writerow([
        "Fundamental Analysis", 
        "Glassnode, Messari", 
        "Project assessment, On-chain analysis", 
        "Explore metrics, Read reports", 
        "Dashboards, Research templates", 
        "Anomaly alerts, Metric thresholds"
    ])

# Add similar sections for other tabs (III to VII) following the same pattern

# Create ZIP file
with zipfile.ZipFile('crypto_trading_platform_guide.zip', 'w') as zipf:
    for file in os.listdir("crypto_trading_sheets"):
        zipf.write(f"crypto_trading_sheets/{file}", arcname=file)

print("Google Sheet files created in 'crypto_trading_sheets' folder")
print("ZIP file created: crypto_trading_platform_guide.zip")