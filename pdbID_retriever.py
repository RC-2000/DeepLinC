import csv

# Add path to protein ID information.
path = r"C:\Users\raiya\OneDrive\_University of Toronto - Mississauga\CSC413H5\Project\author_idx.txt"

# Set of all protein IDs.
protein_ids = []

# Filter out of Lines.
filter = {"", "\n"}

reader = open(path)

# The first 5 lines are part of file header.
for i in range(5):
    reader.readline()

for line in reader:
    words = line.split(" ")
    words = [word for word in words if word not in filter]

    # Determine the protein ID from the line.
    protein_id = words[0]

    protein_ids.append(protein_id)

reader.close()

print(len(protein_ids))

print("-123.43-23".split("-"))