import pandas as pd
df = pd.read_csv("../datasets/eclipse/eclipse.csv")
df = df.fillna("")
df["text"] = (

    "Product: " + df["Product"].astype(str)

    + "\nComponent: " + df["Component"].astype(str)

    + "\nSeverity: " + df["Severity"].astype(str)

    + "\nPriority: " + df["Priority"].astype(str)

    + "\nSummary: " + df["Summary"].astype(str)

    + "\nResolution: " + df["Resolution"].astype(str)

)

processed = df[[

    "Bug ID",

    "Product",

    "Component",

    "Severity",

    "Priority",

    "Resolution",

    "Summary",

    "text"

]]

processed = processed.sample(
    n=5000,
    random_state=42
)

processed.to_csv(

    "data/processed.csv",

    index=False

)

print(processed.head())

print("\nRows:")

print(len(processed))

print("\nPreprocessing Complete")