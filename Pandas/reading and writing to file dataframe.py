import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
input_file = base_dir / "finaoutput.csv"
output_file = base_dir / "highest_amount_by_city.csv"

data = {
    "customer_id": [1, 2, 3],
    "city": ["New York", "Los Angeles", "New York"],
    "amount": [100, 150, 200],
}

df = pd.DataFrame(data)

grouped_df = df.groupby("city", as_index=False)["amount"].sum()
grouped_df = grouped_df.rename(columns={"amount": "grouped_quantity"})
grouped_df["adjusted_quantity"] = grouped_df["grouped_quantity"] * 0.5

grouped_df.to_csv(input_file, index=False)
print("Initial output:")
print(grouped_df)

# Read from previous output, pick the highest amount row per city, then write final output.
read_df = pd.read_csv(input_file)
highest_by_city = (
    read_df.sort_values(["city", "grouped_quantity"], ascending=[True, False])
    .drop_duplicates(subset=["city"], keep="first")
    .reset_index(drop=True)
)

highest_by_city.to_csv(output_file, index=False)
print("\nHighest amount by city:")
print(highest_by_city)

input_file.unlink(missing_ok=True)
print(f"\nDeleted input file: {input_file}")
print(f"Final output written to: {output_file}")
