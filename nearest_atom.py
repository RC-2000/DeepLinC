import math
import os

glob_path = r"C:\Users\raiya\OneDrive\_University of Toronto - Mississauga\CSC413H5\Project\5fj8.txt"

# Filter out of Lines.
filter = {"", "\n"}

def dist(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

def nearest_residue_pdb(pocket, residue):
    reader = open(path)

    coordinates = []

    min_dist = math.inf
    closest_res = None

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

            if words[3] == residue:
                distance = dist(pocket, coordinate)

                if distance < min_dist:
                    min_dist = distance
                    closest_res = coordinate

    return min_dist, closest_res

def nearest_residue(file):
    reader = open(file)

    coordinates = {}
    for line in reader:
        pocket = line.split(" ")
        dimensions = [float(dimension) for dimension in pocket[1:4]]
        coordinate = tuple(dimensions)
        min_dist, closest_res = nearest_residue_pdb(coordinate, "CYS")
        coordinates[coordinate] = min_dist

    reader.close()

    return coordinates

def nearest_pocket_pdb(residue, pockets):

    x_r, y_r, z_r = residue

    closest_pocket = None
    closest_dist = math.inf

    for pocket in pockets:

        x, y, z = pocket
        distance = dist(residue, pocket)

        if distance < closest_dist:
            closest_dist = distance
            closest_pocket = pocket

    return closest_pocket, closest_dist

def nearest_pocket(file, output_file, code):
    reader = open(file)

    residue_atoms = []

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

            if words[3] == "CYS":
                try:
                    residue_code = int(words[5])
                except:
                    residue_code = words[4][1:]
                    residue_code = int(residue_code)

                if residue_code == code:
                    residue_atoms.append(coordinate)

    reader.close()

    reader = open(output_file)

    pockets = []
    for line in reader:
        words = line.split(" ")
        words = [word for word in words if word not in filter]

        # Coordinates are obtained as strings.
        x_cord = words[1]
        y_cord = words[2]
        z_cord = words[3]

        # Convert to floats.
        coordinate = [x_cord, y_cord, z_cord]

        coordinate = tuple([float(dimension) for dimension in coordinate])

        pockets.append(coordinate)
    reader.close()

    pocket_distances = {}

    best_dist = math.inf
    best_pocket = None

    for atom in residue_atoms:
        pocket_dist = math.inf
        closest_pocket = None

        for pocket in pockets:
            distance = dist(atom, pocket)
            if distance < pocket_dist:
                pocket_dist = distance
                closest_pocket = pocket
                if distance < best_dist:
                    best_dist = distance
                    best_pocket = pocket

        pocket_distances[atom] = pocket_dist

    return pocket_distances

def nearest_residue_excel(pdb_file, csv_file):
    reader = open(csv_file)

    output = []

    for line in reader:
        words = line.split(",")
        for word in words:
            word = word.split("_")
            code = word[1]

            output.append(nearest_pocket(file, output_file, code))

    return output

def extract_uniprots(path):
    uniprots = []
    reader = open(path)
    for line in reader:
        line = line.rstrip()
        words = line.split(" ")
        words = [word for word in words if word not in filter]
        if "UNP" in words:
            for i in range(len(words)):
                if words[i] == "UNP":
                    uniprots.append(words[i+1])
    return uniprots

    reader.close()

def verify_uniprot(uniprot):
    return uniprot in extract_uniprots()

def uniprot_mapping():
    mapping = {}
    for protein in os.listdir("PDB Files"):
        path = "PDB Files/" + protein
        uniprots = extract_uniprots(path)
        id = protein[:-4]
        for uniprot in uniprots:
            if uniprot == "RESIDUES":
                continue
            if uniprot not in mapping:
                mapping[uniprot] = [id]
            elif id not in mapping[uniprot]:
                mapping[uniprot].append(id)

    return mapping

pocket = (150, 155, 170)

pockets = [(x, y, z)
                    for x in range(100)
                    for y in range(100)
                    for z in range(100)]

pocket = (14.542352518343494, -11.491730257430671, -30.959028205447087)

print(uniprot_mapping())