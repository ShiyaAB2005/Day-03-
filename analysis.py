import pandas as pd

# Read cleaned dataset
df = pd.read_csv("../dataset/cleaned_facility_data.csv")

print("===== DATA ANALYSIS =====")

# Basic information
print("\nDataset Shape:")
print(df.shape)

# Average scores
print("\nAverage Cleanliness Score:")
print(df["cleanliness_score"].mean())

print("\nAverage Odor Score:")
print(df["odor_score"].mean())

# Minimum and maximum
print("\nMinimum Cleanliness Score:")
print(df["cleanliness_score"].min())

print("\nMaximum Cleanliness Score:")
print(df["cleanliness_score"].max())

# Waste level statistics
print("\nWaste Level Count:")
print(df["waste_level"].value_counts())

# Water availability
print("\nWater Availability:")
print(df["water_availability"].value_counts())

# Footfall statistics
print("\nFootfall Statistics:")
print(df["footfall"].describe())

# Location-wise statistics
print("\nLocation-wise Average Cleanliness:")
print(df.groupby("location")["cleanliness_score"].mean())

# Location-wise average footfall
print("\nLocation-wise Average Footfall:")
print(df.groupby("location")["footfall"].mean())

# Correlation
print("\nCleanliness and Footfall Correlation:")
print(df["cleanliness_score"].corr(df["footfall"]))

print("\nAnalysis completed successfully!")