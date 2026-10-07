import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv("../dataset/cleaned_facility_data.csv")


# -------------------------------
# 1. BAR CHART
# Average Cleanliness by Location
# -------------------------------

cleanliness = df.groupby("location")["cleanliness_score"].mean()

cleanliness.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.tight_layout()

plt.savefig("cleanliness_by_location.png")
plt.show()


# -------------------------------
# 2. BAR CHART
# Average Footfall by Location
# -------------------------------

footfall = df.groupby("location")["footfall"].mean()

footfall.plot(kind="bar")

plt.title("Average Footfall by Location")
plt.xlabel("Location")
plt.ylabel("Average Footfall")
plt.tight_layout()

plt.savefig("footfall_by_location.png")
plt.show()


# -------------------------------
# 3. HISTOGRAM
# Cleanliness Score Distribution
# -------------------------------

plt.hist(df["cleanliness_score"], bins=5)

plt.title("Distribution of Cleanliness Scores")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Facilities")
plt.tight_layout()

plt.savefig("cleanliness_histogram.png")
plt.show()


# -------------------------------
# 4. SCATTER PLOT
# Footfall vs Waste Level
# -------------------------------

waste_mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

df["waste_numeric"] = df["waste_level"].map(waste_mapping)

plt.scatter(df["footfall"], df["waste_numeric"])

plt.title("Footfall vs Waste Level")
plt.xlabel("Footfall")
plt.ylabel("Waste Level")
plt.tight_layout()

plt.savefig("footfall_vs_waste.png")
plt.show()


# -------------------------------
# 5. PIE CHART
# Water Availability
# -------------------------------

water = df["water_availability"].value_counts()

plt.pie(
    water,
    labels=water.index,
    autopct="%1.1f%%"
)

plt.title("Water Availability")
plt.savefig("water_availability.png")
plt.show()


print("All visualizations created successfully!")