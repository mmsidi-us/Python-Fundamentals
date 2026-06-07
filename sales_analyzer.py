import csv

# File path constants
DATA_FILE = "sales_data.csv"
REPORT_TXT = "sales_report.txt"
SUMMARY_CSV = "product_summary.csv"

# Storage structures for calculated data
total_revenue = 0.0
product_revenue = {}    # Format: { product_name: combined_revenue }
product_quantity = {}   # Format: { product_name: combined_quantity }
daily_revenue = {}      # Format: { date_string: combined_revenue }

# =====================================================================
# 1. Parsing and Aggregating Data via DictReader
# =====================================================================
try:
    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Safely extract values and convert from default string format
            product = row["product"]
            qty = int(row["quantity"])
            price = float(row["price"])
            date = row["date"]
            
            # Compute line item revenue
            row_revenue = qty * price
            
            # Aggregate global total revenue
            total_revenue += row_revenue
            
            # Track metrics per unique product item
            product_revenue[product] = product_revenue.get(product, 0.0) + row_revenue
            product_quantity[product] = product_quantity.get(product, 0) + qty
            
            # Accumulate daily metrics to isolate peak sales dates
            daily_revenue[date] = daily_revenue.get(date, 0.0) + row_revenue

except FileNotFoundError:
    print(f"❌ Error: Required input file '{DATA_FILE}' was not found. Please create it first.")
    exit()

# =====================================================================
# 2. Extracting Peak Performance Metrics (Highest Revenue Day)
# =====================================================================
best_day = None
max_daily_rev = 0.0

for day, rev in daily_revenue.items():
    if rev > max_daily_rev:
        max_daily_rev = rev
        best_day = day

# =====================================================================
# 3. Generating the Human-Readable Document (sales_report.txt)
# =====================================================================
with open(REPORT_TXT, mode="w", encoding="utf-8") as text_file:
    text_file.write("=========================================\n")
    text_file.write("         SALES ANALYSIS REPORT           \n")
    text_file.write("=========================================\n\n")
    
    text_file.write(f"Total Combined Revenue: ${total_revenue:,.2f}\n")
    text_file.write(f"Highest Revenue Day:    {best_day} (${max_daily_rev:,.2f})\n\n")
    
    text_file.write("Breakdown Per Product:\n")
    text_file.write("-" * 45 + "\n")
    text_file.write(f"{'Product':<15}{'Qty Sold':<15}{'Total Revenue':<15}\n")
    text_file.write("-" * 45 + "\n")
    
    for prod in sorted(product_revenue.keys()):
        text_file.write(
            f"{prod:<15}{product_quantity[prod]:<15}${product_revenue[prod]:<14.2f}\n"
        )
    text_file.write("-" * 45 + "\n")

print(f"✅ Formatted narrative summary generated: {REPORT_TXT}")

# =====================================================================
# 4. Generating the Machine-Readable Summary (product_summary.csv)
# =====================================================================
with open(SUMMARY_CSV, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["product", "total_quantity", "total_revenue"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Commit headers to file
    writer.writeheader()
    
    # Process rows for each calculated artifact
    for prod in sorted(product_revenue.keys()):
        writer.writerow({
            "product": prod,
            "total_quantity": product_quantity[prod],
            "total_revenue": round(product_revenue[prod], 2)
        })

print(f"✅ Product metrics CSV summary generated: {SUMMARY_CSV}")