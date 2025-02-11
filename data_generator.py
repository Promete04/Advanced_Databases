import csv
import random

# File name
output_file = "products_data.csv"

# Number of records
num_records = 25000000

# Generate the CSV file
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "name", "stock", "price"])  # Header row

    for product_id in range(1, num_records + 1):
        name = f"Product_{product_id}"
        stock = random.randint(0, 20000)
        price = round(random.uniform(10, 5000), 2)
        writer.writerow([product_id, name, stock, price])

print(f"CSV file '{output_file}' generated successfully with {num_records} records.")
