import requests

link = "https://www.rcsb.org/structure/"

def f2():
    # File with all the protein ids
    file = open("protein_ids.txt", "r")
    t = file.read()
    text = t.split(sep=",")

    # Link to the website
    link = "https://files.rcsb.org/view/"
    counter = 0

    # save location
    save = "F:\\413_project\\"
    for protein in text[802468:]:
        flink = link + protein + ".pdb"
        content = requests.get(flink).text
        counter +=1
        f = open(save + str(counter) + ".txt", "w", encoding="utf-8")
        f.write(content)
        f.close()


if __name__ == "__main__":
    f2()
