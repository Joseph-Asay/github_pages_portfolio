from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Find the main project folder and load our cleaned dataset
project_folder = Path(__file__).resolve().parent.parent
players = pd.read_csv(project_folder / "data" / "cleaned_players.csv")

# Find the images folder where we will save our graphs
images_folder = project_folder / "images"

# Keep the coaches in chronological order for our graphs
coach_order = ["Dave Rose", "Mark Pope", "Kevin Young"]


# Graph 1: Average height of players under each head coach
avg_height = players.groupby("head_coach")["height_cm"].mean()
avg_height = avg_height.reindex(coach_order)

avg_height.plot(kind="bar", color="steelblue", figsize=(8, 5))

plt.title("Average Player Height by Head Coach")
plt.xlabel("Head Coach")
plt.ylabel("Average Height (cm)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(images_folder / "height_by_coach.png")
plt.close()


# Graph 2: Average height of players across each season
season_height = players.groupby("season")["height_cm"].mean()
season_height = season_height.sort_index()

season_height.plot(kind="line", marker="o", figsize=(10, 5))

plt.title("Average Player Height by Season")
plt.xlabel("Season")
plt.ylabel("Average Height (cm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(images_folder / "height_by_season.png")
plt.close()


# Graph 3: Percentage of international players under each coach
# Because international is binary, the mean gives us a proportion
international_pct = players.groupby("head_coach")["international"].mean() * 100
international_pct = international_pct.reindex(coach_order)

international_pct.plot(kind="bar", color="steelblue", figsize=(8, 5))

plt.title("Percentage of International Players by Head Coach")
plt.xlabel("Head Coach")
plt.ylabel("International Players (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(images_folder / "international_by_coach.png")
plt.close()


# Graph 4: Percentage of players from Utah under each coach
utah_pct = players.groupby("head_coach")["utah"].mean() * 100
utah_pct = utah_pct.reindex(coach_order)

utah_pct.plot(kind="bar", color="steelblue", figsize=(8, 5))

plt.title("Percentage of Utah Players by Head Coach")
plt.xlabel("Head Coach")
plt.ylabel("Utah Players (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(images_folder / "utah_by_coach.png")
plt.close()


# Confirm our graphs were created
print("All four graphs have been saved to the images folder!")
