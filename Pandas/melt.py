import pandas as pd

df = pd.DataFrame({
    "student": ["Alice", "Bob", "Charlie"],
    "math": [85, 90, 78],
    "science": [88, 76, 92],
    "english": [90, 84, 80]
})

print("Original DataFrame:")
print(df)

melted_df = pd.melt(
    df,
    id_vars="student",
    var_name="subject",
    value_name="marks"
)

print("\nMelted DataFrame:")
print(melted_df)
