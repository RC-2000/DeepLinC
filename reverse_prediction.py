import subprocess
from nearest_atom import nearest_pocket

protein = input("Enter Four Digit Protein ID And Press Enter: ")
code = int(input("Enter Residue Code And Press Enter: "))
response = subprocess.call("prediction.sh " + protein, shell=True)
output = "protein"
print(nearest_pocket(protein+".txt",output+".txt", code))
