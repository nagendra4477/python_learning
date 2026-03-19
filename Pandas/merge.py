import pandas as pd

# -------------------------------
# Orders DataFrame
# -------------------------------
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 103, 104, 105],
    "amount": [500, 700, 300, 900, 1100]
})

# -------------------------------
# Customers DataFrame
# Notice it also has "amount"
# -------------------------------
customers = pd.DataFrame({
    "customer_id": [101, 102, 104],
    "name": ["Alice", "Bob", "David"],
    "amount": [1000, 2000, 3000]   # overlapping column
})

print("ORDERS TABLE")
print(orders)
print()

print("CUSTOMERS TABLE")
print(customers)
print()

# -------------------------------
# Merge (LEFT JOIN)
# -------------------------------
merged_df = pd.merge(
    orders,
    customers,
    on="customer_id",
    suffixes=("_amount", "_customer")  # to handle overlapping "amount" column
)

print("MERGED DATAFRAME")
print(merged_df)
print()

# -------------------------------
# Observe suffix columns
# -------------------------------
print("COLUMNS AFTER MERGE")
print(merged_df.columns)
print()

# -------------------------------
# Filtering after merge
# -------------------------------
filtered = merged_df[merged_df["amount_amount"] > 600]

print("FILTERED RESULT (amount_amount > 600)")
print(filtered)
print()