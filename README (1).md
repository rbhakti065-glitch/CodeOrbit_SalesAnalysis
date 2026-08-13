# Data Cleaning in Excel/Python — CodeOrbit Tech Internship

## Objective
Take a small sample sales dataset and clean it: handle missing values,
duplicates, and formatting issues, using Python (pandas).

## Files
| File | Description |
|---|---|
| `generate_raw_data.py` | Generates the intentionally messy sample dataset (for reproducibility) |
| `raw_sales_data.csv` | The raw, uncleaned dataset |
| `clean_data.py` | The cleaning script — run this to reproduce the cleaned output |
| `cleaned_sales_data.csv` | Final cleaned dataset (CSV) |
| `cleaned_sales_data.xlsx` | Final cleaned dataset, formatted for presentation, with a second sheet showing the cleaning log |
| `cleaning_log.txt` | Plain-text log of every cleaning step applied |

## Issues found in the raw data
- **Duplicate rows** — 3 exact duplicate order records
- **Inconsistent text formatting** — `Region` and `Product` had mixed
  casing and stray whitespace (e.g. `" west"`, `"NORTH "`, `"east"`)
- **Mixed date formats** — `Order Date` mixed `YYYY-MM-DD` and `DD/MM/YYYY`
- **Price stored as text** — some `Unit Price` values included a `$` prefix,
  making the column non-numeric
- **Missing values** — gaps in `Quantity`, `Region`, and `Customer`

## Cleaning steps applied (`clean_data.py`)
1. **Load** the raw CSV.
2. **Remove duplicates** with `drop_duplicates()`.
3. **Standardize text** — strip whitespace and apply Title Case to `Region`
   and `Product`.
4. **Standardize dates** — parse both date formats into a single datetime
   column.
5. **Clean prices** — strip `$` symbols and cast `Unit Price` to float.
6. **Handle missing values**:
   - `Quantity` → filled with the column median (robust to outliers)
   - `Region` → filled with `"Unknown"` rather than guessing a region
   - `Customer` → filled with `"Unknown Customer"`
7. **Fix data types** — `Quantity` and `OrderID` cast to integer.
8. **Add a calculated column** — `Total Sales = Quantity * Unit Price`
   (useful for downstream analysis).
9. **Sort** rows chronologically by `Order Date`.
10. **Save** cleaned data to CSV and a formatted Excel workbook.

## How to reproduce
```bash
pip install pandas openpyxl
python generate_raw_data.py   # creates raw_sales_data.csv
python clean_data.py          # creates cleaned_sales_data.csv + cleaning_log.txt
python make_excel.py          # creates the formatted cleaned_sales_data.xlsx
```

## Result
- Raw dataset: 63 rows, 7 columns, with duplicates and missing/malformed values
- Cleaned dataset: 60 rows, 8 columns, **zero missing values**, consistent
  formatting throughout, ready for analysis
