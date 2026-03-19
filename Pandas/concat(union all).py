import pandas as pd

# -------------------------------------------------
# Example 1 : Vertical Concat (like UNION ALL)
# -------------------------------------------------

sales_jan = pd.DataFrame({
    "order_id": [1, 2, 3],
    "product": ["Laptop", "Mouse", "Keyboard"],
    "amount": [800, 20, 50]
})

sales_feb = pd.DataFrame({
    "order_id": [4, 5, 6],
    "product": ["Monitor", "Laptop", "Mouse"],
    "amount": [200, 900, 25]
})

print("JAN SALES")
print(sales_jan)
print()

print("FEB SALES")
print(sales_feb)
print()

combined_sales = pd.concat([sales_jan, sales_feb], ignore_index=True)

print("COMBINED SALES (VERTICAL CONCAT)")
print(combined_sales)
print()


# -------------------------------------------------
# Example 2 : Horizontal Concat (add columns)
# -------------------------------------------------

customer_ids = pd.DataFrame({
    "customer_id": [101, 102, 103]
})

customer_names = pd.DataFrame({
    "name": ["Alice", "Bob", "John"]
})

customers = pd.concat([customer_ids, customer_names], axis=1)

print("CUSTOMERS (HORIZONTAL CONCAT)")
print(customers)
print()


# -------------------------------------------------
# Example 3 : Different Columns
# -------------------------------------------------

df1 = pd.DataFrame({
    "id": [1, 2],
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "id": [3, 4],
    "age": [25, 30]
})

combined_diff = pd.concat([df1, df2], ignore_index=True)

print("CONCAT WITH DIFFERENT COLUMNS")
print(combined_diff)
print()