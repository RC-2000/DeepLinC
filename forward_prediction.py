import subprocess
from nearest_atom import nearest_residue
#subprocess.run(["bash", "prediction.sh"])

protein = input("Enter Four Digit Protein ID And Press Enter: ")
response = subprocess.call("prediction.sh " + protein, shell=True)

print(nearest_residue(protein+".txt"))

#print(nearest_residue_pdb(pocket, "CYS"))
