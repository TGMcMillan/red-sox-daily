import csv

# File path
file_path = "data/red_sox_games.csv"

# Fake game data (just for testing)
new_row = [
    "2026-04-09",
    "Yankees",
    "Home",
    "6",
    "3",
    "Win",
    "Rafael Devers",
    "Brayan Bello",
    "Boston broke it open in the 7th",
    "2026-04-09-blue-jays.md"
]

# Append row to CSV
with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print("Row added successfully!")
