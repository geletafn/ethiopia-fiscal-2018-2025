# generate_analysis.py
# Creates ethiopia_fred_analysis.xlsx with 4 sheets: Data, Summary, Charts, Trends
# Run: python generate_analysis.py

import pandas as pd
import numpy as np

# === 1. DATA SHEET ===
data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Total Exp. (% GDP)': [18.5, 18.2, 19.0, 18.8, 19.5, 20.1, 21.0, 21.5],
    'GDP (ETB Bn)': [2090, 2472, 2895, 3537, 4113, 4830, 7395, 8977],
    'Total Exp. (ETB Bn)': [387, 450, 550, 665, 802, 971, 1553, 1930],
    'War (ETB Bn)': [45, 50, 70, 100, 120, 146, 150, 290],
    '% War': [11.6, 11.1, 12.7, 15.0, 15.0, 15.0, 9.7, 15.0],
    'Green (ETB Bn)': [35, 40, 45, 50, 60, 70, 54, 106],
    '% Green': [9.0, 8.9, 8.2, 7.5, 7.5, 7.2, 3.5, 5.5],
    'Social (ETB Bn)': [140, 160, 180, 200, 240, 280, 158, 307],
    '% Social': [36.2, 35.6, 32.7, 30.1, 29.9, 28.8, 10.2, 15.9],
    'Debt (ETB Bn)': [30, 35, 45, 60, 100, 139, 200, 386],
    '% Debt': [7.8, 7.8, 8.2, 9.0, 12.5, 14.3, 12.9, 20.0],
    'Recurrent %': [26.2, 26.2, 30.0, 36.0, 40.0, 44.0, 46.5, 61.4],
    'Capital %': [73.8, 73.8, 70.0, 64.0, 60.0, 56.0, 29.1, 18.9]
}
df = pd.DataFrame(data)

# === 2. SUMMARY SHEET ===
summary = pd.DataFrame({
    'Metric': ['Total Growth', 'War Surge', 'Debt Crisis', 'Recurrent 2025'],
    'Value': ['398%', '544%', '1187%', '61.4%'],
    'Insight': [
        'Fiscal expansion + birr devaluation',
        'Tigray/Amhara conflict peak',
        '2023 default → IMF ECF relief',
        'Capital retreat → infrastructure lag'
    ]
})

# === 3. TRENDS SHEET ===
trends = pd.DataFrame({
    'Trend': ['War Finance', 'Green Infra', 'Social Spending', 'Debt Service'],
    '2018 (ETB Bn)': [45, 35, 140, 30],
    '2025 (ETB Bn)': [290, 106, 307, 386],
    'Change': ['+545%', '+203%', '+119%', '+1187%'],
    'Insight': [
        'Conflict-driven surge',
        'GERD stable, share down',
        'Inflation erosion',
        'ECF restructuring needed'
    ]
})

# === 4. WRITE TO EXCEL WITH CHARTS ===
with pd.ExcelWriter('ethiopia_fred_analysis.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    summary.to_excel(writer, sheet_name='Summary', index=False)
    trends.to_excel(writer, sheet_name='Trends', index=False)
    
    # Add Charts Sheet
    workbook = writer.book
    chart_sheet = workbook.create_sheet('Charts')
    
    # Line Chart: Total Expenditure
    from openpyxl.chart import LineChart, Reference
