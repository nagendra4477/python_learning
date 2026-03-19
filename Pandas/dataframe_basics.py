data = {
    "customer_id": [1, 2, 3],
    "amount": [100, 150, 200],
    "city": ["New York", "Los Angeles", "New York"]
}

import pandas as pd  

df = pd.DataFrame(data)
#print(df)

# df = df[df["amount"] != 150]

# df.reset_index(drop=True, inplace=True)
# print(df)

# mask = df["amount"] > 120

# print(df[mask].shape[1])  # Output: 2




#         col1   col2   col3
# row0      10     20     30
# row1      40     50     60
# row2      70     80     90

# import pandas as pd
# data = {
#     "col1": [10, 40, 70],
#     "col2": [20, 50, 80],
#     "col3": [30, 60, 90]
# }

# df = pd.DataFrame(data, index=["row0", "row1", "row2"])
# print(df.sum(axis=1))


# or operator
mask = (df["amount"] > 120) | (df["city"] == "New York")
print(df[mask])

#not operator
df = df[~(df["amount"] == 150)]
print(df)






