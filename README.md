
[[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14678901.svg)](https://doi.org/10.5281/zenodo.14678901)
](https://doi.org/10.5281/zenodo.17561561)
# Ethiopia Federal Budget Dataset (2018–2025)

**Open-access fiscal panel | FRED + IMF + MoFED**  
**Total: ETB 387B → 1,930B (+398%) | War: +545% | Debt: +1187%**

[Download Excel](https://github.com/geletafn/ethiopia-fiscal-2018-2025/raw/main/ethiopia_fred_analysis.xlsx)
---

## **Project Overview**  
This repository provides **cleaned, citable, and reproducible fiscal data** for Ethiopia from **2018 to 2025**, covering the **post-EPRDF transition** under Prime Minister Abiy Ahmed.  

**Core Question**:  
> **How did war finance, green ambition, IMF liberalisation, and inflation reshape public expenditure in Ethiopia?**  

---

## **Key Features**  
| Feature | Description |
|--------|-------------|
| **8-Year Time Series** | Gregorian FY 2018–2025 (actuals + 2025 IMF projection) |
| **Disaggregated Categories** | War Finance, Green Infrastructure, Social Spending, Debt Service |
| **Nominal ETB Values** | Total expenditure: **ETB 387B → 1,930B** (+398%) |
| **Reproducible** | Python/R scripts for FRED, World Bank, MoFED extraction |
| **Open Science** | CSV, Excel, Charts, Citation-ready |

---

## **Data Sources**  
| Source | Indicator | Link |
|-------|----------|------|
| **FRED (IMF)** | `ETHGGXG01GDPPT` – Total Exp. (% GDP) | [FRED Link](https://fred.stlouisfed.org/series/ETHGGXG01GDPPT) |
| **World Bank WDI** | `GC.XPN.TOTL.GD.ZS` | [WDI CSV](https://databank.worldbank.org/source/world-development-indicators) |
| **MoFED** | Citizens’ Budget 2018–2025 | [MoFED Budgets](https://www.mofed.gov.et/resources/budget/) |
| **IMF ECF Reviews** | 2023–2025 Projections | [IMF Ethiopia](https://www.imf.org/en/Countries/ETH) |

---

## **Files in This Repository**  

| File | Description |
|------|-----------|
| `ethiopia_budget_2018_2025_clean.csv` | Cleaned annual data (ETB Bn, % shares) |
| `ethiopia_fred_analysis.xlsx` | Excel with auto-charts & YoY growth |
| `scripts/extract_fred.py` | Python: Download → Clean → Plot |
| `charts/expenditure_trend.png` | Total exp. trend (2018–2025) |
| `charts/category_stack.png` | War/Green/Social/Debt breakdown |
| `CITATION.cff` | Auto-generated citation (Zenodo-ready) |

---

## **Quick Start (Python)**  
```bash
pip install pandas matplotlib requests
python scripts/extract_fred.py
