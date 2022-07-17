from matplotlib import pyplot as plt
from molmass import Formula
import numpy as np
import pickle

# Add path to PDB file.
path = r"C:\Users\raiya\OneDrive\_University of Toronto - Mississauga\CSC413H5\Project\5fj8.txt"

def molecular_weight(compound):

    if compound == "":
        return 0

    else:
        try:
            atom = Formula(compound[:1].capitalize())

            i = 1
            while i < len(compound):
                if compound[i].isdigit():
                    i += 1
                else:
                    break

            if i > 1:
                return atom.mass * int(compound[1:i]) + molecular_weight(compound[i:])

            return atom.mass + molecular_weight(compound[1:])

        except:
            atom = Formula(compound[:2].capitalize())

            i = 2
            while i < len(compound):
                if compound[i].isdigit():
                    i += 1
                else:
                    break

            if i > 2:
                return atom.mass * int(compound[2:i]) + molecular_weight(compound[i:])

            return atom.mass + molecular_weight(compound[2:])

def protein(path):
    # Final Data.
    coordinates = []
    ligands = []

    # Filter out of Lines.
    filter = {"", "\n"}

    # Track line.
    n = 0

    reader = open(path)
    for line in reader:
        words = line.split(" ")
        words = [word for word in words if word not in filter]

        if words[0] == "ATOM":
            index = -6

            if len(words[-3]) > 4:
                index += 1

            # Coordinates are obtained as strings.
            x_cord = words[index]
            y_cord = words[index + 1]
            z_cord = words[index + 2]


            try:
                float(z_cord)
            except ValueError:
                coords = words[index + 2].split("-")
                if len(coords) == 2:
                    y_cord = coords[0]
                    z_cord = "-" + coords[1]
                elif len(coords) == 3:
                    y_cord = "-" + coords[1]
                    z_cord = "-" + coords[2]

            # Convert to floats.
            coordinate = [x_cord, y_cord, z_cord]
            try:
                coordinate = tuple([float(dimension) for dimension in coordinate])
            except:
                pass

            # Add to list of coordinates.
            coordinates.append(coordinate)

        elif "HETATM" in words[0]:
            index = -6

            formula = words[1]

            if len(words[-3]) > 4:
                index += 1

            # Ligands are obtained as strings.
            x_cord = words[index]
            y_cord = words[index + 1]
            z_cord = words[index + 2]

            # Convert to floats.
            ligand = [x_cord, y_cord, z_cord]
            ligand = tuple([float(dimension) for dimension in ligand])

            # Add to list of ligands, if sufficient weight.
            if molecular_weight(formula) > 150:
                ligands.append(ligand)


        n += 1

    reader.close()

    protein = (coordinates, ligands)

    return protein

coordinates, ligands = protein(path)


"""
for i in range(1, 911183):
    full_path = path + "\\" + str(i) + ".txt"
    print(i)
    protein(full_path)
"""

output = r"C:\Users\raiya\OneDrive\_University of Toronto - Mississauga\CSC413H5\Project\protein.pkl"

# Save protein coordinates as a file.
"""
with open(output, "wb") as f:
    pickle.dump([coordinates, ligands], f)

# Plot coordinates in 3D.

fig = plt.figure(figsize=(7,7))

ax = fig.add_subplot(115, projection='3d')

for x, y, z in coordinates:
    ax.scatter(x, y, z)

plt.show()
"""
print(("AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE").lower())
