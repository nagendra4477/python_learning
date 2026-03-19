import pandas as pd

orders = pd.DataFrame({
    "order_id": [1,2,3,4],
    "id": [101,102,103,104],
    "amount": [500,700,900,1100]
})

customers = pd.DataFrame({
    "customer_id": [101,102,103],
    "name": ["Alice","Bob","John"],
    "amount": [500,700,900]
})

customers = customers.set_index("customer_id")

#write a code with given suffix

result = orders.join(customers, on="id",lsuffix="_customer", rsuffix="_order", how="inner")

print(result)